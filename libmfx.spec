%global commit 7adf2e463149adf6820de745a4d9e5d9a1ba8763
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20160317
%global abi 0

Name: libmfx
Summary: Intel hardware video acceleration dispatcher library
Version: 1.16
Release: 1.%{date}git%{shortcommit}%{?dist}
URL:     https://github.com/lu-zero/mfx_dispatch
Source0: https://github.com/lu-zero/mfx_dispatch/archive/%{commit}/mfx_dispatch-%{commit}.tar.gz
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
%setup -q -n mfx_dispatch-%{commit}
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
* Sun Jul 10 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.16-1.20160317git7adf2e4
- initial build
