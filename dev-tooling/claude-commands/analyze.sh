#!/usr/bin/env bash
# dev-tooling/claude-commands/analyze.sh
# Runs the scoped pyright + semgrep analyzers against the sibling ../gramps fork and
# writes structured findings to dev-tooling/findings/ for Claude Code (or a human) to read.
#
# Usage (from the gramps-testbed repo root):
#   ./dev-tooling/claude-commands/analyze.sh                 # analyze the default gui/ scope
#   ./dev-tooling/claude-commands/analyze.sh ../gramps/gramps/gui/widgets/fanchart.py   # narrow
#
# Output:
#   dev-tooling/findings/pyright.json   (--outputjson)
#   dev-tooling/findings/semgrep.json   (--json)
#   dev-tooling/findings/summary.txt    (human-skimmable counts + one-line-per-finding)
#
# findings/ is gitignored: regenerable analyzer output, same discipline as triage/data/.
set -uo pipefail

# Resolve repo root regardless of where the script is called from.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$ROOT" || exit 1

SEMGREP_TARGET="${1:-../gramps/gramps/gui/}"
OUT="dev-tooling/findings"
mkdir -p "$OUT"

PYRIGHT_CFG="dev-tooling/pyright/pyrightconfig.experiment.json"
SEMGREP_RULES="dev-tooling/semgrep/rules/"

echo "==> pyright (scoped None-flow)"
pyright --project "$PYRIGHT_CFG" --outputjson > "$OUT/pyright.json" 2> "$OUT/pyright.stderr.txt"
PYRIGHT_RC=$?

echo "==> semgrep (gramps shape patterns) on $SEMGREP_TARGET"
semgrep --config "$SEMGREP_RULES" --json "$SEMGREP_TARGET" > "$OUT/semgrep.json" 2> "$OUT/semgrep.stderr.txt"
SEMGREP_RC=$?

# Build a compact, skimmable summary from the JSON. Pure stdlib; no jq dependency.
python3 - "$OUT" << 'PY'
import json, sys, collections, os
out = sys.argv[1]

def load(p):
    try:
        with open(p) as f: return json.load(f)
    except Exception as e:
        return {"_error": str(e)}

pr = load(os.path.join(out, "pyright.json"))
sg = load(os.path.join(out, "semgrep.json"))

lines = []
lines.append("# dev-tooling analyzer findings\n")

# --- pyright ---
diags = pr.get("generalDiagnostics", []) if isinstance(pr, dict) else []
by_rule = collections.Counter(d.get("rule", "(no-rule)") for d in diags)
lines.append("## pyright (scoped None-flow)")
if "_error" in pr:
    lines.append(f"  ERROR reading pyright.json: {pr['_error']}")
else:
    summ = pr.get("summary", {})
    lines.append(f"  files={summ.get('filesAnalyzed','?')} "
                 f"errors={summ.get('errorCount','?')} "
                 f"warnings={summ.get('warningCount','?')}")
    for rule, n in by_rule.most_common():
        lines.append(f"  {n:4}  {rule}")
    # flag anything that is NOT one of the five intended Optional rules
    intended = {"reportOptionalMemberAccess","reportOptionalSubscript","reportOptionalCall",
                "reportOptionalOperand","reportOptionalIterable"}
    leaked = [r for r in by_rule if r not in intended and r != "(no-rule)"]
    if leaked:
        lines.append(f"  !! NON-Optional rules leaked (config/include too broad?): {', '.join(leaked)}")
lines.append("")

# one line per pyright finding
for d in diags:
    rng = d.get("range", {}).get("start", {})
    lines.append(f"  {d.get('file','?')}:{rng.get('line','?')+1 if isinstance(rng.get('line'),int) else '?'}:"
                 f"{rng.get('character','?')+1 if isinstance(rng.get('character'),int) else '?'}  "
                 f"[{d.get('rule','')}] {d.get('message','').splitlines()[0][:100]}")
lines.append("")

# --- semgrep ---
results = sg.get("results", []) if isinstance(sg, dict) else []
sg_by_rule = collections.Counter(r.get("check_id","?").split('.')[-1] for r in results)
lines.append("## semgrep (gramps shape patterns)")
if "_error" in sg:
    lines.append(f"  ERROR reading semgrep.json: {sg['_error']}")
else:
    lines.append(f"  findings={len(results)}")
    for rule, n in sg_by_rule.most_common():
        lines.append(f"  {n:4}  {rule}")
lines.append("")
for r in results:
    s = r.get("start", {})
    lines.append(f"  {r.get('path','?')}:{s.get('line','?')}:{s.get('col','?')}  "
                 f"[{r.get('check_id','').split('.')[-1]}]")
lines.append("")

with open(os.path.join(out, "summary.txt"), "w") as f:
    f.write("\n".join(lines))
print("\n".join(lines))
PY

echo ""
echo "==> wrote $OUT/{pyright.json,semgrep.json,summary.txt}"
echo "    pyright rc=$PYRIGHT_RC  semgrep rc=$SEMGREP_RC"
echo "    In Claude Code:  /analyze   (or: read dev-tooling/findings/summary.txt)"
