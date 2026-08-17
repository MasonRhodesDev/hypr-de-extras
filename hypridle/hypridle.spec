# hypridle 0.1.8.
#
# Rebased from the 0.1.7 packaging in eddievs/hyprland. 0.1.8 is required by
# hypr-de: its hypridle.service drop-in starts the daemon with
# `-c /usr/share/hypr-de/hypr/hypridle.conf`, and the -c/--config flag is only
# honoured from 0.1.8 onward. In 0.1.7 the flag is advertised in --help but
# ignored, so startup falls through to the XDG config search and aborts with
# "Could not find config in HOME, XDG_CONFIG_HOME, XDG_CONFIG_DIRS or /etc/hypr"
# (SIGABRT), silently killing idle-locking for the whole session.
#
# %%autorelease/%%autochangelog replaced with static values so this builds
# without the rpmautospec macros.

Name:           hypridle
Version:        0.1.8
Release:        1%{?dist}
Summary:        Hyprland's idle daemon
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hypridle
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros

BuildRequires:  cmake(hyprwayland-scanner)
BuildRequires:  pkgconfig(hyprland-protocols)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install
# Upstream drops a sample policy into %%{_datadir}/hypr; hypr-de owns the real
# one under %%{_datadir}/hypr-de. -f so a layout change upstream is not fatal.
rm -f %{buildroot}%{_datadir}/hypr/hypridle.conf

%files
%license LICENSE
%doc README.md assets/example.conf
%{_bindir}/%{name}
%{_userunitdir}/%{name}.service

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun %{name}.service

%changelog
* Mon Aug 17 2026 Mason Rhodes <mrhodesdev@gmail.com> - 0.1.8-1
- Update to 0.1.8 for working -c/--config, required by hypr-de's drop-in
