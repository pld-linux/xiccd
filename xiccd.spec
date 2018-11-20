Summary:	X color profile daemon
Name:		xiccd
Version:	0.2.4
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://github.com/agalakhov/xiccd/archive/v%{version}.tar.gz
# Source0-md5:	1f44dcd4eea6743039210f5b622c5117
URL:		https://github.com/agalakhov/xiccd
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.9
BuildRequires:	colord-devel >= 1.0.2
BuildRequires:	glib2-devel >= 1:2.36
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXrandr-devel >= 1.3
Requires:	colord >= 1.0.2
Requires:	glib2 >= 1:2.36
Requires:	xorg-lib-libXrandr >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xiccd is a simple bridge between colord and X. It does the following
tasks:

 * Enumerates displays and register them in colord;
 * Creates default ICC profiles based on EDID data;
 * Applies ICC profiles provided by colord;
 * Maintains user's private ICC storage directory.

It does basically the same as gnome-settings-daemon color plugin or
colord-kde but does not depend on any particular desktop. It even
doesn't depend on GTK so it doesn't create useless GTK3 dependency if
the desktop environment is GTK2-based or vice versa. The primary goal
of xiccd is providing color profile support for desktop environments
other than Gnome and KDE (Xfce, LXDE and probably others) that do not
support native color management yet. It is however not meant to be
excuse of not adding native color management to the session daemons of
them.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xiccd
%{_desktopdir}/xiccd.desktop
%{_mandir}/man8/xiccd.8*
