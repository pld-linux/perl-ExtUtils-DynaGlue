#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	ExtUtils
%define		pnam	DynaGlue
%include	/usr/lib/rpm/macros.perl
Summary:	ExtUtils::DynaGlue - methods for generating Perl extension files
Summary(pl.UTF-8):	ExtUtils::DynaGlue - metody do generacji plików rozszerzeń Perla
Name:		perl-ExtUtils-DynaGlue
Version:	1.00a
Release:	11
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	900f869899702bfd18c55bc661d07c6b
URL:		http://search.cpan.org/dist/ExtUtils-DynaGlue/
BuildRequires:	perl-C-Scan
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::DynaGlue module provides methods for generating Perl
extension files.

%description -l pl.UTF-8
Moduł ExtUtils::DynaGlue udostępnia metody do generowania plików
rozszerzeń Pela.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/ExtUtils/DynaGlue.pm
%{_mandir}/man3/*
