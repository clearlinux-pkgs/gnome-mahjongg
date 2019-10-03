#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-mahjongg
Version  : 3.34.0
Release  : 3
URL      : https://download.gnome.org/sources/gnome-mahjongg/3.34/gnome-mahjongg-3.34.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-mahjongg/3.34/gnome-mahjongg-3.34.0.tar.xz
Summary  : Disassemble a pile of tiles by removing matching pairs
Group    : Development/Tools
License  : CC-BY-SA-3.0 GPL-2.0
Requires: gnome-mahjongg-bin = %{version}-%{release}
Requires: gnome-mahjongg-data = %{version}-%{release}
Requires: gnome-mahjongg-license = %{version}-%{release}
Requires: gnome-mahjongg-locales = %{version}-%{release}
Requires: gnome-mahjongg-man = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : librsvg-dev
BuildRequires : pkgconfig(librsvg-2.0)

%description
The Mahjongg Map Tool makes it easy to generate new layouts for GNOME Mahjongg.
https://github.com/logicplace/mggmap

%package bin
Summary: bin components for the gnome-mahjongg package.
Group: Binaries
Requires: gnome-mahjongg-data = %{version}-%{release}
Requires: gnome-mahjongg-license = %{version}-%{release}

%description bin
bin components for the gnome-mahjongg package.


%package data
Summary: data components for the gnome-mahjongg package.
Group: Data

%description data
data components for the gnome-mahjongg package.


%package doc
Summary: doc components for the gnome-mahjongg package.
Group: Documentation
Requires: gnome-mahjongg-man = %{version}-%{release}

%description doc
doc components for the gnome-mahjongg package.


%package license
Summary: license components for the gnome-mahjongg package.
Group: Default

%description license
license components for the gnome-mahjongg package.


%package locales
Summary: locales components for the gnome-mahjongg package.
Group: Default

%description locales
locales components for the gnome-mahjongg package.


%package man
Summary: man components for the gnome-mahjongg package.
Group: Default

%description man
man components for the gnome-mahjongg package.


%prep
%setup -q -n gnome-mahjongg-3.34.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570113428
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-mahjongg
cp COPYING %{buildroot}/usr/share/package-licenses/gnome-mahjongg/COPYING
cp help/C/license.page %{buildroot}/usr/share/package-licenses/gnome-mahjongg/help_C_license.page
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-mahjongg

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-mahjongg

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Mahjongg.desktop
/usr/share/glib-2.0/schemas/org.gnome.Mahjongg.gschema.xml
/usr/share/gnome-mahjongg/maps/mahjongg.map
/usr/share/gnome-mahjongg/themes/edu_kang_xi.png
/usr/share/gnome-mahjongg/themes/postmodern.svg
/usr/share/gnome-mahjongg/themes/smooth.png
/usr/share/icons/hicolor/scalable/apps/org.gnome.Mahjongg.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Mahjongg-symbolic.svg
/usr/share/metainfo/org.gnome.Mahjongg.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/gnome-mahjongg/bonustiles.page
/usr/share/help/C/gnome-mahjongg/bug-filing.page
/usr/share/help/C/gnome-mahjongg/develop.page
/usr/share/help/C/gnome-mahjongg/documentation.page
/usr/share/help/C/gnome-mahjongg/figures/black-symbol.png
/usr/share/help/C/gnome-mahjongg/figures/hints-video.ogv
/usr/share/help/C/gnome-mahjongg/figures/layout-bridges.png
/usr/share/help/C/gnome-mahjongg/figures/layout-cloud.png
/usr/share/help/C/gnome-mahjongg/figures/layout-conf-cross.png
/usr/share/help/C/gnome-mahjongg/figures/layout-difficult.png
/usr/share/help/C/gnome-mahjongg/figures/layout-easy.png
/usr/share/help/C/gnome-mahjongg/figures/layout-overpass.png
/usr/share/help/C/gnome-mahjongg/figures/layout-pyramid-walls.png
/usr/share/help/C/gnome-mahjongg/figures/layout-red-dragon.png
/usr/share/help/C/gnome-mahjongg/figures/layout-tic-tac-toe.png
/usr/share/help/C/gnome-mahjongg/figures/layout-ziggurat.png
/usr/share/help/C/gnome-mahjongg/figures/logo.png
/usr/share/help/C/gnome-mahjongg/figures/logo32.png
/usr/share/help/C/gnome-mahjongg/figures/mahjongg-video.ogv
/usr/share/help/C/gnome-mahjongg/figures/moves-left.png
/usr/share/help/C/gnome-mahjongg/figures/yellow-symbol.png
/usr/share/help/C/gnome-mahjongg/gameplay.page
/usr/share/help/C/gnome-mahjongg/hints.page
/usr/share/help/C/gnome-mahjongg/index.page
/usr/share/help/C/gnome-mahjongg/legal.xml
/usr/share/help/C/gnome-mahjongg/license.page
/usr/share/help/C/gnome-mahjongg/map.page
/usr/share/help/C/gnome-mahjongg/moves.page
/usr/share/help/C/gnome-mahjongg/pause.page
/usr/share/help/C/gnome-mahjongg/rules.page
/usr/share/help/C/gnome-mahjongg/scoring.page
/usr/share/help/C/gnome-mahjongg/strategy.page
/usr/share/help/C/gnome-mahjongg/translate.page
/usr/share/help/ca/gnome-mahjongg/bonustiles.page
/usr/share/help/ca/gnome-mahjongg/bug-filing.page
/usr/share/help/ca/gnome-mahjongg/develop.page
/usr/share/help/ca/gnome-mahjongg/documentation.page
/usr/share/help/ca/gnome-mahjongg/figures/black-symbol.png
/usr/share/help/ca/gnome-mahjongg/figures/hints-video.ogv
/usr/share/help/ca/gnome-mahjongg/figures/layout-bridges.png
/usr/share/help/ca/gnome-mahjongg/figures/layout-cloud.png
/usr/share/help/ca/gnome-mahjongg/figures/layout-conf-cross.png
/usr/share/help/ca/gnome-mahjongg/figures/layout-difficult.png
/usr/share/help/ca/gnome-mahjongg/figures/layout-easy.png
/usr/share/help/ca/gnome-mahjongg/figures/layout-overpass.png
/usr/share/help/ca/gnome-mahjongg/figures/layout-pyramid-walls.png
/usr/share/help/ca/gnome-mahjongg/figures/layout-red-dragon.png
/usr/share/help/ca/gnome-mahjongg/figures/layout-tic-tac-toe.png
/usr/share/help/ca/gnome-mahjongg/figures/layout-ziggurat.png
/usr/share/help/ca/gnome-mahjongg/figures/logo.png
/usr/share/help/ca/gnome-mahjongg/figures/logo32.png
/usr/share/help/ca/gnome-mahjongg/figures/mahjongg-video.ogv
/usr/share/help/ca/gnome-mahjongg/figures/moves-left.png
/usr/share/help/ca/gnome-mahjongg/figures/yellow-symbol.png
/usr/share/help/ca/gnome-mahjongg/gameplay.page
/usr/share/help/ca/gnome-mahjongg/hints.page
/usr/share/help/ca/gnome-mahjongg/index.page
/usr/share/help/ca/gnome-mahjongg/legal.xml
/usr/share/help/ca/gnome-mahjongg/license.page
/usr/share/help/ca/gnome-mahjongg/map.page
/usr/share/help/ca/gnome-mahjongg/moves.page
/usr/share/help/ca/gnome-mahjongg/pause.page
/usr/share/help/ca/gnome-mahjongg/rules.page
/usr/share/help/ca/gnome-mahjongg/scoring.page
/usr/share/help/ca/gnome-mahjongg/strategy.page
/usr/share/help/ca/gnome-mahjongg/translate.page
/usr/share/help/cs/gnome-mahjongg/bonustiles.page
/usr/share/help/cs/gnome-mahjongg/bug-filing.page
/usr/share/help/cs/gnome-mahjongg/develop.page
/usr/share/help/cs/gnome-mahjongg/documentation.page
/usr/share/help/cs/gnome-mahjongg/figures/black-symbol.png
/usr/share/help/cs/gnome-mahjongg/figures/hints-video.ogv
/usr/share/help/cs/gnome-mahjongg/figures/layout-bridges.png
/usr/share/help/cs/gnome-mahjongg/figures/layout-cloud.png
/usr/share/help/cs/gnome-mahjongg/figures/layout-conf-cross.png
/usr/share/help/cs/gnome-mahjongg/figures/layout-difficult.png
/usr/share/help/cs/gnome-mahjongg/figures/layout-easy.png
/usr/share/help/cs/gnome-mahjongg/figures/layout-overpass.png
/usr/share/help/cs/gnome-mahjongg/figures/layout-pyramid-walls.png
/usr/share/help/cs/gnome-mahjongg/figures/layout-red-dragon.png
/usr/share/help/cs/gnome-mahjongg/figures/layout-tic-tac-toe.png
/usr/share/help/cs/gnome-mahjongg/figures/layout-ziggurat.png
/usr/share/help/cs/gnome-mahjongg/figures/logo.png
/usr/share/help/cs/gnome-mahjongg/figures/logo32.png
/usr/share/help/cs/gnome-mahjongg/figures/mahjongg-video.ogv
/usr/share/help/cs/gnome-mahjongg/figures/moves-left.png
/usr/share/help/cs/gnome-mahjongg/figures/yellow-symbol.png
/usr/share/help/cs/gnome-mahjongg/gameplay.page
/usr/share/help/cs/gnome-mahjongg/hints.page
/usr/share/help/cs/gnome-mahjongg/index.page
/usr/share/help/cs/gnome-mahjongg/legal.xml
/usr/share/help/cs/gnome-mahjongg/license.page
/usr/share/help/cs/gnome-mahjongg/map.page
/usr/share/help/cs/gnome-mahjongg/moves.page
/usr/share/help/cs/gnome-mahjongg/pause.page
/usr/share/help/cs/gnome-mahjongg/rules.page
/usr/share/help/cs/gnome-mahjongg/scoring.page
/usr/share/help/cs/gnome-mahjongg/strategy.page
/usr/share/help/cs/gnome-mahjongg/translate.page
/usr/share/help/de/gnome-mahjongg/bonustiles.page
/usr/share/help/de/gnome-mahjongg/bug-filing.page
/usr/share/help/de/gnome-mahjongg/develop.page
/usr/share/help/de/gnome-mahjongg/documentation.page
/usr/share/help/de/gnome-mahjongg/figures/black-symbol.png
/usr/share/help/de/gnome-mahjongg/figures/hints-video.ogv
/usr/share/help/de/gnome-mahjongg/figures/layout-bridges.png
/usr/share/help/de/gnome-mahjongg/figures/layout-cloud.png
/usr/share/help/de/gnome-mahjongg/figures/layout-conf-cross.png
/usr/share/help/de/gnome-mahjongg/figures/layout-difficult.png
/usr/share/help/de/gnome-mahjongg/figures/layout-easy.png
/usr/share/help/de/gnome-mahjongg/figures/layout-overpass.png
/usr/share/help/de/gnome-mahjongg/figures/layout-pyramid-walls.png
/usr/share/help/de/gnome-mahjongg/figures/layout-red-dragon.png
/usr/share/help/de/gnome-mahjongg/figures/layout-tic-tac-toe.png
/usr/share/help/de/gnome-mahjongg/figures/layout-ziggurat.png
/usr/share/help/de/gnome-mahjongg/figures/logo.png
/usr/share/help/de/gnome-mahjongg/figures/logo32.png
/usr/share/help/de/gnome-mahjongg/figures/mahjongg-video.ogv
/usr/share/help/de/gnome-mahjongg/figures/moves-left.png
/usr/share/help/de/gnome-mahjongg/figures/yellow-symbol.png
/usr/share/help/de/gnome-mahjongg/gameplay.page
/usr/share/help/de/gnome-mahjongg/hints.page
/usr/share/help/de/gnome-mahjongg/index.page
/usr/share/help/de/gnome-mahjongg/legal.xml
/usr/share/help/de/gnome-mahjongg/license.page
/usr/share/help/de/gnome-mahjongg/map.page
/usr/share/help/de/gnome-mahjongg/moves.page
/usr/share/help/de/gnome-mahjongg/pause.page
/usr/share/help/de/gnome-mahjongg/rules.page
/usr/share/help/de/gnome-mahjongg/scoring.page
/usr/share/help/de/gnome-mahjongg/strategy.page
/usr/share/help/de/gnome-mahjongg/translate.page
/usr/share/help/el/gnome-mahjongg/bonustiles.page
/usr/share/help/el/gnome-mahjongg/bug-filing.page
/usr/share/help/el/gnome-mahjongg/develop.page
/usr/share/help/el/gnome-mahjongg/documentation.page
/usr/share/help/el/gnome-mahjongg/figures/black-symbol.png
/usr/share/help/el/gnome-mahjongg/figures/hints-video.ogv
/usr/share/help/el/gnome-mahjongg/figures/layout-bridges.png
/usr/share/help/el/gnome-mahjongg/figures/layout-cloud.png
/usr/share/help/el/gnome-mahjongg/figures/layout-conf-cross.png
/usr/share/help/el/gnome-mahjongg/figures/layout-difficult.png
/usr/share/help/el/gnome-mahjongg/figures/layout-easy.png
/usr/share/help/el/gnome-mahjongg/figures/layout-overpass.png
/usr/share/help/el/gnome-mahjongg/figures/layout-pyramid-walls.png
/usr/share/help/el/gnome-mahjongg/figures/layout-red-dragon.png
/usr/share/help/el/gnome-mahjongg/figures/layout-tic-tac-toe.png
/usr/share/help/el/gnome-mahjongg/figures/layout-ziggurat.png
/usr/share/help/el/gnome-mahjongg/figures/logo.png
/usr/share/help/el/gnome-mahjongg/figures/logo32.png
/usr/share/help/el/gnome-mahjongg/figures/mahjongg-video.ogv
/usr/share/help/el/gnome-mahjongg/figures/moves-left.png
/usr/share/help/el/gnome-mahjongg/figures/yellow-symbol.png
/usr/share/help/el/gnome-mahjongg/gameplay.page
/usr/share/help/el/gnome-mahjongg/hints.page
/usr/share/help/el/gnome-mahjongg/index.page
/usr/share/help/el/gnome-mahjongg/legal.xml
/usr/share/help/el/gnome-mahjongg/license.page
/usr/share/help/el/gnome-mahjongg/map.page
/usr/share/help/el/gnome-mahjongg/moves.page
/usr/share/help/el/gnome-mahjongg/pause.page
/usr/share/help/el/gnome-mahjongg/rules.page
/usr/share/help/el/gnome-mahjongg/scoring.page
/usr/share/help/el/gnome-mahjongg/strategy.page
/usr/share/help/el/gnome-mahjongg/translate.page
/usr/share/help/es/gnome-mahjongg/bonustiles.page
/usr/share/help/es/gnome-mahjongg/bug-filing.page
/usr/share/help/es/gnome-mahjongg/develop.page
/usr/share/help/es/gnome-mahjongg/documentation.page
/usr/share/help/es/gnome-mahjongg/figures/black-symbol.png
/usr/share/help/es/gnome-mahjongg/figures/hints-video.ogv
/usr/share/help/es/gnome-mahjongg/figures/layout-bridges.png
/usr/share/help/es/gnome-mahjongg/figures/layout-cloud.png
/usr/share/help/es/gnome-mahjongg/figures/layout-conf-cross.png
/usr/share/help/es/gnome-mahjongg/figures/layout-difficult.png
/usr/share/help/es/gnome-mahjongg/figures/layout-easy.png
/usr/share/help/es/gnome-mahjongg/figures/layout-overpass.png
/usr/share/help/es/gnome-mahjongg/figures/layout-pyramid-walls.png
/usr/share/help/es/gnome-mahjongg/figures/layout-red-dragon.png
/usr/share/help/es/gnome-mahjongg/figures/layout-tic-tac-toe.png
/usr/share/help/es/gnome-mahjongg/figures/layout-ziggurat.png
/usr/share/help/es/gnome-mahjongg/figures/logo.png
/usr/share/help/es/gnome-mahjongg/figures/logo32.png
/usr/share/help/es/gnome-mahjongg/figures/mahjongg-video.ogv
/usr/share/help/es/gnome-mahjongg/figures/moves-left.png
/usr/share/help/es/gnome-mahjongg/figures/yellow-symbol.png
/usr/share/help/es/gnome-mahjongg/gameplay.page
/usr/share/help/es/gnome-mahjongg/hints.page
/usr/share/help/es/gnome-mahjongg/index.page
/usr/share/help/es/gnome-mahjongg/legal.xml
/usr/share/help/es/gnome-mahjongg/license.page
/usr/share/help/es/gnome-mahjongg/map.page
/usr/share/help/es/gnome-mahjongg/moves.page
/usr/share/help/es/gnome-mahjongg/pause.page
/usr/share/help/es/gnome-mahjongg/rules.page
/usr/share/help/es/gnome-mahjongg/scoring.page
/usr/share/help/es/gnome-mahjongg/strategy.page
/usr/share/help/es/gnome-mahjongg/translate.page
/usr/share/help/fr/gnome-mahjongg/bonustiles.page
/usr/share/help/fr/gnome-mahjongg/bug-filing.page
/usr/share/help/fr/gnome-mahjongg/develop.page
/usr/share/help/fr/gnome-mahjongg/documentation.page
/usr/share/help/fr/gnome-mahjongg/figures/black-symbol.png
/usr/share/help/fr/gnome-mahjongg/figures/hints-video.ogv
/usr/share/help/fr/gnome-mahjongg/figures/layout-bridges.png
/usr/share/help/fr/gnome-mahjongg/figures/layout-cloud.png
/usr/share/help/fr/gnome-mahjongg/figures/layout-conf-cross.png
/usr/share/help/fr/gnome-mahjongg/figures/layout-difficult.png
/usr/share/help/fr/gnome-mahjongg/figures/layout-easy.png
/usr/share/help/fr/gnome-mahjongg/figures/layout-overpass.png
/usr/share/help/fr/gnome-mahjongg/figures/layout-pyramid-walls.png
/usr/share/help/fr/gnome-mahjongg/figures/layout-red-dragon.png
/usr/share/help/fr/gnome-mahjongg/figures/layout-tic-tac-toe.png
/usr/share/help/fr/gnome-mahjongg/figures/layout-ziggurat.png
/usr/share/help/fr/gnome-mahjongg/figures/logo.png
/usr/share/help/fr/gnome-mahjongg/figures/logo32.png
/usr/share/help/fr/gnome-mahjongg/figures/mahjongg-video.ogv
/usr/share/help/fr/gnome-mahjongg/figures/moves-left.png
/usr/share/help/fr/gnome-mahjongg/figures/yellow-symbol.png
/usr/share/help/fr/gnome-mahjongg/gameplay.page
/usr/share/help/fr/gnome-mahjongg/hints.page
/usr/share/help/fr/gnome-mahjongg/index.page
/usr/share/help/fr/gnome-mahjongg/legal.xml
/usr/share/help/fr/gnome-mahjongg/license.page
/usr/share/help/fr/gnome-mahjongg/map.page
/usr/share/help/fr/gnome-mahjongg/moves.page
/usr/share/help/fr/gnome-mahjongg/pause.page
/usr/share/help/fr/gnome-mahjongg/rules.page
/usr/share/help/fr/gnome-mahjongg/scoring.page
/usr/share/help/fr/gnome-mahjongg/strategy.page
/usr/share/help/fr/gnome-mahjongg/translate.page
/usr/share/help/hu/gnome-mahjongg/bonustiles.page
/usr/share/help/hu/gnome-mahjongg/bug-filing.page
/usr/share/help/hu/gnome-mahjongg/develop.page
/usr/share/help/hu/gnome-mahjongg/documentation.page
/usr/share/help/hu/gnome-mahjongg/figures/black-symbol.png
/usr/share/help/hu/gnome-mahjongg/figures/hints-video.ogv
/usr/share/help/hu/gnome-mahjongg/figures/layout-bridges.png
/usr/share/help/hu/gnome-mahjongg/figures/layout-cloud.png
/usr/share/help/hu/gnome-mahjongg/figures/layout-conf-cross.png
/usr/share/help/hu/gnome-mahjongg/figures/layout-difficult.png
/usr/share/help/hu/gnome-mahjongg/figures/layout-easy.png
/usr/share/help/hu/gnome-mahjongg/figures/layout-overpass.png
/usr/share/help/hu/gnome-mahjongg/figures/layout-pyramid-walls.png
/usr/share/help/hu/gnome-mahjongg/figures/layout-red-dragon.png
/usr/share/help/hu/gnome-mahjongg/figures/layout-tic-tac-toe.png
/usr/share/help/hu/gnome-mahjongg/figures/layout-ziggurat.png
/usr/share/help/hu/gnome-mahjongg/figures/logo.png
/usr/share/help/hu/gnome-mahjongg/figures/logo32.png
/usr/share/help/hu/gnome-mahjongg/figures/mahjongg-video.ogv
/usr/share/help/hu/gnome-mahjongg/figures/moves-left.png
/usr/share/help/hu/gnome-mahjongg/figures/yellow-symbol.png
/usr/share/help/hu/gnome-mahjongg/gameplay.page
/usr/share/help/hu/gnome-mahjongg/hints.page
/usr/share/help/hu/gnome-mahjongg/index.page
/usr/share/help/hu/gnome-mahjongg/legal.xml
/usr/share/help/hu/gnome-mahjongg/license.page
/usr/share/help/hu/gnome-mahjongg/map.page
/usr/share/help/hu/gnome-mahjongg/moves.page
/usr/share/help/hu/gnome-mahjongg/pause.page
/usr/share/help/hu/gnome-mahjongg/rules.page
/usr/share/help/hu/gnome-mahjongg/scoring.page
/usr/share/help/hu/gnome-mahjongg/strategy.page
/usr/share/help/hu/gnome-mahjongg/translate.page
/usr/share/help/ko/gnome-mahjongg/bonustiles.page
/usr/share/help/ko/gnome-mahjongg/bug-filing.page
/usr/share/help/ko/gnome-mahjongg/develop.page
/usr/share/help/ko/gnome-mahjongg/documentation.page
/usr/share/help/ko/gnome-mahjongg/figures/black-symbol.png
/usr/share/help/ko/gnome-mahjongg/figures/hints-video.ogv
/usr/share/help/ko/gnome-mahjongg/figures/layout-bridges.png
/usr/share/help/ko/gnome-mahjongg/figures/layout-cloud.png
/usr/share/help/ko/gnome-mahjongg/figures/layout-conf-cross.png
/usr/share/help/ko/gnome-mahjongg/figures/layout-difficult.png
/usr/share/help/ko/gnome-mahjongg/figures/layout-easy.png
/usr/share/help/ko/gnome-mahjongg/figures/layout-overpass.png
/usr/share/help/ko/gnome-mahjongg/figures/layout-pyramid-walls.png
/usr/share/help/ko/gnome-mahjongg/figures/layout-red-dragon.png
/usr/share/help/ko/gnome-mahjongg/figures/layout-tic-tac-toe.png
/usr/share/help/ko/gnome-mahjongg/figures/layout-ziggurat.png
/usr/share/help/ko/gnome-mahjongg/figures/logo.png
/usr/share/help/ko/gnome-mahjongg/figures/logo32.png
/usr/share/help/ko/gnome-mahjongg/figures/mahjongg-video.ogv
/usr/share/help/ko/gnome-mahjongg/figures/moves-left.png
/usr/share/help/ko/gnome-mahjongg/figures/yellow-symbol.png
/usr/share/help/ko/gnome-mahjongg/gameplay.page
/usr/share/help/ko/gnome-mahjongg/hints.page
/usr/share/help/ko/gnome-mahjongg/index.page
/usr/share/help/ko/gnome-mahjongg/legal.xml
/usr/share/help/ko/gnome-mahjongg/license.page
/usr/share/help/ko/gnome-mahjongg/map.page
/usr/share/help/ko/gnome-mahjongg/moves.page
/usr/share/help/ko/gnome-mahjongg/pause.page
/usr/share/help/ko/gnome-mahjongg/rules.page
/usr/share/help/ko/gnome-mahjongg/scoring.page
/usr/share/help/ko/gnome-mahjongg/strategy.page
/usr/share/help/ko/gnome-mahjongg/translate.page
/usr/share/help/pl/gnome-mahjongg/bonustiles.page
/usr/share/help/pl/gnome-mahjongg/bug-filing.page
/usr/share/help/pl/gnome-mahjongg/develop.page
/usr/share/help/pl/gnome-mahjongg/documentation.page
/usr/share/help/pl/gnome-mahjongg/figures/black-symbol.png
/usr/share/help/pl/gnome-mahjongg/figures/hints-video.ogv
/usr/share/help/pl/gnome-mahjongg/figures/layout-bridges.png
/usr/share/help/pl/gnome-mahjongg/figures/layout-cloud.png
/usr/share/help/pl/gnome-mahjongg/figures/layout-conf-cross.png
/usr/share/help/pl/gnome-mahjongg/figures/layout-difficult.png
/usr/share/help/pl/gnome-mahjongg/figures/layout-easy.png
/usr/share/help/pl/gnome-mahjongg/figures/layout-overpass.png
/usr/share/help/pl/gnome-mahjongg/figures/layout-pyramid-walls.png
/usr/share/help/pl/gnome-mahjongg/figures/layout-red-dragon.png
/usr/share/help/pl/gnome-mahjongg/figures/layout-tic-tac-toe.png
/usr/share/help/pl/gnome-mahjongg/figures/layout-ziggurat.png
/usr/share/help/pl/gnome-mahjongg/figures/logo.png
/usr/share/help/pl/gnome-mahjongg/figures/logo32.png
/usr/share/help/pl/gnome-mahjongg/figures/mahjongg-video.ogv
/usr/share/help/pl/gnome-mahjongg/figures/moves-left.png
/usr/share/help/pl/gnome-mahjongg/figures/yellow-symbol.png
/usr/share/help/pl/gnome-mahjongg/gameplay.page
/usr/share/help/pl/gnome-mahjongg/hints.page
/usr/share/help/pl/gnome-mahjongg/index.page
/usr/share/help/pl/gnome-mahjongg/legal.xml
/usr/share/help/pl/gnome-mahjongg/license.page
/usr/share/help/pl/gnome-mahjongg/map.page
/usr/share/help/pl/gnome-mahjongg/moves.page
/usr/share/help/pl/gnome-mahjongg/pause.page
/usr/share/help/pl/gnome-mahjongg/rules.page
/usr/share/help/pl/gnome-mahjongg/scoring.page
/usr/share/help/pl/gnome-mahjongg/strategy.page
/usr/share/help/pl/gnome-mahjongg/translate.page
/usr/share/help/ro/gnome-mahjongg/bonustiles.page
/usr/share/help/ro/gnome-mahjongg/bug-filing.page
/usr/share/help/ro/gnome-mahjongg/develop.page
/usr/share/help/ro/gnome-mahjongg/documentation.page
/usr/share/help/ro/gnome-mahjongg/figures/black-symbol.png
/usr/share/help/ro/gnome-mahjongg/figures/hints-video.ogv
/usr/share/help/ro/gnome-mahjongg/figures/layout-bridges.png
/usr/share/help/ro/gnome-mahjongg/figures/layout-cloud.png
/usr/share/help/ro/gnome-mahjongg/figures/layout-conf-cross.png
/usr/share/help/ro/gnome-mahjongg/figures/layout-difficult.png
/usr/share/help/ro/gnome-mahjongg/figures/layout-easy.png
/usr/share/help/ro/gnome-mahjongg/figures/layout-overpass.png
/usr/share/help/ro/gnome-mahjongg/figures/layout-pyramid-walls.png
/usr/share/help/ro/gnome-mahjongg/figures/layout-red-dragon.png
/usr/share/help/ro/gnome-mahjongg/figures/layout-tic-tac-toe.png
/usr/share/help/ro/gnome-mahjongg/figures/layout-ziggurat.png
/usr/share/help/ro/gnome-mahjongg/figures/logo.png
/usr/share/help/ro/gnome-mahjongg/figures/logo32.png
/usr/share/help/ro/gnome-mahjongg/figures/mahjongg-video.ogv
/usr/share/help/ro/gnome-mahjongg/figures/moves-left.png
/usr/share/help/ro/gnome-mahjongg/figures/yellow-symbol.png
/usr/share/help/ro/gnome-mahjongg/gameplay.page
/usr/share/help/ro/gnome-mahjongg/hints.page
/usr/share/help/ro/gnome-mahjongg/index.page
/usr/share/help/ro/gnome-mahjongg/legal.xml
/usr/share/help/ro/gnome-mahjongg/license.page
/usr/share/help/ro/gnome-mahjongg/map.page
/usr/share/help/ro/gnome-mahjongg/moves.page
/usr/share/help/ro/gnome-mahjongg/pause.page
/usr/share/help/ro/gnome-mahjongg/rules.page
/usr/share/help/ro/gnome-mahjongg/scoring.page
/usr/share/help/ro/gnome-mahjongg/strategy.page
/usr/share/help/ro/gnome-mahjongg/translate.page
/usr/share/help/sv/gnome-mahjongg/bonustiles.page
/usr/share/help/sv/gnome-mahjongg/bug-filing.page
/usr/share/help/sv/gnome-mahjongg/develop.page
/usr/share/help/sv/gnome-mahjongg/documentation.page
/usr/share/help/sv/gnome-mahjongg/figures/black-symbol.png
/usr/share/help/sv/gnome-mahjongg/figures/hints-video.ogv
/usr/share/help/sv/gnome-mahjongg/figures/layout-bridges.png
/usr/share/help/sv/gnome-mahjongg/figures/layout-cloud.png
/usr/share/help/sv/gnome-mahjongg/figures/layout-conf-cross.png
/usr/share/help/sv/gnome-mahjongg/figures/layout-difficult.png
/usr/share/help/sv/gnome-mahjongg/figures/layout-easy.png
/usr/share/help/sv/gnome-mahjongg/figures/layout-overpass.png
/usr/share/help/sv/gnome-mahjongg/figures/layout-pyramid-walls.png
/usr/share/help/sv/gnome-mahjongg/figures/layout-red-dragon.png
/usr/share/help/sv/gnome-mahjongg/figures/layout-tic-tac-toe.png
/usr/share/help/sv/gnome-mahjongg/figures/layout-ziggurat.png
/usr/share/help/sv/gnome-mahjongg/figures/logo.png
/usr/share/help/sv/gnome-mahjongg/figures/logo32.png
/usr/share/help/sv/gnome-mahjongg/figures/mahjongg-video.ogv
/usr/share/help/sv/gnome-mahjongg/figures/moves-left.png
/usr/share/help/sv/gnome-mahjongg/figures/yellow-symbol.png
/usr/share/help/sv/gnome-mahjongg/gameplay.page
/usr/share/help/sv/gnome-mahjongg/hints.page
/usr/share/help/sv/gnome-mahjongg/index.page
/usr/share/help/sv/gnome-mahjongg/legal.xml
/usr/share/help/sv/gnome-mahjongg/license.page
/usr/share/help/sv/gnome-mahjongg/map.page
/usr/share/help/sv/gnome-mahjongg/moves.page
/usr/share/help/sv/gnome-mahjongg/pause.page
/usr/share/help/sv/gnome-mahjongg/rules.page
/usr/share/help/sv/gnome-mahjongg/scoring.page
/usr/share/help/sv/gnome-mahjongg/strategy.page
/usr/share/help/sv/gnome-mahjongg/translate.page

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-mahjongg/COPYING
/usr/share/package-licenses/gnome-mahjongg/help_C_license.page

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man6/gnome-mahjongg.6

%files locales -f gnome-mahjongg.lang
%defattr(-,root,root,-)

