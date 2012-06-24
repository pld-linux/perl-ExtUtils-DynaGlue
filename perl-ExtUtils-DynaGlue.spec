%include	/usr/lib/rpm/macros.perl
Summary:	ExtUtils-DynaGlue perl module
Summary(pl):	Modu� perla ExtUtils-DynaGlue
Name:		perl-ExtUtils-DynaGlue
Version:	1.00a
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/ExtUtils/ExtUtils-DynaGlue-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-C-Scan
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils-DynaGlue - Methods for generating Perl extension files.

%description -l pl
ExtUtils-DynaGlue - metody do generowania plik�w rozszerze�.

%prep
%setup -q -n ExtUtils-DynaGlue-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/ExtUtils/DynaGlue.pm
%{_mandir}/man3/*
