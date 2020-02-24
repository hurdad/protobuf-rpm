Name:           protobuf
Version:        %{VERSION}
Release:        %{RELEASE}%{?dist}
Summary:        Protocol Buffers - Google's data interchange format 
License:        BSD
Group:          Development/Libraries/C and C++
Url:            https://developers.google.com/protocol-buffers/
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)	
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel

%description
Protocol Buffers (a.k.a., protobuf) are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data.

%package compiler
Summary:        Protocol Buffers compiler
Requires:       %{name} = %{version}-%{release}
 
%description compiler
This package contains Protocol Buffers compiler for all programming
languages

%package devel
Summary:    Development headers and library for %{name}
Group:      Development/Libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   zlib-devel
Requires:   pkgconfig

%description devel
This package contains the development headers and library for %{name}.

%package static
Summary:        Static development files for %{name}
Requires:       %{name}-devel = %{version}-%{release}
 
%description static
Static libraries for Protocol Buffers
 
%package lite
Summary:        Protocol Buffers LITE_RUNTIME libraries
 
%description lite
Protocol Buffers built with optimize_for = LITE_RUNTIME.
 
The "optimize_for = LITE_RUNTIME" option causes the compiler to generate code
which only depends libprotobuf-lite, which is much smaller than libprotobuf but
lacks descriptors, reflection, and some other features.
 
%package lite-devel
Summary:        Protocol Buffers LITE_RUNTIME development libraries
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-lite = %{version}-%{release}
 
%description lite-devel
This package contains development libraries built with
optimize_for = LITE_RUNTIME.
 
The "optimize_for = LITE_RUNTIME" option causes the compiler to generate code
which only depends libprotobuf-lite, which is much smaller than libprotobuf but
lacks descriptors, reflection, and some other features.
 
%package lite-static
Summary:        Static development files for %{name}-lite
Requires:       %{name}-devel = %{version}-%{release}
 
%description lite-static
This package contains static development libraries built with
optimize_for = LITE_RUNTIME.
 
The "optimize_for = LITE_RUNTIME" option causes the compiler to generate code
which only depends libprotobuf-lite, which is much smaller than libprotobuf but
lacks descriptors, reflection, and some other features.

%prep
%setup -n %{name}-%{version}

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall	
find %{buildroot} -type f -name "*.la" -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post 
ldconfig

%post lite
ldconfig

%post compiler
ldconfig

%postun
ldconfig

%postun lite
ldconfig

%postun compiler
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_libdir}/libprotobuf.so.22*

%files compiler
%defattr(-,root,root,-)
%{_bindir}/protoc
%{_libdir}/libprotoc.so.22*

%files devel
%defattr(-,root,root,-)
%{_bindir}/protoc
%{_includedir}/google/protobuf/
%{_libdir}/libprotobuf.so
%{_libdir}/libprotoc.so
%{_libdir}/pkgconfig/*.pc

%files static
%{_libdir}/libprotobuf.a
%{_libdir}/libprotoc.a
 
%files lite
%{_libdir}/libprotobuf-lite.so.22*
 
%files lite-devel
%{_libdir}/libprotobuf-lite.so
%{_libdir}/pkgconfig/protobuf-lite.pc
 
%files lite-static
%{_libdir}/libprotobuf-lite.a

%changelog
