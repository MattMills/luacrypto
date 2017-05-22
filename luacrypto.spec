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
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/lua/5.1/
mv $RPM_BUILD_ROOT/usr/lib64/crypto.so $RPM_BUILD_ROOT/usr/local/lib/lua/5.1/
rm -rf $RPM_BUILD_ROOT/usr/share
rm -rf $RPM_BUILD_ROOT/usr/include
rm -rf $RPM_BUILD_ROOT/usr/lib64
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%files
%attr(755, -, root) /usr/local/lib/lua/5.1/crypto.so
