%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define git 20230909

%define wall_list Altai Autumn BytheWater Canopee Cascade Cluster ColdRipple ColorfulCups DarkestHour Elarun EveningGlow FallenLeaf Flow FlyingKonqui Grey Honeywave IceCold Kay Kite Kokkini MilkyWay OneStandsOut Opal PastelHills Patak Path SafeLanding Shell summer_1am Volna

Name: plasma6-workspace-wallpapers
Version:	5.240.0
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/plasma-workspace-wallpapers/-/archive/master/plasma-workspace-wallpapers-master.tar.bz2#/plasma-workspace-wallpapers-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
%endif
Source1: plasma6-workspace-wallpapers-template.in
Summary: Additional wallpapers for KDE Plasma 6
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: ninja
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildArch: noarch
%{expand:%(\
        for wallpaper in %wall_list; do\
		echo "Suggests: plasma6-wallpaper-$(echo ${wallpaper}|tr A-Z a-z)"
	done\
)}

%description
Additional wallpapers for KDE Plasma 6.

%files
#----------------------------------------------------------------------------

%{expand:%(\
        for wallpaper in %wall_list; do\
                echo "%%{expand:%%(sed -e "s!__LNAME__!${wallpaper,,}!g" -e "s!__NAME__!$wallpaper!g" %{SOURCE1} 2> /dev/null)}";\
        done\
        )
}

%prep
%autosetup -p1 -n plasma-workspace-wallpapers-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
