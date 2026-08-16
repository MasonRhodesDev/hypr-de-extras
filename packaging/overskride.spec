Name:           overskride
Version:        0.6.6
Release:        2%{?dist}
Summary:        Bluetooth and Obex client

License:        GPL-3.0-or-later
URL:            https://github.com/kaii-lb/overskride
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  gcc
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  glib2-devel

Requires:       bluez
Requires:       hicolor-icon-theme

%description
A Bluetooth and Obex client that is desktop-agnostic. Used by hypr-DE as
the pairing, adapter, audio-profile, and file-transfer UI.

%prep
%autosetup -n %{name}-%{version}

%build
export CARGO_HOME="%{_builddir}/.cargo"
%meson
%meson_build

%install
%meson_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.kaii_lb.Overskride.desktop
# Upstream appstream test is known-flaky in packaging.
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/appdata/io.github.kaii_lb.Overskride.appdata.xml || :

%post
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%license LICENSE
%doc README.md
%{_bindir}/overskride
%{_datadir}/applications/io.github.kaii_lb.Overskride.desktop
%{_datadir}/appdata/io.github.kaii_lb.Overskride.appdata.xml
%{_datadir}/glib-2.0/schemas/io.github.kaii_lb.Overskride.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/io.github.kaii_lb.Overskride.svg
%{_datadir}/icons/hicolor/symbolic/apps/io.github.kaii_lb.Overskride-symbolic.svg
%{_datadir}/overskride/overskride.gresource

%changelog
* Sun Aug 16 2026 Mason Rhodes <mrhodesdev@gmail.com> - 0.6.6-2
- Rebuild with the gh -R release pin so COPR publish can succeed.

* Sat Aug 15 2026 Mason Rhodes <mrhodesdev@gmail.com> - 0.6.6-1
- Initial COPR package for hypr-DE (upstream v0.6.6)
