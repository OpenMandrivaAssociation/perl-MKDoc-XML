%define module   MKDoc-XML
%define version    0.75
%define release    %mkrel 3

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    The MKDoc XML Toolkit
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/MKDoc/%{module}-%{version}.tar.gz
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
MKDoc is a web content management system written in Perl which focuses on
standards compliance, accessiblity and usability issues, and multi-lingual
websites.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/MKDoc

