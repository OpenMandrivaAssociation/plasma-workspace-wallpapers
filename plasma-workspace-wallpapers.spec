%define major 5
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define debug_package %{nil}

Name: plasma-workspace-wallpapers
Version: 5.3.0
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: Additional wallpapers for KDE Plasma 5
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
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

%description
Additional wallpapers for KDE Plasma 5.

%files
#----------------------------------------------------------------------------

%package -n plasma-wallpaper-alps
Summary:	Plasma 5 Alps wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-alps
Plasma 5 Alps wallpaper.

%files -n plasma-wallpaper-alps
%dir %{_datadir}/wallpapers/Alps/
%{_datadir}/wallpapers/Alps/*

#----------------------------------------------------------------------------

%package -n plasma-wallpaper-blueflower
Summary:	Plasma 5 Blue Flower wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-blueflower
Plasma 5 Blue Flower wallpaper.

%files -n plasma-wallpaper-blueflower
%dir %{_datadir}/wallpapers/BlueFlower/
%{_datadir}/wallpapers/BlueFlower/*

#----------------------------------------------------------------------------

%package -n plasma-wallpaper-danceofthespirits
Summary:	Plasma 5 Dance of the Spirits wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-danceofthespirits
Plasma 5 Dance of the Spirits wallpaper.

%files -n plasma-wallpaper-danceofthespirits
%dir %{_datadir}/wallpapers/Dance_of_the_Spirits/
%{_datadir}/wallpapers/Dance_of_the_Spirits/*

#----------------------------------------------------------------------------

%package -n plasma-wallpaper-fog
Summary:	Plasma 5 Fog wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-fog
Plasma 5 Fog wallpaper.

%files -n plasma-wallpaper-fog
%dir %{_datadir}/wallpapers/Fog/
%{_datadir}/wallpapers/Fog/*

#----------------------------------------------------------------------------

%package -n plasma-wallpaper-forestfog
Summary:	Plasma 5 Forest Fog wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-forestfog
Plasma 5 Forest Fog wallpaper.

%files -n plasma-wallpaper-forestfog
%dir %{_datadir}/wallpapers/ForestFog/
%{_datadir}/wallpapers/ForestFog/*

#----------------------------------------------------------------------------

%package -n plasma-wallpaper-foresthouse
Summary:	Plasma 5 Forest House wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-foresthouse
Plasma 5 Forest House wallpaper.

%files -n plasma-wallpaper-foresthouse
%dir %{_datadir}/wallpapers/ForestHouse/
%{_datadir}/wallpapers/ForestHouse/*

#----------------------------------------------------------------------------

%package -n plasma-wallpaper-gereatheron
Summary:	Plasma 5 Gereat Heron wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-gereatheron
Plasma 5 Gereat Heron wallpaper.

%files -n plasma-wallpaper-gereatheron
%dir %{_datadir}/wallpapers/GereatHeron/
%{_datadir}/wallpapers/GereatHeron/*

#----------------------------------------------------------------------------

%package -n plasma-wallpaper-greenleaves
Summary:	Plasma 5 Green Leaves wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-greenleaves
Plasma 5 Green Leaves wallpaper.

%files -n plasma-wallpaper-greenleaves
%dir %{_datadir}/wallpapers/Green_Leaves/
%{_datadir}/wallpapers/Green_Leaves/*

#----------------------------------------------------------------------------

%package -n plasma-wallpaper-grey
Summary:	Plasma 5 Grey wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-grey
Plasma 5 Grey wallpaper.

%files -n plasma-wallpaper-grey
%dir %{_datadir}/wallpapers/Grey/
%{_datadir}/wallpapers/Grey/*

#----------------------------------------------------------------------------

%package -n plasma-wallpaper-indiansummer
Summary:	Plasma 5 Indian Summer wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-indiansummer
Plasma 5 Indian Summer wallpaper.

%files -n plasma-wallpaper-indiansummer
%dir %{_datadir}/wallpapers/IndianSummer/
%{_datadir}/wallpapers/IndianSummer/*

#----------------------------------------------------------------------------

%package -n plasma-wallpaper-landmannalaugar
Summary:	Plasma 5 Landmannalaugar wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-landmannalaugar
Plasma 5 Landmannalaugar wallpaper.

%files -n plasma-wallpaper-landmannalaugar
%dir %{_datadir}/wallpapers/Landmannalaugar/
%{_datadir}/wallpapers/Landmannalaugar/*

#----------------------------------------------------------------------------

%package -n plasma-wallpaper-poppy
Summary:	Plasma 5 Poppy wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-poppy
Plasma 5 Poppy wallpaper.

%files -n plasma-wallpaper-poppy
%dir %{_datadir}/wallpapers/Poppy/
%{_datadir}/wallpapers/Poppy/*

#----------------------------------------------------------------------------

%package -n plasma-wallpaper-spray
Summary:	Plasma 5 Spray wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-spray
Plasma 5 Spray wallpaper.

%files -n plasma-wallpaper-spray
%dir %{_datadir}/wallpapers/Spray/
%{_datadir}/wallpapers/Spray/*

#----------------------------------------------------------------------------

%package -n plasma-wallpaper-sunset
Summary:	Plasma 5 Sunset wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-sunset
Plasma 5 Sunset wallpaper.

%files -n plasma-wallpaper-sunset
%dir %{_datadir}/wallpapers/Sunset/
%{_datadir}/wallpapers/Sunset/*

#----------------------------------------------------------------------------

%package -n plasma-wallpaper-tauplitz
Summary:	Plasma 5 Tauplitz wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-tauplitz
Plasma 5 Tauplitz wallpaper.

%files -n plasma-wallpaper-tauplitz
%dir %{_datadir}/wallpapers/Tauplitz/
%{_datadir}/wallpapers/Tauplitz/*

#----------------------------------------------------------------------------

%package -n plasma-wallpaper-walmendingerhorn
Summary:	Plasma 5 Walmendinger Horn wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-walmendingerhorn
Plasma 5 Walmendinger Horn wallpaper.

%files -n plasma-wallpaper-walmendingerhorn
%dir %{_datadir}/wallpapers/WalmendingerHorn/
%{_datadir}/wallpapers/WalmendingerHorn/*

#----------------------------------------------------------------------------

%package -n plasma-wallpaper-water
Summary:	Plasma 5 Water wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-water
Plasma 5 Water wallpaper.

%files -n plasma-wallpaper-water
%dir %{_datadir}/wallpapers/Water/
%{_datadir}/wallpapers/Water/*

#----------------------------------------------------------------------------

%package -n plasma-wallpaper-whiskergrass
Summary:	Plasma 5 Whisker Grass wallpaper
Group:		Graphical desktop/KDE

%description -n plasma-wallpaper-whiskergrass
Plasma 5 Whisker Grass wallpaper.

%files -n plasma-wallpaper-whiskergrass
%dir %{_datadir}/wallpapers/Whisker_Grass/
%{_datadir}/wallpapers/Whisker_Grass/*

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{plasmaver}
%apply_patches

%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
