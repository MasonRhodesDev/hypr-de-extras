#!/bin/bash
# Create solaris765/hypr-de-extras and register the third-party SCM packages.
# Requires copr-cli and ~/.config/copr (https://copr.fedorainfracloud.org/api/).
set -euo pipefail

PROJECT="${COPR_PROJECT:-hypr-de-extras}"
CLONE="${CLONE_URL:-https://github.com/MasonRhodesDev/hypr-de-extras.git}"
CHROOTS=(fedora-42-x86_64 fedora-43-x86_64 fedora-rawhide-x86_64)

if ! command -v copr-cli >/dev/null; then
    echo "install copr-cli (Fedora: dnf install copr-cli) and put a token in ~/.config/copr" >&2
    exit 1
fi

if ! copr-cli list-packages "$PROJECT" >/dev/null 2>&1; then
    echo "==> creating COPR project $PROJECT"
    args=()
    for c in "${CHROOTS[@]}"; do
        args+=(--chroot "$c")
    done
    copr-cli create "$PROJECT" "${args[@]}" \
        --description "Third-party packages hypr-DE needs that Fedora, solopasha/hyprland, and heus-sueh/packages do not ship."
fi

echo "==> enable network during builds (overskride cargo fetch)"
copr-cli modify "$PROJECT" --enable-net on >/dev/null 2>&1 || \
    echo "!! could not set --enable-net; set it in the COPR web UI for overskride" >&2

add_scm() {
    local name=$1
    if copr-cli get-package "$PROJECT" --name "$name" >/dev/null 2>&1; then
        echo "==> updating $name"
        copr-cli edit-package-scm "$PROJECT" \
            --name "$name" \
            --clone-url "$CLONE" \
            --commit main \
            --subdir "$name" \
            --spec "$name.spec" \
            --type git \
            --method rpkg \
            --webhook-rebuild on
    else
        echo "==> adding $name"
        copr-cli add-package-scm "$PROJECT" \
            --name "$name" \
            --clone-url "$CLONE" \
            --commit main \
            --subdir "$name" \
            --spec "$name.spec" \
            --type git \
            --method rpkg \
            --webhook-rebuild on
    fi
}

add_scm overskride
add_scm hyprshutdown
add_scm hyprland-guiutils

echo "==> submitting builds"
copr-cli build-package "$PROJECT" --name overskride --nowait || true
copr-cli build-package "$PROJECT" --name hyprshutdown --nowait || true
copr-cli build-package "$PROJECT" --name hyprland-guiutils --nowait || true

if ! copr-cli list-packages hyprstate-gui >/dev/null 2>&1; then
    echo "==> hyprstate-gui COPR project is missing (own software, not this repo)."
    echo "    copr-cli create hyprstate-gui --chroot fedora-42-x86_64 --chroot fedora-43-x86_64"
    echo "    then point its SCM at https://github.com/MasonRhodesDev/hyprstate-gui (.copr/Makefile)"
fi

echo "done. enable with: dnf copr enable solaris765/$PROJECT"
