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
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
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
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/ExtUtils/DynaGlue.pm
%{_mandir}/man3/*
