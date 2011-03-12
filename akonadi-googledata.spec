Summary:	Google contacts and calendar Akonadi resource plugin
Summary(pl.UTF-8):	Wtyczka zasobów Kalendarz i kontaktów Google dla Akonadi
Name:		akonadi-googledata
Version:	1.2.0
Release:	2
License:	LGPL v2.1
Group:		X11/Applications
Source0:	http://libgcal.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	483bb82d4492ff20edb64d3d4edc02eb
URL:		http://code.google.com/p/libgcal/
BuildRequires:	akonadi-devel
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.6.2
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	libgcal-devel
BuildRequires:	libxslt-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin allowing synchronizing Google calendar and contacts with KDE
applications like KOrganizer, Kontact or Kaddressbook.

%description -l pl.UTF-8
Wtyczka pozwalająca na synchronizację kalendarza oraz kontaktów Google
z programami środowiska KDE, takimi jak KOrganizer, Kontakt czy
Kaddressbook.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DMYSQLD_EXECUTABLE=%{_sbindir}/mysqld \
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/akonadi_gcal_resource
%attr(755,root,root) %{_bindir}/akonadi_googledata_resource
%{_datadir}/akonadi/agents/gcalresource.desktop
%{_datadir}/akonadi/agents/googledataresource.desktop
