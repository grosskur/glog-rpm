Name:           glog
Version:        0.1.2
Release:        6%{?dist}
Summary:        A C++ application logging library

Group:          System Environment/Libraries
License:        BSD
URL:            http://code.google.com/p/google-glog
Source0:        http://google-glog.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:         glog-lpthread.patch
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  autoconf
#Requires:       

%description
Google glog is a library that implements application-level
logging. This library provides logging APIs based on C++-style
streams and various helper macros.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p0


%build
autoconf
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README
%{_libdir}/libglog.so.*

%files devel
%defattr(-,root,root,-)
%doc doc/designstyle.css doc/glog.html
%{_libdir}/libglog.so
%dir %{_includedir}/glog
%{_includedir}/glog/*


%changelog
* Thu Dec 4 2008 John A. Khvatov <ivaxer@fedoraproject.org> 0.1.2-6
- fix %%{_includedir}
- fixed documentation

* Wed Dec 3 2008 John A. Khvatov <ivaxer@fedoraproject.org> 0.1.2-5
- Added configure regeneration

* Tue Dec 2 2008 John A. Khvatov <ivaxer@fedoraproject.org> 0.1.2-4
- Initial release
