Summary:	GUI search/replace tool
Summary(pl):	Graficzne narzêdzie do wyszukiwania i zamiany
Name:		regexxer
Version:	0.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	8bdbf7356b0645651a03f907675e80a6
URL:		http://regexxer.sourceforge.net/
BuildRequires:	gtkmm-devel >= 2.2.0
BuildRequires:	libsigc++-devel >= 1.2.1
BuildRequires:	pcre-devel >= 4.4-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
regexxer is a nifty GUI search/replace tool featuring Perl-style
regular expressions.

%description -l pl
regexxer jest ¶wietnym, graficznym narzêdziem do wyszukiwania i
zamiany, wykorzystuj±cym wyra¿enia regularne w stypu Perla.

%prep
%setup -q

%build
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
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
