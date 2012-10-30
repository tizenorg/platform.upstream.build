Name:           build
Summary:        A Script to Build SUSE Linux RPMs
License:        GPL-2.0+ and GPL-2.0
Group:          Development/Tools/Building
Version:        20120927
Release:        0
#!BuildIgnore:  build-mkbaselibs
Source:         obs-build-%{version}.tar.gz
BuildArch:      noarch
# Manual requires to avoid hard require to bash-static
AutoReqProv:    off
# Keep the following dependencies in sync with obs-worker package
Requires:       bash
Requires:       binutils
Requires:       perl
Requires:       tar
Recommends:     perl(Date::Language)
Recommends:     perl(Date::Parse)
Recommends:     perl(LWP::UserAgent)
Recommends:     perl(Pod::Usage)
Recommends:     perl(Time::Zone)
Recommends:     perl(URI)
Recommends:     perl(XML::Parser)
Recommends:     bsdtar
Recommends:     qemu-linux-user

Requires:       build-mkbaselibs
Recommends:     build-mkdrpms

%description
This package provides a script for building RPMs for SUSE Linux in a
chroot environment.


%package mkbaselibs
Summary:        Tools to generate base lib packages
Group:          Development/Tools/Building
# NOTE: this package must not have dependencies which may break boot strapping (eg. perl modules)

%description mkbaselibs
This package contains the parts which may be installed in the inner build system
for generating base lib packages.

%package mkdrpms
Summary:        Tools to generate delta rpms
Group:          Development/Tools/Building
Requires:       deltarpm
# XXX: we wanted to avoid that but mkdrpms needs Build::Rpm::rpmq
Requires:       build

%description mkdrpms
This package contains the parts which may be installed in the inner build system
for generating delta rpm packages.


%prep
%setup -q -n obs-build-%version

%build

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root)
%doc README
/usr/bin/build
/usr/bin/buildvc
/usr/bin/unrpm
/usr/lib/build
%{_mandir}/man1/build.1*


%files mkbaselibs
%defattr(-,root,root)
%dir /usr/lib/build
/usr/lib/build/mkbaselibs
/usr/lib/build/baselibs*

%files mkdrpms
%defattr(-,root,root)
%dir /usr/lib/build
/usr/lib/build/mkdrpms

%changelog
