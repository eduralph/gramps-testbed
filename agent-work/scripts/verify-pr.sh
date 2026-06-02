#!/usr/bin/env bash
# Poll a GitHub PR's checks until they all complete; report green/red.
#
# Usage: verify-pr.sh <repo> <PR#> [--watch]
#
#   repo  = org/repo (e.g. gramps-project/gramps, gramps-project/addons-source,
#                    Ralphovi/gramps-testbed)
#   PR#   = pull-request number
#   --watch (optional) = keep polling until every check has a terminal
#           status (pass / fail / skip). Without --watch, prints the
#           current snapshot and exits.
#
# Exit codes:
#   0   all required checks green (or no checks at all -- still draft, etc.)
#   1   at least one check failed
#   2   --watch timed out (default 30 minutes)
#   3   usage error / gh not available
#
# Designed to be called manually after a push, or wired into a
# post-push agent step. NOT a git hook -- git has no post-push hook,
# and a pre-push hook can't see the resulting CI run anyway.

set -euo pipefail

usage() {
    cat >&2 <<EOF
Usage: $0 <repo> <PR#> [--watch]
  repo   org/repo (e.g. gramps-project/gramps)
  PR#    pull-request number
  --watch  keep polling until all checks complete (default 30min timeout)
EOF
    exit 3
}

[[ $# -ge 2 ]] || usage
repo="$1"
pr="$2"
watch="${3:-}"

if ! command -v gh >/dev/null 2>&1; then
    echo "error: gh not on PATH" >&2
    exit 3
fi

poll_interval=30   # seconds between polls in --watch mode
max_wait=1800      # 30-minute ceiling
elapsed=0

snapshot() {
    # `gh pr checks` exit codes:
    #   0 = all required checks pass
    #   1 = some required checks failed
    #   8 = checks still running
    # We capture text and ignore the exit code; the printout below
    # determines our own exit.
    gh pr checks "$pr" --repo "$repo" 2>/dev/null || true
}

evaluate() {
    local out="$1"
    local fail=0 pending=0 total=0
    while IFS=$'\t' read -r name status duration url; do
        [[ -z "$name" ]] && continue
        total=$((total + 1))
        case "$status" in
            pass|skipping)
                ;;
            fail)
                fail=$((fail + 1))
                ;;
            pending|in_progress|queued)
                pending=$((pending + 1))
                ;;
            *)
                # unknown status -- treat as pending to be safe
                pending=$((pending + 1))
                ;;
        esac
    done <<< "$out"
    echo "$total $fail $pending"
}

print_summary() {
    local out="$1"
    if [[ -z "$out" ]]; then
        echo "(no checks reported; PR may still be draft or just pushed)"
        return
    fi
    echo "$out" | awk -F'\t' '{
        sym = $2 == "pass"    ? "✓" :
              $2 == "fail"    ? "✗" :
              $2 == "skipping" ? "-"      : "·"
        printf "  %s %-50s %s\n", sym, $1, $2
    }'
}

while :; do
    out=$(snapshot)
    read -r total fail pending < <(evaluate "$out")

    print_summary "$out"
    echo
    echo "  total=$total  fail=$fail  pending=$pending"

    if [[ "$watch" != "--watch" ]]; then
        if [[ "$fail" -gt 0 ]]; then exit 1; fi
        exit 0
    fi

    if [[ "$pending" -eq 0 ]]; then
        if [[ "$fail" -gt 0 ]]; then
            echo
            echo "FAIL: $fail check(s) red on $repo PR #$pr"
            exit 1
        fi
        echo
        echo "GREEN: all checks complete on $repo PR #$pr"
        exit 0
    fi

    if (( elapsed >= max_wait )); then
        echo
        echo "TIMEOUT after ${max_wait}s; $pending check(s) still pending"
        exit 2
    fi

    echo "  -- $pending check(s) pending; sleeping ${poll_interval}s --"
    sleep "$poll_interval"
    elapsed=$((elapsed + poll_interval))
done
