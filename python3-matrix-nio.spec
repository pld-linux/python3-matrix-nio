%define		module		nio
%define		egg_name	nio
Summary:	A Python Matrix client library
Name:		python3-matrix-nio
Version:	0.21.2
Release:	1
License:	ISC
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/matrix-nio/
Source0:	https://files.pythonhosted.org/packages/source/m/matrix-nio/matrix_nio-%{version}.tar.gz
# Source0-md5:	30da9fe8d49cf2c67c1451e51142dcf9
URL:		https://github.com/poljar/matrix-nio
BuildRequires:	python3 >= 1:3.8
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.8
Requires:	python3-olm
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nio is a multilayered Matrix client library. The underlying base layer
doesn't do any network IO on its own, but on top of that is a
full-fledged batteries-included asyncio layer using aiohttp. File IO
is only done if you enable end-to-end encryption (E2EE).

%prep
%setup -q -n matrix_nio-%{version}
cat > setup.py <<EOF
from setuptools import setup
setup(version='%{version}')
EOF

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
