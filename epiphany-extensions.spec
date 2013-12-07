%define _disable_ld_no_undefined 1
%define url_ver %(echo %{version}|cut -d. -f1,2)
%define api 3.4

Summary:	Extensions for the GNOME Web Browser, Epiphany
Name:		epiphany-extensions
Version:	3.4.0
Release:	3
## The Live HTTP Headers extension is LGPLv2.1+; the Gestures extension is
## GPLv2 (only); and all other extensions are GPLv2+.
License:        LGPLv2+ and GPLv2 and GPLv2+ and GFDL
Group:		Networking/WWW
Url:		http://www.gnome.org/projects/epiphany/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/epiphany-extensions/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	rarian
BuildRequires:	opensp-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(epiphany) >= %{version}
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
Requires:	epiphany >= %{version}

%description
This package contains the following extensions for the GNOME Web Browser:
Actions
Ad blocker
Auto-Reload
Auto-scroller
Certificates
Extension Manager
Gestures
Greasemonkey
HTML5 Tube
Push scroller
RSS
SoupFly
Tab groups
Tab Key Tab Navigate
Tab states

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc COPYING* AUTHORS NEWS README*
%doc extensions/gestures/ephy-gestures.xml
%{_datadir}/%{name}/
%{_datadir}/epiphany/icons/hicolor/*/status/*
%{_datadir}/glib-2.0/schemas/org.gnome.epiphanyextensions.gschema.xml
%{_libdir}/epiphany/%{api}/extensions/*.so
%{_libdir}/epiphany/%{api}/extensions/actions.ephy-extension
%{_libdir}/epiphany/%{api}/extensions/adblock.ephy-extension
%{_libdir}/epiphany/%{api}/extensions/auto-reload.ephy-extension
%{_libdir}/epiphany/%{api}/extensions/extensions-manager-ui.ephy-extension
%{_libdir}/epiphany/%{api}/extensions/gestures.ephy-extension
%{_libdir}/epiphany/%{api}/extensions/greasemonkey.ephy-extension
%{_libdir}/epiphany/%{api}/extensions/html5tube.ephy-extension
%{_libdir}/epiphany/%{api}/extensions/push-scroller.ephy-extension
%{_libdir}/epiphany/%{api}/extensions/rss.ephy-extension
%{_libdir}/epiphany/%{api}/extensions/soup-fly.ephy-extension
%{_libdir}/epiphany/%{api}/extensions/tab-key-tab-navigate.ephy-extension
%{_libdir}/epiphany/%{api}/extensions/tab-states.ephy-extension

