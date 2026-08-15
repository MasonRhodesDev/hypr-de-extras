# hypr-de-extras

Third-party packages **hypr-DE** requires that Fedora official repos, `solopasha/hyprland`, and `heus-sueh/packages` do not ship under the names in `hypr-DE/deps.toml`.

Hosted on COPR **`solaris765/hypr-de-extras`**. Arch extra already has `hyprshutdown` and `hyprland-guiutils`; only **overskride** is also packaged here for `[mason]`.

## Inventory

| Package | Why Mason hosts it | Arch extra | Fedora | solopasha / heus-sueh |
|---|---|---|---|---|
| `overskride` | Bluetooth UI; AUR-only | no | no | no |
| `hyprshutdown` | power-menu binary | yes | no | no |
| `hyprland-guiutils` | `hyprland-dialog`; solopasha still ships stale `hyprland-qtutils` 0.1.5 | yes | no | name/version mismatch |

Not in this repo (already ship elsewhere, or explicitly weak):

- Mason tools → per-project `solaris765/<name>` COPRs
- Hyprland stack (`hyprland`, `hyprpwcenter`, `hyprsunset`, `uwsm`, `matugen`, …) → Fedora and/or `solopasha/hyprland` / `heus-sueh/packages`
- `gpu-screen-recorder` → Fedora weak dep, 1.0-gate
- `hyprstate-gui` → own repo/spec; COPR *project* still needs creating (`copr-cli create hyprstate-gui`)

## COPR

```sh
# token: https://copr.fedorainfracloud.org/api/
./scripts/setup-copr.sh
```

`get-hypr-de.sh` enables `solaris765/hypr-de-extras`.

Overskride’s Meson build runs `cargo` and needs **network during the RPM build** (crate fetch). The setup script turns that on for this COPR.
