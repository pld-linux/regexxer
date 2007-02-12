Summary:	GUI search/replace tool
Summary(pl.UTF-8):	Graficzne narzędzie do wyszukiwania i zamiany
Name:		regexxer
Version:	0.8
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	acaa19b119cc7159c42b7f93e02f9fbd
URL:		http://regexxer.sourceforge.net/
BuildRequires:	gconfmm-devel >= 2.6.1
BuildRequires:	gtkmm-devel >= 2.4.0
BuildRequires:	libglademm-devel >= 2.4.0
BuildRequires:	pcre-devel >= 4.4-3
Requires(post): GConf2 >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
regexxer is a nifty GUI search/replace tool featuring Perl-style
regular expressions.

%description -l pl.UTF-8
regexxer jest świetnym, graficznym narzędziem do wyszukiwania i
zamiany, wykorzystującym wyrażenia regularne w stylu Perla.

%prep
%setup -q

%build
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%post
%gconf_schema_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_sysconfdir}/gconf/schemas/%{name}.schemas
