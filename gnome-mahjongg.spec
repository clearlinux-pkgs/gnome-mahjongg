#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-mahjongg
Version  : 3.38.3
Release  : 11
URL      : https://download.gnome.org/sources/gnome-mahjongg/3.38/gnome-mahjongg-3.38.3.tar.xz
Source0  : https://download.gnome.org/sources/gnome-mahjongg/3.38/gnome-mahjongg-3.38.3.tar.xz
Summary  : No detailed summary available
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
# GNOME Mahjongg
Mahjongg is a solitaire (one player) version of the classic Eastern tile
game, Mahjongg. The objective is to select pairs of similar tiles.

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
%setup -q -n gnome-mahjongg-3.38.3
cd %{_builddir}/gnome-mahjongg-3.38.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604441111
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dcompile-schemas=disabled \
-Dupdate-icon-cache=disabled  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-mahjongg
cp %{_builddir}/gnome-mahjongg-3.38.3/COPYING %{buildroot}/usr/share/package-licenses/gnome-mahjongg/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/gnome-mahjongg-3.38.3/help/C/license.page %{buildroot}/usr/share/package-licenses/gnome-mahjongg/99449fd3e6417f1f32dbe2a5b252880badb25704
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
/usr/share/help/C/gnome-mahjongg/figures/keyboard-key-pause.svg
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
/usr/share/help/ca/gnome-mahjongg/figures/keyboard-key-pause.svg
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
/usr/share/help/cs/gnome-mahjongg/figures/keyboard-key-pause.svg
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
/usr/share/help/da/gnome-mahjongg/bonustiles.page
/usr/share/help/da/gnome-mahjongg/bug-filing.page
/usr/share/help/da/gnome-mahjongg/develop.page
/usr/share/help/da/gnome-mahjongg/documentation.page
/usr/share/help/da/gnome-mahjongg/figures/black-symbol.png
/usr/share/help/da/gnome-mahjongg/figures/hints-video.ogv
/usr/share/help/da/gnome-mahjongg/figures/keyboard-key-pause.svg
/usr/share/help/da/gnome-mahjongg/figures/layout-bridges.png
/usr/share/help/da/gnome-mahjongg/figures/layout-cloud.png
/usr/share/help/da/gnome-mahjongg/figures/layout-conf-cross.png
/usr/share/help/da/gnome-mahjongg/figures/layout-difficult.png
/usr/share/help/da/gnome-mahjongg/figures/layout-easy.png
/usr/share/help/da/gnome-mahjongg/figures/layout-overpass.png
/usr/share/help/da/gnome-mahjongg/figures/layout-pyramid-walls.png
/usr/share/help/da/gnome-mahjongg/figures/layout-red-dragon.png
/usr/share/help/da/gnome-mahjongg/figures/layout-tic-tac-toe.png
/usr/share/help/da/gnome-mahjongg/figures/layout-ziggurat.png
/usr/share/help/da/gnome-mahjongg/figures/logo.png
/usr/share/help/da/gnome-mahjongg/figures/logo32.png
/usr/share/help/da/gnome-mahjongg/figures/mahjongg-video.ogv
/usr/share/help/da/gnome-mahjongg/figures/yellow-symbol.png
/usr/share/help/da/gnome-mahjongg/gameplay.page
/usr/share/help/da/gnome-mahjongg/hints.page
/usr/share/help/da/gnome-mahjongg/index.page
/usr/share/help/da/gnome-mahjongg/legal.xml
/usr/share/help/da/gnome-mahjongg/license.page
/usr/share/help/da/gnome-mahjongg/map.page
/usr/share/help/da/gnome-mahjongg/moves.page
/usr/share/help/da/gnome-mahjongg/pause.page
/usr/share/help/da/gnome-mahjongg/rules.page
/usr/share/help/da/gnome-mahjongg/scoring.page
/usr/share/help/da/gnome-mahjongg/strategy.page
/usr/share/help/da/gnome-mahjongg/translate.page
/usr/share/help/de/gnome-mahjongg/bonustiles.page
/usr/share/help/de/gnome-mahjongg/bug-filing.page
/usr/share/help/de/gnome-mahjongg/develop.page
/usr/share/help/de/gnome-mahjongg/documentation.page
/usr/share/help/de/gnome-mahjongg/figures/black-symbol.png
/usr/share/help/de/gnome-mahjongg/figures/hints-video.ogv
/usr/share/help/de/gnome-mahjongg/figures/keyboard-key-pause.svg
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
/usr/share/help/el/gnome-mahjongg/figures/keyboard-key-pause.svg
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
/usr/share/help/es/gnome-mahjongg/figures/keyboard-key-pause.svg
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
/usr/share/help/fr/gnome-mahjongg/figures/keyboard-key-pause.svg
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
/usr/share/help/hu/gnome-mahjongg/figures/keyboard-key-pause.svg
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
/usr/share/help/id/gnome-mahjongg/bonustiles.page
/usr/share/help/id/gnome-mahjongg/bug-filing.page
/usr/share/help/id/gnome-mahjongg/develop.page
/usr/share/help/id/gnome-mahjongg/documentation.page
/usr/share/help/id/gnome-mahjongg/figures/black-symbol.png
/usr/share/help/id/gnome-mahjongg/figures/hints-video.ogv
/usr/share/help/id/gnome-mahjongg/figures/keyboard-key-pause.svg
/usr/share/help/id/gnome-mahjongg/figures/layout-bridges.png
/usr/share/help/id/gnome-mahjongg/figures/layout-cloud.png
/usr/share/help/id/gnome-mahjongg/figures/layout-conf-cross.png
/usr/share/help/id/gnome-mahjongg/figures/layout-difficult.png
/usr/share/help/id/gnome-mahjongg/figures/layout-easy.png
/usr/share/help/id/gnome-mahjongg/figures/layout-overpass.png
/usr/share/help/id/gnome-mahjongg/figures/layout-pyramid-walls.png
/usr/share/help/id/gnome-mahjongg/figures/layout-red-dragon.png
/usr/share/help/id/gnome-mahjongg/figures/layout-tic-tac-toe.png
/usr/share/help/id/gnome-mahjongg/figures/layout-ziggurat.png
/usr/share/help/id/gnome-mahjongg/figures/logo.png
/usr/share/help/id/gnome-mahjongg/figures/logo32.png
/usr/share/help/id/gnome-mahjongg/figures/mahjongg-video.ogv
/usr/share/help/id/gnome-mahjongg/figures/yellow-symbol.png
/usr/share/help/id/gnome-mahjongg/gameplay.page
/usr/share/help/id/gnome-mahjongg/hints.page
/usr/share/help/id/gnome-mahjongg/index.page
/usr/share/help/id/gnome-mahjongg/legal.xml
/usr/share/help/id/gnome-mahjongg/license.page
/usr/share/help/id/gnome-mahjongg/map.page
/usr/share/help/id/gnome-mahjongg/moves.page
/usr/share/help/id/gnome-mahjongg/pause.page
/usr/share/help/id/gnome-mahjongg/rules.page
/usr/share/help/id/gnome-mahjongg/scoring.page
/usr/share/help/id/gnome-mahjongg/strategy.page
/usr/share/help/id/gnome-mahjongg/translate.page
/usr/share/help/ko/gnome-mahjongg/bonustiles.page
/usr/share/help/ko/gnome-mahjongg/bug-filing.page
/usr/share/help/ko/gnome-mahjongg/develop.page
/usr/share/help/ko/gnome-mahjongg/documentation.page
/usr/share/help/ko/gnome-mahjongg/figures/black-symbol.png
/usr/share/help/ko/gnome-mahjongg/figures/hints-video.ogv
/usr/share/help/ko/gnome-mahjongg/figures/keyboard-key-pause.svg
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
/usr/share/help/pl/gnome-mahjongg/figures/keyboard-key-pause.svg
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
/usr/share/help/ro/gnome-mahjongg/figures/keyboard-key-pause.svg
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
/usr/share/help/sv/gnome-mahjongg/figures/keyboard-key-pause.svg
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
/usr/share/help/uk/gnome-mahjongg/bonustiles.page
/usr/share/help/uk/gnome-mahjongg/bug-filing.page
/usr/share/help/uk/gnome-mahjongg/develop.page
/usr/share/help/uk/gnome-mahjongg/documentation.page
/usr/share/help/uk/gnome-mahjongg/figures/black-symbol.png
/usr/share/help/uk/gnome-mahjongg/figures/hints-video.ogv
/usr/share/help/uk/gnome-mahjongg/figures/keyboard-key-pause.svg
/usr/share/help/uk/gnome-mahjongg/figures/layout-bridges.png
/usr/share/help/uk/gnome-mahjongg/figures/layout-cloud.png
/usr/share/help/uk/gnome-mahjongg/figures/layout-conf-cross.png
/usr/share/help/uk/gnome-mahjongg/figures/layout-difficult.png
/usr/share/help/uk/gnome-mahjongg/figures/layout-easy.png
/usr/share/help/uk/gnome-mahjongg/figures/layout-overpass.png
/usr/share/help/uk/gnome-mahjongg/figures/layout-pyramid-walls.png
/usr/share/help/uk/gnome-mahjongg/figures/layout-red-dragon.png
/usr/share/help/uk/gnome-mahjongg/figures/layout-tic-tac-toe.png
/usr/share/help/uk/gnome-mahjongg/figures/layout-ziggurat.png
/usr/share/help/uk/gnome-mahjongg/figures/logo.png
/usr/share/help/uk/gnome-mahjongg/figures/logo32.png
/usr/share/help/uk/gnome-mahjongg/figures/mahjongg-video.ogv
/usr/share/help/uk/gnome-mahjongg/figures/yellow-symbol.png
/usr/share/help/uk/gnome-mahjongg/gameplay.page
/usr/share/help/uk/gnome-mahjongg/hints.page
/usr/share/help/uk/gnome-mahjongg/index.page
/usr/share/help/uk/gnome-mahjongg/legal.xml
/usr/share/help/uk/gnome-mahjongg/license.page
/usr/share/help/uk/gnome-mahjongg/map.page
/usr/share/help/uk/gnome-mahjongg/moves.page
/usr/share/help/uk/gnome-mahjongg/pause.page
/usr/share/help/uk/gnome-mahjongg/rules.page
/usr/share/help/uk/gnome-mahjongg/scoring.page
/usr/share/help/uk/gnome-mahjongg/strategy.page
/usr/share/help/uk/gnome-mahjongg/translate.page

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-mahjongg/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/gnome-mahjongg/99449fd3e6417f1f32dbe2a5b252880badb25704

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man6/gnome-mahjongg.6

%files locales -f gnome-mahjongg.lang
%defattr(-,root,root,-)

