# hypr-de-extras

Third-party packages **hypr-DE** requires that Fedora official repos, `nett00n/hyprland`, and `heus-sueh/packages` do not ship under the names in `hypr-DE/deps.toml`.

Hosted on COPR **`solaris765/hypr-de-extras`** and Arch **`[mason]`**. A `v*` tag publishes both; do not submit COPR from a laptop.

## Inventory

| Package | Why Mason hosts it | Arch extra | Fedora | nett00n / heus-sueh |
|---|---|---|---|---|
| `overskride` | Bluetooth UI; AUR-only | no | no | no |

`hyprshutdown` and `hyprland-guiutils` specs remain in-tree as a fallback. **nett00n/hyprland** ships current builds of both; do not register them on extras unless that COPR drops them.

Not in this repo:

- Mason tools → per-project `solaris765/<name>` COPRs, published by that repo's tag workflow
- Hyprland stack → `nett00n/hyprland`
- `matugen` → `heus-sueh/packages`

## Release

1. Bump `packaging/overskride.spec` Version + `%changelog` and `packaging/PKGBUILD` `pkgver`/`sha256sums` together (upstream tag).
2. `git tag vX.Y.Z && git push --tags`
3. CI builds the Arch package, attaches it to the GitHub Release, submits the SRPM to COPR (creating `hypr-de-extras` if needed, with network enabled for cargo), and dispatches arch-repo.

Org secrets required: `COPR_CONFIG`, `ARCH_REPO_TOKEN`.

`get-hypr-de.sh` enables `solaris765/hypr-de-extras`.
