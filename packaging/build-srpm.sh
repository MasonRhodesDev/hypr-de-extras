#!/bin/bash
# Build the overskride SRPM from the pinned upstream tarball and optionally
# submit it to COPR. This repo is packaging-only; CI on a v* tag publishes
# Arch and COPR. Do not release from a laptop.
#
# --head skips the tag gate (PR/CI testing only).
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
NAME=overskride
SPEC="$REPO/packaging/$NAME.spec"
SOURCES="${HOME}/rpmbuild/SOURCES"
COPR_PROJECT="${COPR_PROJECT:-hypr-de-extras}"

VER=$(sed -n 's/^Version:[[:space:]]*//p' "$SPEC")
PKGBUILD_VER=$(sed -n 's/^pkgver=//p' "$REPO/packaging/PKGBUILD")
if [ "$PKGBUILD_VER" != "$VER" ]; then
    echo "ERROR: version mismatch: spec Version=$VER, PKGBUILD pkgver=$PKGBUILD_VER" >&2
    exit 1
fi

REF="v$VER"
if [ "${1:-}" = "--head" ]; then
    echo "WARNING: building from HEAD (testing only); still fetching upstream $REF"
    shift
elif ! git -C "$REPO" rev-parse -q --verify "refs/tags/$REF" >/dev/null; then
    echo "ERROR: tag $REF not found — tag the extras release first (or use --head to test)" >&2
    exit 1
fi

mkdir -p "$SOURCES"
echo "==> fetching upstream $NAME $REF"
if command -v spectool >/dev/null; then
    spectool -g -C "$SOURCES" "$SPEC"
else
    url=$(sed -n 's/^URL:[[:space:]]*//p' "$SPEC")
    curl -fsSL -o "$SOURCES/v$VER.tar.gz" "$url/archive/refs/tags/v$VER.tar.gz"
fi

echo "==> building SRPM"
SRPM=$(rpmbuild -bs "$SPEC" | sed -n 's/^Wrote: //p')
echo "    $SRPM"
rpmlint --rpmlintrc "$REPO/packaging/$NAME.rpmlintrc" "$SRPM"

if [ "${1:-}" = "--copr" ]; then
    echo "==> submitting to COPR project $COPR_PROJECT"
    if ! copr-cli build "$COPR_PROJECT" "$SRPM"; then
        echo "ERROR: copr build failed. If this was a 401, the API token has" >&2
        echo "expired (~180 days) — renew at https://copr.fedorainfracloud.org/api/" >&2
        echo "and update the GitHub org secret COPR_CONFIG." >&2
        exit 1
    fi
fi
