Name:           hyprland-guiutils
Version:        0.2.2
Release:        1%{?dist}
Summary:        Hyprland GUI utilities

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland-guiutils
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(hyprtoolkit)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(xkbcommon)

# solopasha still ships the pre-rename package.
Obsoletes:      hyprland-qtutils <= 0.1.5
Provides:       hyprland-qtutils = %{version}-%{release}

%description
Hyprland GUI utilities including hyprland-dialog. Replaces the older
hyprland-qtutils name. Hosted here because Fedora does not ship it and
solopasha/hyprland still builds the 0.1.5 qtutils package.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/hyprland-dialog
%{_bindir}/hyprland-donate-screen
%{_bindir}/hyprland-run
%{_bindir}/hyprland-update-screen
%{_bindir}/hyprland-welcome

%changelog
* Sat Aug 15 2026 Mason Rhodes <mrhodesdev@gmail.com> - 0.2.2-1
- Initial COPR package for hypr-DE (replaces hyprland-qtutils)
