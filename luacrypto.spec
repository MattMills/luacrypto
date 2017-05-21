%define debug_package %{nil}
Name:		lua_crypto
Version:        %{version}
Release:        %{build_number}
Summary:	Lua library that enables encryption and decryption through OpenSSL
Vendor:		None
License:	MIT
URL:		https://github.com/MattMills/luacrypto
Source:		%{_sourcedir}/

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

