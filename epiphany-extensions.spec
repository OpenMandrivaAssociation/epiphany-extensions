%define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

%define epiver 2.29.0
%define api_version 2.29
%define dir_version 2.29
%define git 0
%if %git
%define release %mkrel -c %git 1
%else
%define release %mkrel 1
%endif

Summary: Extensions for the GNOME Web Browser, Epiphany
Name: epiphany-extensions
Version: 2.29.6
Release: %release
%if %git
Source0:       %{name}-%{git}.tar.xz
%else
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
%endif
## The Live HTTP Headers extension is LGPLv2.1+; the Gestures extension is
## GPLv2 (only); and all other extensions are GPLv2+.
License:        LGPLv2+ and GPLv2 and GPLv2+ and GFDL
Group: Networking/WWW
Url: http://www.gnome.org/projects/epiphany/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: epiphany-devel >= %epiver
BuildRequires: OpenSP-devel
BuildRequires: dbus-devel >= 0.50
BuildRequires: automake1.9
BuildRequires: gnome-common
BuildRequires: intltool
BuildRequires: scrollkeeper
BuildRequires: gnome-doc-utils
Requires: epiphany >= %epiver
Requires(post): scrollkeeper
Requires(postun): scrollkeeper


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
Tab states

%prep
%if %git
%setup -q -n %name
./autogen.sh -V
%else
%setup -q
%endif

cp extensions/error-viewer/README README.error-viewer

%build
#gw not enabled extensions:
#net-monitor 
%configure2_5x 
#--with-extensions=actions,adblock,auto-reload,auto-scroller,certificates,cc-license-viewer,epilicious,error-viewer,extensions-manager-ui,favicon,gestures,greasemonkey,java-console,livehttpheaders,page-info,permissions,push-scroller,python-console,rss,select-stylesheet,sidebar,tab-groups,tab-states

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name-%api_version
%find_lang %name --with-gnome
for omf in %buildroot%_datadir/omf/*/*[_-]??.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done

cat %name.lang >> %name-%api_version.lang


#remove unpackaged files
rm -rf $RPM_BUILD_ROOT%{_libdir}/epiphany/%{dir_version}/extensions/*.la \
      %buildroot/var/lib/scrollkeeper

%postun
%clean_scrollkeeper


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name-%api_version.lang
%defattr(-,root,root)
%doc COPYING* AUTHORS NEWS README*
#%doc ChangeLog
%doc extensions/gestures/ephy-gestures.xml
#%_sysconfdir/gconf/schemas/epilicious.schemas
%_datadir/%name/
%_datadir/epiphany/icons/hicolor/*/status/*
%dir %_datadir/omf/%name
%_datadir/omf/%name/%name-C.omf
%_libdir/epiphany/%{dir_version}/extensions/*.so
%_libdir/epiphany/%{dir_version}/extensions/actions.ephy-extension
%_libdir/epiphany/%{dir_version}/extensions/adblock.ephy-extension
%_libdir/epiphany/%{dir_version}/extensions/auto-reload.ephy-extension
%_libdir/epiphany/%{dir_version}/extensions/auto-scroller.ephy-extension
%_libdir/epiphany/%{dir_version}/extensions/certificates.ephy-extension
%_libdir/epiphany/%{dir_version}/extensions/extensions-manager-ui.ephy-extension
%_libdir/epiphany/%{dir_version}/extensions/gestures.ephy-extension
%_libdir/epiphany/%{dir_version}/extensions/greasemonkey.ephy-extension
%_libdir/epiphany/%{dir_version}/extensions/html5tube.ephy-extension
%_libdir/epiphany/%{dir_version}/extensions/push-scroller.ephy-extension
%_libdir/epiphany/%{dir_version}/extensions/rss.ephy-extension
%_libdir/epiphany/%{dir_version}/extensions/soup-fly.ephy-extension
%_libdir/epiphany/%{dir_version}/extensions/tab-groups.ephy-extension
%_libdir/epiphany/%{dir_version}/extensions/tab-states.ephy-extension

