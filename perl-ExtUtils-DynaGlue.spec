%include	/usr/lib/rpm/macros.perl
Summary:	ExtUtils-DynaGlue perl module
Summary(pl):	Modu³ perla ExtUtils-DynaGlue
Name:		perl-ExtUtils-DynaGlue
Version:	1.00a
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/ExtUtils/ExtUtils-DynaGlue-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-C-Scan
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils-DynaGlue - Methods for generating Perl extension files.

%description -l pl
ExtUtils-DynaGlue - metody do generowania plików rozszerzeñ.

%prep
%setup -q -n ExtUtils-DynaGlue-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/ExtUtils/DynaGlue
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/ExtUtils/DynaGlue.pm
%{perl_sitearch}/auto/ExtUtils/DynaGlue

%{_mandir}/man3/*
