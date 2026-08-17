# JetBrainsMono Nerd Font for hypr-de-extras.
#
# hypr-DE's waybar/swaync stylesheets set
#   font-family: "JetBrainsMono Nerd Font", "Symbols Nerd Font", sans-serif
# Fedora ships only the plain jetbrains-mono-fonts (no Nerd variants exist in
# the official repos), so on a fresh Fedora install every glyph in the bar and
# notification center renders as tofu. Mirrored from the upstream nerd-fonts
# release archive, matching Arch's ttf-jetbrains-mono-nerd.

Name:           jetbrains-mono-nerd-fonts
Version:        3.5.0
Release:        1%{?dist}
Summary:        JetBrains Mono patched with Nerd Fonts glyphs
License:        OFL-1.1
URL:            https://github.com/ryanoasis/nerd-fonts
Source0:        %{url}/releases/download/v%{version}/JetBrainsMono.tar.xz

BuildArch:      noarch
BuildRequires:  fontpackages-devel

%description
JetBrains Mono patched with the Nerd Fonts glyph set (Powerline, devicons,
codicons, and friends). Provides the "JetBrainsMono Nerd Font" family that
hypr-DE's waybar and swaync stylesheets request.

%prep
%setup -q -c

%build
# Fonts are prebuilt upstream; nothing to compile.

%install
install -d %{buildroot}%{_fontdir}
# Ship the standard variant only; the Mono/Propo repacks triple the size for
# families nothing here references.
install -Dpm0644 JetBrainsMonoNerdFont-*.ttf -t %{buildroot}%{_fontdir}

%files
%license OFL.txt
%doc README.md
%dir %{_fontdir}
%{_fontdir}/*.ttf

%changelog
* Mon Aug 17 2026 Mason Rhodes <mrhodesdev@gmail.com> - 3.5.0-1
- Initial package for hypr-de's Fedora font gap (upstream nerd-fonts v3.5.0)
