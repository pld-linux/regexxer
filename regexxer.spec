Summary:	GUI search/replace tool
Summary(pl):	Graficzne narzêdzie do wyszukiwania i zamiany
Name:		regexxer
Version:	0.6
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	34ef50fa035669aca8520de3d085071a
URL:		http://regexxer.sourceforge.net/
BuildRequires:	gconfmm-devel >= 2.0.1
BuildRequires:	gnome-vfsmm-devel >= 1.3.5
BuildRequires:	libsigc++12-devel >= 1.2.1
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
