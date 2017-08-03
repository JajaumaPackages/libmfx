#global commit e6fc25c974839dcbcf483edee01f51142ddc74f3
#global shortcommit %(c=%{commit}; echo ${c:0:7})
#global date 20170322
%global abi 0

Name: libmfx
Summary: Intel hardware video acceleration dispatcher library
Version: 1.21
Release: 3%{?dist}
URL:     https://github.com/lu-zero/mfx_dispatch
Source0: https://github.com/lu-zero/mfx_dispatch/archive/%{version}.tar.gz#/libmfx-%{version}.tar.gz
License: BSD
BuildRequires: gcc-c++
BuildRequires: libdrm-devel
BuildRequires: libtool
BuildRequires: libva-devel
ExclusiveArch: %{ix86} x86_64

%description
The dispatcher is a layer that lies between applications and Intel Media SDK
implementations. Upon initialization, the dispatcher locates the appropriate
platform-specific SDK implementation. If there is none, it will select the
software SDK implementation. The dispatcher will redirect subsequent function
calls to the same functions in the selected SDK implementation.

%package devel
Summary: Intel hardware video acceleration dispatcher library - development files
Requires: %{name}%{_isa} = %{version}-%{release}

%description devel
The dispatcher is a layer that lies between applications and Intel Media SDK
implementations. Upon initialization, the dispatcher locates the appropriate
platform-specific SDK implementation. If there is none, it will select the
software SDK implementation. The dispatcher will redirect subsequent function
calls to the same functions in the selected SDK implementation.

This package contains the development files.

%prep
%setup -q -n mfx_dispatch-%{version}
chmod 644 mfx/*.h
autoreconf -vif

%build
%configure --disable-static --enable-shared
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/libmfx.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libmfx.so.%{abi}*

%files devel
%{_includedir}/mfx
%{_libdir}/pkgconfig/libmfx.pc
%{_libdir}/libmfx.so

%changelog
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 Dominik Mierzejewski <rpm@greysector.net> - 1.21-1.20170322gite6fc25c
- update to 1.21

* Tue Feb 14 2017 Dominik Mierzejewski <rpm@greysector.net> - 1.19-1.20170114gita5ba231
- update to 1.19 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-2.20160317git7adf2e4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 10 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.16-1.20160317git7adf2e4
- initial build
