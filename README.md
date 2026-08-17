# hypr-de-extras

Third-party packages **hypr-DE** requires that Fedora official repos do not
ship under the names in `hypr-DE/deps.toml`, plus a mirror of the Hyprland
library stack so hypr-DE's Fedora path never depends on an unowned COPR's
chroot or release decisions (solopasha dropped f43/f44 silently; eddievs lags
— hypridle stopped at 0.1.7, whose `-c` flag is advertised but unimplemented).

Hosted on COPR **`solaris765/hypr-de-extras`** and (overskride only) Arch
**`[mason]`**. Everything publishes through CI; **do not submit COPR from a
laptop.**

## Inventory

| Package | Source of truth | Why |
|---|---|---|
| `overskride` | `packaging/` + `v*` tag | Bluetooth UI; AUR-only, no Fedora package anywhere |
| `jetbrains-mono-nerd-fonts`, `nerd-fonts-symbols` | `<name>/<name>.spec` | Fedora ships zero Nerd fonts; the waybar/swaync stylesheets request these families by name |
| `hypridle` (0.1.8+) | `hypridle/hypridle.spec` | 0.1.7's `-c` is a no-op → SIGABRT under hypr-DE's drop-in; nobody else packages 0.1.8 |
| `hyprutils`, `hyprlang`, `hyprgraphics`, `aquamarine`, `hyprtoolkit`, `hyprwayland-scanner`, `glaze`, `hyprland-protocols` | `<name>/<name>.spec` (mirrored from eddievs SRPMs) | Fedora's copies are too old for the stack (scanner < 0.4.4 miscompiles aquamarine; hyprutils 0.7 vs required ≥ 0.8) |
| `hyprlock`, `hyprpicker`, `hyprcursor`, `hyprland-qt-support`, `xdg-desktop-portal-hyprland`, `hyprland-guiutils`, `hyprshutdown` | `<name>/<name>.spec` | soname-locked to the mirrored hyprutils/hyprlang — must move together |

The stack is soname-locked (libhyprutils.so.13 as of hyprutils 0.14): never
bump one of the lib packages without rebuilding its dependents in the same
pass.

Not in this repo:

- Mason tools → per-project `solaris765/<name>` COPRs, published by that
  repo's tag workflow
- `hyprland` itself + `uwsm` → `nett00n/hyprland` (hypr-de Requires
  python3-pyxdg directly because that uwsm RPM omits it)
- `matugen` → `heus-sueh/packages`

## Release

**overskride** (Fedora + Arch from one tag):

1. Bump `packaging/overskride.spec` Version + `%changelog` and
   `packaging/PKGBUILD` `pkgver`/`sha256sums` together (upstream tag).
2. `git tag vX.Y.Z && git push --tags`
3. `release.yml` builds the Arch package, attaches it to the GitHub Release,
   submits the SRPM to COPR, and dispatches arch-repo.

**Everything else** (Fedora only): edit the package's spec (bump Version /
add a patch) and push to main. `fedora-stack.yml` rebuilds exactly the
packages the push touched — SRPM from the spec with sources fetched from the
upstream URLs, submitted to COPR, CI red if the COPR build fails. Releases
come from rpmautospec (`%autorelease` counts commits touching the spec).
`workflow_dispatch` rebuilds a named set or `all`.

Repo secrets required: `COPR_CONFIG`, `ARCH_REPO_TOKEN`.

`get-hypr-de.sh` enables `solaris765/hypr-de-extras`.
