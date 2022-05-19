#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.04.1
%define		kframever	5.83.0
%define		qtver		5.9.0
%define		kaname		elisa
######		Unknown group!
Summary:	Elisa music player
Name:		ka5-%{kaname}
Version:	22.04.1
Release:	2222222222222222222222oup:		Multimedia
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	2f1549588f09135034a60ccedbaca63f
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel >= 5.15.2
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= 5.15.2
BuildRequires:	Qt5DBus-devel >= 5.15.2
BuildRequires:	Qt5Gui-devel >= 5.15.2
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5Network-devel >= 5.15.2
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-controls2-devel >= 5.15.0
BuildRequires:	Qt5Quick-devel >= 5.15.2
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel >= 5.15.2
BuildRequires:	cmake >= 2.8.12
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-baloo-devel >= 5.85.0
BuildRequires:	kf5-extra-cmake-modules >= 5.85.0
BuildRequires:	kf5-kauth-devel >= 5.92.0
BuildRequires:	kf5-kcodecs-devel >= 5.92.0
BuildRequires:	kf5-kcompletion-devel >= 5.92.0
BuildRequires:	kf5-kconfig-devel >= 5.92.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.92.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.92.0
BuildRequires:	kf5-kcrash-devel >= 5.85.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.85.0
BuildRequires:	kf5-kdeclarative-devel >= 5.85.0
BuildRequires:	kf5-kdoctools-devel >= 5.85.0
BuildRequires:	kf5-kfilemetadata-devel >= 5.85.0
BuildRequires:	kf5-ki18n-devel >= 5.85.0
BuildRequires:	kf5-kiconthemes-devel >= 5.85.0
BuildRequires:	kf5-kio-devel >= 5.85.0
BuildRequires:	kf5-kirigami2-devel >= 5.85.0
BuildRequires:	kf5-kitemviews-devel >= 5.92.0
BuildRequires:	kf5-kjobwidgets-devel >= 5.92.0
BuildRequires:	kf5-kpackage-devel >= 5.85.0
BuildRequires:	kf5-kservice-devel >= 5.92.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.92.0
BuildRequires:	kf5-kxmlgui-devel >= 5.92.0
BuildRequires:	kf5-solid-devel >= 5.92.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-phonon-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	vlc-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elisa is a simple music player aiming to provide a nice experience for
its users. Elisa allows to browse music by album, artist or all
tracks. The music is indexed using either a private indexer or an
indexer using Baloo. The private one can be configured to scan music
on chosen paths. The Baloo one is much faster because Baloo is
providing all needed data from its own database. You can build and
play your own playlist.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/elisa
%dir %{_libdir}/elisa
%ghost %{_libdir}/elisa/libelisaLib.so.0
%{_libdir}/elisa/libelisaLib.so.0.*
%dir %{_libdir}/qt5/qml/org/kde/elisa
%{_libdir}/qt5/qml/org/kde/elisa/libelisaqmlplugin.so
%{_libdir}/qt5/qml/org/kde/elisa/plugins.qmltypes
%{_libdir}/qt5/qml/org/kde/elisa/qmldir
%{_desktopdir}/org.kde.elisa.desktop
%{_iconsdir}/hicolor/128x128/apps/elisa.png
%{_iconsdir}/hicolor/16x16/apps/elisa.png
%{_iconsdir}/hicolor/22x22/apps/elisa.png
%{_iconsdir}/hicolor/32x32/apps/elisa.png
%{_iconsdir}/hicolor/48x48/apps/elisa.png
%{_iconsdir}/hicolor/64x64/apps/elisa.png
%{_iconsdir}/hicolor/scalable/apps/elisa.svg
%{_datadir}/metainfo/org.kde.elisa.appdata.xml
%{_datadir}/qlogging-categories5/elisa.categories
%{_datadir}/dbus-1/services/org.kde.elisa.service
