%define module   MKDoc-XML

Name:		perl-%{module}
Version:	0.75
Release:	6
License:	GPL or Artistic
Group:		Development/Perl
Summary:	The MKDoc XML Toolkit
Url:		https://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/MKDoc/%{module}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
MKDoc is a web content management system written in Perl which focuses on
standards compliance, accessiblity and usability issues, and multi-lingual
websites.

%prep
%setup -q -n %{module}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/MKDoc

%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.75-3mdv2010.0
+ Revision: 430504
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.75-2mdv2009.0
+ Revision: 268575
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.75-1mdv2009.0
+ Revision: 213620
- import perl-MKDoc-XML


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.75-1mdv2009.0
- first mdv release
