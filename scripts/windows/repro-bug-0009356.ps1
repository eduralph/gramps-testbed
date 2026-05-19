<#
.SYNOPSIS
    Manual repro / verification script for Gramps bug 0009356.

.DESCRIPTION
    Bug 0009356: "Working Installation Crash & New Install Crash due to
    PYTHONHOME" -- https://gramps-project.org/bugs/view.php?id=9356

    Original (2016) symptom on Gramps 4.2.x:
        Setting PYTHONHOME=<some other Python install> in the
        environment, then launching gramps.exe, produced:
            Fatal Python error: Py_Initialize: unable to load the file system codec
            ImportError: No module named 'encodings'
        followed by "This application has requested the Runtime to
        terminate it in an unusual way."

    Root cause: the 4.2-era launcher (custom C, gramps.c -> gramps.exe)
    called Py_Initialize() without setting Py_IgnoreEnvironmentFlag,
    so an externally-defined PYTHONHOME pointed CPython at the wrong
    encodings/ tree and startup failed.

    Modern AIO architecture (Gramps 6.x) replaces that C launcher
    with cx_Freeze-frozen Python entry points (grampsaiow.py,
    grampsaioc.py, grampsaiocd.py -- see ../gramps/aio/setup.py). The
    cx_Freeze bootloader calls Py_SetPythonHome to the frozen bundle's
    directory before Py_Initialize, which is documented to override
    any external PYTHONHOME. So the 2016 failure mode is expected to
    be obsolete -- but obsolete is a hypothesis until verified.

    This script verifies that hypothesis on a current Windows AIO
    install. It runs Gramps' console entry point with `--version` (a
    quick smoke that forces Py_Initialize without launching the GUI),
    twice:
        1. Baseline:   no PYTHONHOME set
        2. With PYTHONHOME pointing at a nonexistent path

    If both runs print the same version string with exit code 0, bug
    9356 is obsolete on the tested build. If run #2 fails / differs,
    the bug still reproduces and the original Py_IgnoreEnvironmentFlag
    fix (or equivalent cx_Freeze override) needs revisiting.

.PARAMETER InstallDir
    Path to the Gramps AIO `bin` directory (containing grampsc.exe or
    gramps.exe). If omitted, the script auto-detects the most-recent
    GrampsAIO64-* install under Program Files.

.EXAMPLE
    .\repro-bug-0009356.ps1

.EXAMPLE
    .\repro-bug-0009356.ps1 -InstallDir 'C:\Program Files\GrampsAIO64-6.0.8\bin'

.NOTES
    Author: gramps-testbed
    Run from any PowerShell prompt; no admin required.
#>

[CmdletBinding()]
param(
    [string]$InstallDir
)

$ErrorActionPreference = 'Stop'

function Find-GrampsLauncher {
    param([string]$Dir)

    # AIO names the console launcher 'grampsc.exe' in current builds;
    # older 4.x AIOs called it 'gramps.exe'. Pick whichever exists.
    foreach ($name in @('grampsc.exe', 'gramps.exe')) {
        $path = Join-Path $Dir $name
        if (Test-Path -LiteralPath $path) { return $path }
    }
    return $null
}

function Resolve-AioInstallDir {
    param([string]$ExplicitDir)

    if ($ExplicitDir) {
        if (-not (Test-Path -LiteralPath $ExplicitDir)) {
            throw "InstallDir '$ExplicitDir' does not exist."
        }
        return (Resolve-Path -LiteralPath $ExplicitDir).Path
    }

    # Search both Program Files trees; sort by version-suffix descending
    # so the newest install wins when several are present side-by-side.
    $candidates = @()
    foreach ($root in @($env:ProgramFiles, ${env:ProgramFiles(x86)})) {
        if (-not $root) { continue }
        $matches = Get-ChildItem -LiteralPath $root -Directory `
            -Filter 'GrampsAIO*' -ErrorAction SilentlyContinue
        foreach ($m in $matches) {
            $bin = Join-Path $m.FullName 'bin'
            if (Test-Path -LiteralPath $bin) { $candidates += $bin }
        }
    }

    if ($candidates.Count -eq 0) {
        throw @"
No GrampsAIO install found under Program Files. Pass -InstallDir
explicitly, e.g.:
    .\repro-bug-0009356.ps1 -InstallDir 'C:\Program Files\GrampsAIO64-6.0.8\bin'
"@
    }
    return ($candidates | Sort-Object -Descending | Select-Object -First 1)
}

function Invoke-GrampsVersion {
    param(
        [string]$LauncherPath,
        [hashtable]$ExtraEnv
    )

    # Run the launcher in a child PowerShell so env overrides are
    # scoped to this invocation only -- the calling shell stays clean.
    # `cmd /c` captures both stdout and stderr; Start-Process with
    # -RedirectStandard* is more verbose without buying anything here.
    $envPrefix = ''
    foreach ($k in $ExtraEnv.Keys) {
        $v = $ExtraEnv[$k]
        $envPrefix += "set `"$k=$v`" && "
    }
    # Use --version: forces Py_Initialize, exits ~immediately, no GUI.
    $cmd = "$envPrefix`"$LauncherPath`" --version 2>&1"

    $started = Get-Date
    $output = & cmd.exe /c $cmd
    $exitCode = $LASTEXITCODE
    $elapsed = (Get-Date) - $started

    return [PSCustomObject]@{
        ExitCode = $exitCode
        Output   = ($output -join "`n")
        Elapsed  = $elapsed
    }
}

# ---- main -------------------------------------------------------------

$installDir = Resolve-AioInstallDir -ExplicitDir $InstallDir
$launcher = Find-GrampsLauncher -Dir $installDir
if (-not $launcher) {
    throw "Neither grampsc.exe nor gramps.exe found under '$installDir'."
}

Write-Host "-> Using launcher: $launcher" -ForegroundColor Cyan
Write-Host ""

# ---- Run 1: baseline (no PYTHONHOME) ----------------------------------
Write-Host "=== Run 1: baseline (no PYTHONHOME) ===" -ForegroundColor Yellow
$baseline = Invoke-GrampsVersion -LauncherPath $launcher -ExtraEnv @{}
Write-Host "exit code: $($baseline.ExitCode)"
Write-Host "elapsed:   $([math]::Round($baseline.Elapsed.TotalSeconds, 2))s"
Write-Host "--- output ---"
Write-Host $baseline.Output
Write-Host "--------------"
Write-Host ""

# ---- Run 2: with bogus PYTHONHOME -------------------------------------
$bogusPython = 'C:\nonexistent-python-for-bug-9356-repro'
Write-Host "=== Run 2: PYTHONHOME=$bogusPython ===" -ForegroundColor Yellow
$withPythonhome = Invoke-GrampsVersion -LauncherPath $launcher `
    -ExtraEnv @{ PYTHONHOME = $bogusPython }
Write-Host "exit code: $($withPythonhome.ExitCode)"
Write-Host "elapsed:   $([math]::Round($withPythonhome.Elapsed.TotalSeconds, 2))s"
Write-Host "--- output ---"
Write-Host $withPythonhome.Output
Write-Host "--------------"
Write-Host ""

# ---- Verdict ----------------------------------------------------------
Write-Host "=== Verdict ===" -ForegroundColor Yellow

# Original 2016 fingerprint: 'Py_Initialize: unable to load the file
# system codec' + ModuleNotFoundError for 'encodings'. Either string
# (or any exit-code-0 -> exit-code-nonzero divergence) means the bug
# still reproduces.
$originalFingerprint = @(
    'Py_Initialize: unable to load the file system codec',
    "No module named 'encodings'",
    'Fatal Python error'
)

$reproduced = $false
$reason = ''

if ($baseline.ExitCode -ne 0) {
    $reason = "Baseline run did not exit cleanly (exit=$($baseline.ExitCode)) -- cannot conclude. Investigate the Gramps install before retrying."
}
elseif ($withPythonhome.ExitCode -ne 0) {
    $reproduced = $true
    $reason = "PYTHONHOME-set run failed (exit=$($withPythonhome.ExitCode)) while baseline succeeded."
}
else {
    foreach ($fp in $originalFingerprint) {
        if ($withPythonhome.Output -match [regex]::Escape($fp)) {
            $reproduced = $true
            $reason = "PYTHONHOME-set run printed the original 2016 fingerprint: '$fp'"
            break
        }
    }
    if (-not $reproduced) {
        $reason = "Both runs exited cleanly and neither emitted the 2016 fingerprint. Bug 9356 appears obsolete on this AIO build."
    }
}

if ($reproduced) {
    Write-Host "REPRODUCED -- bug 9356 still occurs." -ForegroundColor Red
    Write-Host $reason
    exit 1
} else {
    Write-Host "NOT REPRODUCED -- bug 9356 appears obsolete." -ForegroundColor Green
    Write-Host $reason
    exit 0
}
