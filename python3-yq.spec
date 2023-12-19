# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       python3-yq

# >> macros
# << macros
%define int_name yq

Summary:    Command-line YAML/XML processor - jq wrapper for YAML/XML documents
Version:    3.1.1
Release:    0
Group:      Applications
License:    Apache-2.0
BuildArch:  noarch
URL:        https://pypi.org/project/yq/
Source0:    https://files.pythonhosted.org/packages/y/%{int_name}/%{int_name}-%{version}.tar.gz
Source100:  python3-yq.yaml
Requires:   jq
BuildRequires:  pkgconfig(python)
BuildRequires:  python3-setuptools_scm >= 3.4.3
BuildRequires:  python3-yaml >= 3.5.1
BuildRequires:  python3-rpm-macros

%description

yq takes YAML input, converts it to JSON, and pipes it to jq

%if "%{?vendor}" == "chum"
PackageName: yq
Type: console-application
Categories:
 - Utility
Custom:
  PackagingRepo: https://github.com/sailfishos-chum/python3-yq
Url:
  Homepage: https://pypi.org/project/yq/
  Help: https://pypi.org/project/yq/#description
%endif


%prep
%setup -q -n %{int_name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%{py3_build}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%{py3_install}

# >> install post
# << install post

%files
%defattr(-,root,root,-)
# >> files
%license LICENSE
%doc README.rst
%{_bindir}/*
%{python3_sitelib}/*
# << files
