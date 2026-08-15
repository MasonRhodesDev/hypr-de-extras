Name:           hyprshutdown
Version:        0.1.1
Release:        1%{?dist}
Summary:        Graceful shutdown utility for Hyprland

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprshutdown
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(hyprtoolkit)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  cmake(glaze)

Requires:       systemd

%description
Graceful shutdown/logout utility for Hyprland. hypr-DE's power menu invokes
it; Fedora and solopasha/hyprland do not ship this package.

%prep
%autosetup

%build
%cmake -GNinja -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/hyprshutdown

%changelog
* Sat Aug 15 2026 Mason Rhodes <mrhodesdev@gmail.com> - 0.1.1-1
- Initial COPR package for hypr-DE
