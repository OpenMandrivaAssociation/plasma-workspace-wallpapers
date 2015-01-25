%define major 5
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define debug_package %{nil}

Name: plasma-workspace-wallpapers
Version: 5.1.95
Release: 1
Source0: ftp://ftp.kde.org/pub/kde/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: Additional wallpapers for KDE Plasma 5
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: ninja
BuildArch: noarch

%description
Additional wallpapers for KDE Plasma 5

%prep
%setup -qn %{name}-%{plasmaver}
%apply_patches

%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files
%{_datadir}/wallpapers/Dance_of_the_Spirits
%{_datadir}/wallpapers/Green_Leaves
%{_datadir}/wallpapers/Whisker_Grass
