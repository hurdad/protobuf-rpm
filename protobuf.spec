Name:           protobuf
Version:        %{VERSION}
Release:        %{RELEASE}%{?dist}
Summary:        Protocol Buffers - Google's data interchange format 
License:        BSD
Group:          Development/Libraries/C and C++
Url:            https://developers.google.com/protocol-buffers/
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  automake

%description
Protocol Buffers (a.k.a., protobuf) are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data.

%package devel
Summary:    Development headers and library for %{name}
Group:      Development/Libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers and library for %{name}.

%prep
%setup -n %{name}-5902e759108d14ee8e6b0b07653dac2f4e70ac73

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_libdir}/libprotobuf.so.*
%{_libdir}/libprotobuf-lite.so.*
%{_libdir}/libprotoc.so.*

%files devel
%defattr(-,root,root,-)
%{_bindir}/protoc
%{_includedir}/google/protobuf/
%{_libdir}/libprotobuf.so
%{_libdir}/libprotobuf.a
%{_libdir}/libprotobuf.la
%{_libdir}/libprotobuf-lite.so
%{_libdir}/libprotobuf-lite.a
%{_libdir}/libprotobuf-lite.la
%{_libdir}/libprotoc.so
%{_libdir}/libprotoc.a
%{_libdir}/libprotoc.la
%{_libdir}/pkgconfig/*.pc

%changelog
