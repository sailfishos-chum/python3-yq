Name:       python3-yq

%define int_name yq

%if 0%{?sailfishos_version} >= 40500
ExclusiveArch: none
%endif

Summary:    Command-line YAML/XML processor - jq wrapper for YAML/XML documents
Version:    3.1.1
Release:    0
Group:      Applications
License:    Apache-2.0
BuildArch:  noarch
URL:        https://pypi.org/project/yq/
Source0:    https://files.pythonhosted.org/packages/y/%{int_name}/%{int_name}-%{version}.tar.gz
Requires:   jq
BuildRequires:  pkgconfig(python3)
BuildRequires:  sailfish-version < 4.5.0
BuildRequires:  python3-setuptools_scm >= 3.4.3
BuildRequires:  python3-yaml >= 3.5.1
BuildRequires:  python3-rpm-macros

%description

yq takes YAML input, converts it to JSON, and pipes it to jq

%if 0%{?_chum}
Title: yq
Type: console-application
Categories:
 - Utility
Custom:
  PackagingRepo: https://github.com/sailfishos-chum/python3-yq
Links:
  Homepage: https://pypi.org/project/yq/
  Help: https://pypi.org/project/yq/#description
%endif


%prep
%setup -q -n %{int_name}-%{version}

%build
%{py3_build}

%install
%{py3_install}

%files
%license LICENSE
%doc README.rst
%{_bindir}/*
%{python3_sitelib}/*
