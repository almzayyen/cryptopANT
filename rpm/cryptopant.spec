%define sover   1
%define libname libcryptopant%{sover}
Name:           cryptopant
Version:        1.2.0
Release:        1%{?dist}
Summary:        IP address anonymization library
Group:          Development/Libraries/C and C++

License:        GPL-2.0-only
URL:            http://ant.isi.edu/software/cryptopANT/index.html
Source0:        %{name}_%{version}.orig.tar.gz

BuildRequires:  openssl-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
cryptopANT is a library for IP address anonymization. It implements
a widely used prefix-preserving technique known as "cryptopan".
This is ANT's project implementation of this technique for
anonymization of ipv4 and ipv6 addresses.

%package -n %{libname}
Summary:        IP address anonymization library shared library
Group:          System/Libraries

%description -n %{libname}
cryptopANT is a library for IP address anonymization. It implements
a widely used prefix-preserving technique known as "cryptopan".
This is ANT's project implementation of this technique for
anonymization of ipv4 and ipv6 addresses.

%package devel
Summary:        IP address anonymization library development files
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       openssl-devel

%description devel
cryptopANT is a library for IP address anonymization. It implements
a widely used prefix-preserving technique known as "cryptopan".
This is ANT's project implementation of this technique for
anonymization of ipv4 and ipv6 addresses.


%prep
%setup -q -n %{name}_%{version}


%build
sh autogen.sh
%configure --without-scramble_ips
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%post -n %{libname}
/sbin/ldconfig


%postun -n %{libname}
/sbin/ldconfig


%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/libcryptopant.so.%{sover}*


%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_mandir}/man3/*
%{_libdir}/libcryptopant.so
%exclude %{_libdir}/libcryptopant.a
%exclude %{_libdir}/libcryptopant.la


%changelog
* Wed Jun 19 2019 Jerry Lundström <lundstrom.jerry@gmail.com> 1.2.0-1
- Update to v1.2.0
* Thu Nov 29 2018 Jerry Lundström <lundstrom.jerry@gmail.com> 1.1.0-1
- Initial v1.1.0 code
