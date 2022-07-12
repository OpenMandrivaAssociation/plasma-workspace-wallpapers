%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

%define wall_list Altai Autumn BytheWater Canopee Cascade Cluster ColdRipple ColorfulCups DarkestHour Elarun EveningGlow FallenLeaf Flow FlyingKonqui Grey Honeywave IceCold Kite Kokkini MilkyWay OneStandsOut Opal PastelHills Patak Path Shell summer_1am Volna

Name: plasma-workspace-wallpapers
Version:	5.25.3
Release:	1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Source1: %{name}-template.in
Summary: Additional wallpapers for KDE Plasma 5
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: qmake5
BuildRequires: ninja
BuildRequires: cmake(Qt5Core)
BuildArch: noarch
%{expand:%(\
        for wallpaper in %wall_list; do\
		echo "Suggests: plasma-wallpaper-$(echo ${wallpaper}|tr A-Z a-z)"
	done\
)}
Obsoletes: kde-wallpapers < 2:15.08.3-3
Provides: kde-wallpapers = 2:15.08.3-3
Obsoletes: kdeartwork-wallpapers < 1:15.08.3-3
Obsoletes: kdeartwork4-wallpapers < 1:4.14.3-2
Provides: kdeartwork-wallpapers = 1:15.08.3-3
Provides: kdeartwork4-wallpapers = 1:4.14.3-2

%description
Additional wallpapers for KDE Plasma 5.

%files
#----------------------------------------------------------------------------


%{expand:%(\
        for wallpaper in %wall_list; do\
                echo "%%{expand:%%(sed -e "s!__LNAME__!${wallpaper,,}!g" -e "s!__NAME__!$wallpaper!g" %{SOURCE1} 2> /dev/null)}";\
        done\
        )
}

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
