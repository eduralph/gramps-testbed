#!/usr/bin/env bash
# Clone your gramps + addons-source forks as siblings of this testbed repo,
# configure 'upstream' remotes, and check out maintenance/gramps60.
#
# Intended layout after running:
#   <workspace>/
#   ├── gramps/              (fork of gramps-project/gramps)
#   ├── addons-source/       (fork of gramps-project/addons-source)
#   ├── addons/              (upstream read-only, needed by make.py)
#   └── gramps-testbed/      (this repo)
#
# Configuration (override via environment):
#   FORK_OWNER             GitHub owner of your gramps + addons-source forks.
#                          Default: auto-detected from this testbed's origin
#                          remote, so `you/gramps-testbed` picks up
#                          `you/gramps` and `you/addons-source` for free.
#                          Falls back to `eduralph` if detection fails.
#   GRAMPS_FORK_URL        Full URL override for the gramps fork.
#   ADDONS_SRC_FORK_URL    Full URL override for the addons-source fork.
#   BRANCH                 Branch to check out in both forks.
#                          Default: maintenance/gramps60
#
# Usage:
#   ./agent-work/scripts/bootstrap-forks.sh                  # HTTPS, auto-owner
#   ./agent-work/scripts/bootstrap-forks.sh --ssh            # SSH, auto-owner
#   FORK_OWNER=alice ./agent-work/scripts/bootstrap-forks.sh # HTTPS, alice/*

set -euo pipefail

USE_SSH=0
if [[ "${1:-}" == "--ssh" ]]; then
  USE_SSH=1
fi

# Repo root via git (depth-independent — a fixed-depth ../.. walk silently
# breaks on directory moves; see test_runner_workspace_root.py). WORKSPACE
# is its parent, where the sibling gramps/ checkout gets cloned.
TESTBED="$(git -C "$(dirname "${BASH_SOURCE[0]}")" rev-parse --show-toplevel)"
WORKSPACE="$(cd "$TESTBED/.." && pwd)"
cd "$WORKSPACE"

# Auto-detect FORK_OWNER from the testbed's origin remote so a fork of
# gramps-testbed → you/gramps-testbed picks up you/gramps etc. without
# configuration. Fall back to eduralph when there's no detectable remote.
detect_fork_owner() {
  local url owner
  url="$(git -C "$TESTBED" config --get remote.origin.url 2>/dev/null || true)"
  if [[ "$url" =~ github\.com[:/]([^/]+)/ ]]; then
    owner="${BASH_REMATCH[1]}"
    printf '%s' "$owner"
  else
    printf 'eduralph'
  fi
}

FORK_OWNER="${FORK_OWNER:-$(detect_fork_owner)}"
BRANCH="${BRANCH:-maintenance/gramps61}"
UPSTREAM_OWNER="gramps-project"

if (( USE_SSH )); then
  PREFIX="git@github.com:"
else
  PREFIX="https://github.com/"
fi
github_url() { printf '%s%s.git\n' "$PREFIX" "$1"; }

GRAMPS_FORK="${GRAMPS_FORK_URL:-$(github_url "$FORK_OWNER/gramps")}"
ADDONS_SRC_FORK="${ADDONS_SRC_FORK_URL:-$(github_url "$FORK_OWNER/addons-source")}"
GRAMPS_UPSTREAM="$(github_url "$UPSTREAM_OWNER/gramps")"
ADDONS_SRC_UPSTREAM="$(github_url "$UPSTREAM_OWNER/addons-source")"
ADDONS_UPSTREAM="$(github_url "$UPSTREAM_OWNER/addons")"

clone_if_missing() {
  local dir="$1" fork_url="$2" upstream_url="$3" branch="$4"
  if [[ -d "$dir/.git" ]]; then
    echo "✔ $dir already cloned, fetching..."
    git -C "$dir" fetch --all --prune
  else
    echo "→ cloning $dir from $fork_url"
    git clone "$fork_url" "$dir"
    git -C "$dir" remote add upstream "$upstream_url"
    git -C "$dir" fetch upstream
  fi
  # ensure maintenance branch is tracked
  if git -C "$dir" show-ref --verify --quiet "refs/remotes/origin/$branch"; then
    git -C "$dir" checkout -B "$branch" "origin/$branch" 2>/dev/null || \
      git -C "$dir" checkout "$branch"
  fi
}

clone_if_missing "gramps"         "$GRAMPS_FORK"      "$GRAMPS_UPSTREAM"      "$BRANCH"
clone_if_missing "addons-source"  "$ADDONS_SRC_FORK"  "$ADDONS_SRC_UPSTREAM"  "$BRANCH"

# addons: upstream-only, used by make.py as the publish target
if [[ ! -d "addons/.git" ]]; then
  echo "→ cloning addons (upstream read-only)"
  git clone "$ADDONS_UPSTREAM" addons
else
  git -C addons fetch --all --prune
fi

echo
echo "Done. Layout:"
ls -d */ 2>/dev/null | sed 's/^/  /'
echo
echo "Next: sync upstream into your forks when needed:"
echo "  git -C gramps         fetch upstream && git -C gramps         rebase upstream/$BRANCH"
echo "  git -C addons-source  fetch upstream && git -C addons-source  rebase upstream/$BRANCH"
