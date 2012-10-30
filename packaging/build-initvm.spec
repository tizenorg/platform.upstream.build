#
# spec file for package build-initvm
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           build-initvm
Summary:        A Script to Build SUSE Linux RPMs
License:        GPL-2.0+
Group:          Development/Tools/Building
Version:        20120927
Release:        0
Source:         obs-build-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
AutoReqProv:    off
Requires:       build
BuildRequires:  gcc
BuildRequires:  glibc-devel
%if 0%{?suse_version} > 1200
BuildRequires:  glibc-devel-static
%endif

%description
This package provides a script for building RPMs for SUSE Linux in a
chroot or a secure virtualized environment.


%prep
%setup -q -n obs-build-%version

%build
make CFLAGS="$RPM_BUILD_FLAGS" initvm-all

%install
make DESTDIR=$RPM_BUILD_ROOT initvm-install

%files
%defattr(-,root,root)
/usr/lib/build/initvm

%changelog
