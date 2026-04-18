#!/usr/bin/env bash
# Clone your gramps + addons-source forks as siblings of this testbed repo,
# configure 'upstream' remotes, and check out maintenance/gramps60.
#
# Intended layout after running:
#   <workspace>/
#   ├── gramps/              (fork: eduralph/gramps)
#   ├── addons-source/       (fork: eduralph/addons-source)
#   ├── addons/              (upstream read-only, needed by make.py)
#   └── gramps-testbed/      (this repo)
#
# Usage:
#   cd <workspace>/gramps-testbed
#   ./scripts/bootstrap-forks.sh [--ssh]

set -euo pipefail

USE_SSH=0
if [[ "${1:-}" == "--ssh" ]]; then
  USE_SSH=1
fi

WORKSPACE="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$WORKSPACE"

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

if (( USE_SSH )); then
  GRAMPS_FORK="git@github.com:eduralph/gramps.git"
  ADDONS_SRC_FORK="git@github.com:eduralph/addons-source.git"
  GRAMPS_UPSTREAM="git@github.com:gramps-project/gramps.git"
  ADDONS_SRC_UPSTREAM="git@github.com:gramps-project/addons-source.git"
  ADDONS_UPSTREAM="git@github.com:gramps-project/addons.git"
else
  GRAMPS_FORK="https://github.com/eduralph/gramps.git"
  ADDONS_SRC_FORK="https://github.com/eduralph/addons-source.git"
  GRAMPS_UPSTREAM="https://github.com/gramps-project/gramps.git"
  ADDONS_SRC_UPSTREAM="https://github.com/gramps-project/addons-source.git"
  ADDONS_UPSTREAM="https://github.com/gramps-project/addons.git"
fi

BRANCH="maintenance/gramps60"

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
