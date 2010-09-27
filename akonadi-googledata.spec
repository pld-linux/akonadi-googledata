%define		qtbrver		4.6.0
Summary:	Akonadi
Summary(pl.UTF-8):	Akonadi -
Name:		akonadi-googledata
Version:	1.2.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://libgcal.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	483bb82d4492ff20edb64d3d4edc02eb
# svn co svn://anonsvn.kde.org/home/kde/trunk/kdesupport/akonadi-googledata/
#Source0:	%{name}-%{version}-%{snap}.tar.bz2
URL:		http://code.google.com/p/libgcal/
BuildRequires:	automoc4
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.6.2
BuildRequires:	libgcal-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description


%description -l pl.UTF-8



%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
-DMYSQLD_EXECUTABLE=%{_sbindir}/mysqld \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akonadi_gcal_resource
%attr(755,root,root) %{_bindir}/akonadi_googledata_resource
%{_datadir}/akonadi/agents/gcalresource.desktop
%{_datadir}/akonadi/agents/googledataresource.desktop
# %{_datadir}/locale/zh_TW/LC_MESSAGES/akonadi_gcal_resource.mo # FIXME consider using %find_lang
