%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	DynaGlue
Summary:	ExtUtils::DynaGlue perl module
Summary(pl):	Modu³ perla ExtUtils::DynaGlue
Name:		perl-ExtUtils-DynaGlue
Version:	1.00a
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	900f869899702bfd18c55bc661d07c6b
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-C-Scan
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::DynaGlue - Methods for generating Perl extension files.

%description -l pl
ExtUtils::DynaGlue - metody do generowania plików rozszerzeñ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/ExtUtils/DynaGlue.pm
%{_mandir}/man3/*
