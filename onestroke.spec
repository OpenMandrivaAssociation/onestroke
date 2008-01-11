%define name	onestroke
%define version	0.8.3
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Gesture recognition for tablet PC's
Version: 	%{version}
Release: 	%{release}

Source:		http://www.missirina.com/risujin/%{name}-%{version}.tar.bz2
URL:		http://www.missirina.com/risujin/onestroke.php
License:	GPL
Group:		Accessibility
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	ImageMagick
BuildRequires:	gtk2-devel
BuildRequires:  libxtst-devel
BuildRequires:  desktop-file-utils

%description
OneStroke is a pen gesture recognition program designed for Unix-based Tablet
PCs. The program serves as a keyboard replacement for tablet mode. When one of
the gestures is drawn on the main window, the configured keyboard event is
sent to the currently focused window.

%prep
%setup -q %name-%version
chmod 644 README *.png *.desktop

%build
%make
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_datadir/applications
mkdir -p %buildroot/%_datadir/pixmaps
make install PREFIX=%buildroot/%_prefix

#menu

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="X-MandrivaLinux-MoreApplications-Accessibility" \
  --dir $RPM_BUILD_ROOT/%_datadir/applications $RPM_BUILD_ROOT/%_datadir/applications/*

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 %name.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 %name.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 %name.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc README
%{_bindir}/%name
%{_datadir}/applications/%name.desktop
%{_datadir}/pixmaps/%name.png
%{_datadir}/%name-0.8
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png


