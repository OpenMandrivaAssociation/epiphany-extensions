%define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

%define epiver 2.23
%define api_version 2.23
%define svn 1648

Summary: Extensions for the GNOME Web Browser, Epiphany
Name: epiphany-extensions
Version: 2.22.2
Release: %mkrel 2
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch: epiphany-extensions-r1739-epi2.23.patch
License: GPLv2+
Group: Networking/WWW
Url: http://www.gnome.org/projects/epiphany/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: epiphany-devel >= %epiver
BuildRequires: mozilla-firefox-devel
BuildRequires: OpenSP-devel
BuildRequires: pcre-devel
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
Auto-scroller
Auto-reload
Certificates
Creative Commons License viewer
Error-viewer
Epilicious
Favicon
Gestures
Greasemonkey
Java Console
Live HTTP Headers
Net-monitor
Page-info
Permissions
Push scroller
Python Console
RSS
Select stylesheet
Sidebar
Smart-bookmarks lookup
Tab groups
Tab states

%prep
%setup -q
%patch -p1
autoconf

cp extensions/error-viewer/README README.error-viewer

%build
#gw not enabled extensions:
#net-monitor
%configure2_5x --with-extensions=actions,adblock,auto-reload,auto-scroller,certificates,cc-license-viewer,epilicious,error-viewer,extensions-manager-ui,favicon,gestures,greasemonkey,java-console,livehttpheaders,page-info,permissions,push-scroller,python-console,rss,select-stylesheet,sidebar,smart-bookmarks,tab-groups,tab-states \
%if %mdkversion <= 200700
--with-mozilla=mozilla-firefox
%endif

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name-%api_version
%find_lang %name --with-gnome
for omf in %buildroot%_datadir/omf/*/*-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done

cat %name.lang >> %name-%api_version.lang


#remove unpackaged files
rm -rf $RPM_BUILD_ROOT%{_libdir}/epiphany/%{api_version}/extensions/*.la \
      %buildroot/var/lib/scrollkeeper

%post
%update_scrollkeeper
%define schemas epilicious smart-bookmarks 
%post_install_gconf_schemas %schemas

%preun
%preun_uninstall_gconf_schemas %schemas

%postun
%clean_scrollkeeper


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name-%api_version.lang
%defattr(-,root,root)
%doc COPYING* AUTHORS NEWS README*
#%doc ChangeLog
%doc extensions/gestures/ephy-gestures.xml
%_sysconfdir/gconf/schemas/smart-bookmarks.schemas
%_sysconfdir/gconf/schemas/epilicious.schemas
%_datadir/%name/
%_datadir/epiphany/icons/hicolor/*/status/*
%dir %_datadir/omf/%name
%_datadir/omf/%name/%name-C.omf
%dir %{_libdir}/epiphany
%_libdir/epiphany/%{api_version}
