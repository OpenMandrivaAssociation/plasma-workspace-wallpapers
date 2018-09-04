%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define debug_package %{nil}

%define wall_list Autumn BytheWater ColdRipple ColorfulCups DarkestHour EveningGlow FallenLeaf FlyingKonqui Grey Kite OneStandsOut PastelHills Path

Name: plasma-workspace-wallpapers
Version: 5.13.5
Release: 1
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
Suggests: plasma-wallpaper-alps
Suggests: plasma-wallpaper-blueflower
Suggests: plasma-wallpaper-danceofthespirits
Suggests: plasma-wallpaper-fog
Suggests: plasma-wallpaper-forestfog
Suggests: plasma-wallpaper-foresthouse
Suggests: plasma-wallpaper-gereatheron
Suggests: plasma-wallpaper-greenleaves
Suggests: plasma-wallpaper-grey
Suggests: plasma-wallpaper-indiansummer
Suggests: plasma-wallpaper-landmannalaugar
Suggests: plasma-wallpaper-poppy
Suggests: plasma-wallpaper-spray
Suggests: plasma-wallpaper-sunset
Suggests: plasma-wallpaper-tauplitz
Suggests: plasma-wallpaper-walmendingerhorn
Suggests: plasma-wallpaper-water
Suggests: plasma-wallpaper-whiskergrass
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
%setup -qn %{name}-%{plasmaver}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
