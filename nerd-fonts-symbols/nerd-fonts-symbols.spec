# Symbols Nerd Font (icons-only) for hypr-de-extras.
#
# Fallback family in hypr-DE's stylesheets:
#   font-family: "JetBrainsMono Nerd Font", "Symbols Nerd Font", sans-serif
# The symbols-only font lets any base font pick up Nerd glyphs through
# fontconfig fallback. No Fedora package exists; mirrored from the upstream
# nerd-fonts release archive (Arch: ttf-nerd-fonts-symbols).

Name:           nerd-fonts-symbols
Version:        3.5.0
Release:        1%{?dist}
Summary:        Nerd Fonts symbols-only font (icon glyphs for fallback)
License:        OFL-1.1
URL:            https://github.com/ryanoasis/nerd-fonts
Source0:        %{url}/releases/download/v%{version}/NerdFontsSymbolsOnly.tar.xz

BuildArch:      noarch
BuildRequires:  fontpackages-devel

%description
The Nerd Fonts symbols-only font ("Symbols Nerd Font"): every Nerd Fonts icon
glyph with no letterforms, intended as a fontconfig fallback so unpatched
fonts can render icon codepoints.

%prep
%setup -q -c

%build
# Fonts are prebuilt upstream; nothing to compile.

%install
install -d %{buildroot}%{_fontdir}
install -Dpm0644 SymbolsNerdFont*.ttf -t %{buildroot}%{_fontdir}
# Upstream's fontconfig snippet: aliases the symbols font as a fallback so
# unpatched fonts pick up Nerd glyph codepoints — the whole point of the pkg.
install -Dpm0644 10-nerd-font-symbols.conf \
    %{buildroot}%{_sysconfdir}/fonts/conf.d/10-nerd-font-symbols.conf

%files
%license LICENSE
%doc README.md
%dir %{_fontdir}
%{_fontdir}/*.ttf
%config(noreplace) %{_sysconfdir}/fonts/conf.d/10-nerd-font-symbols.conf

%changelog
* Mon Aug 17 2026 Mason Rhodes <mrhodesdev@gmail.com> - 3.5.0-1
- Initial package for hypr-de's Fedora font gap (upstream nerd-fonts v3.5.0)
