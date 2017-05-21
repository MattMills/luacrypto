%define		debug_package %{nil}
Name:		luacrypto
Version:        1.0
Release:        1
Summary:	Lua library that enables encryption and decryption through OpenSSL
Vendor:		None
License:	MIT
URL:		https://github.com/MattMills/luacrypto
Source0:	%{name}-%{version}.tar.gz

%description
This package contains a library which provides a wrapper for OpenSSL to Lua

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name \*.la -delete

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%files
/usr/include/luacrypto/lcrypto.h
%attr(755, -, root) /usr/lib64/crypto.so
/usr/lib64/pkgconfig/luacrypto.pc
%docdir /usr/share/doc/luacrypto/
%doc /usr/share/doc/luacrypto/examples.html
%doc /usr/share/doc/luacrypto/index.html
%doc /usr/share/doc/luacrypto/license.html
%doc /usr/share/doc/luacrypto/luacrypto-128.png
%doc /usr/share/doc/luacrypto/manual.html
