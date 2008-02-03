Summary:	Ngspice circuit simulator
Summary(pl.UTF-8):	Ngspice symulator obwodów
Name:		ng-spice
Version:	17
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/ngspice/%{name}-rework-%{version}.tar.gz
Source1:	%{name}.desktop
# Source0-md5:	abe283dea98b913a2122f085076865b1
URL:		http://ngspice.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ngspice is a mixed-level/mixed-signal circuit simulator. Its code is
based on three open source software packages: Spice3f5, Cider1b1 and
Xspice.

%description -l pl.UTF-8
Ngspice is a mixed-level/mixed-signal circuit simulator. Its code is
based on three open source software packages: Spice3f5, Cider1b1 and
Xspice.

%prep
%setup -q -n %{name}-rework-%{version}
find . '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
%configure \
	--enable-xspice \
	--enable-cider \
	--enable-xgraph \
	--with-x
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_desktopdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
cp -R examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANALYSES AUTHORS ChangeLog NEWS README doc/ngspice.pdf doc doc/ngspice.info*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}-rework
%{_libdir}/spice
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/ng*1*
%{_infodir}/ngspice*
%{_examplesdir}/%{name}-%{version}
