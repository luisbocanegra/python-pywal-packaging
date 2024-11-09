#
# spec file for package python-pywal
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define pythons python3
%global debug_package %{nil}
Name:           python-pywal
Version:        3.3.0
Release:        2%{?dist}
Summary:        Generate and change color-schemes on the fly
License:        MIT
URL:            https://github.com/dylanaraps/pywal
Source:         https://files.pythonhosted.org/packages/source/p/pywal/pywal-%{version}.tar.gz
Source1:        python-pywal.rpmlintrc
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  python3-devel
Recommends:     ImageMagick
BuildArch:      x86_64

%description
Generate and change color-schemes on the fly

%prep
%autosetup -p1 -n pywal-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{$python3_sitelib}/pywal/

%check
# Forbidden by imagemagick's security policy
%pytest -k 'not test_gen_colors'

%files
%doc README.md
%license LICENSE.md
%{_bindir}/wal
%{python3_sitelib}/pywal
%{python3_sitelib}/pywal-%{version}.dist-info

%changelog
* Fri Nov  8 2024 Luis Bocanegra <luisbocanegra@users.noreply.github.com> 3.3.0-2
- Rebuilt for Python 3.13
* Sun May 22 2024 Luis Bocanegra <luisbocanegra@users.noreply.github.com> 3.3.0-1
- new package built with tito
