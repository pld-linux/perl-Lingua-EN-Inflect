#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Lingua
%define		pnam	EN-Inflect
Summary:	Lingua::EN::Inflect Perl module
Summary(cs):	Modul Lingua::EN::Inflect pro Perl
Summary(da):	Perlmodul Lingua::EN::Inflect
Summary(de):	Lingua::EN::Inflect Perl Modul
Summary(es):	Módulo de Perl Lingua::EN::Inflect
Summary(fr):	Module Perl Lingua::EN::Inflect
Summary(it):	Modulo di Perl Lingua::EN::Inflect
Summary(ja):	Lingua::EN::Inflect Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Lingua::EN::Inflect ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Lingua::EN::Inflect
Summary(pl):	Modu³ Perla Lingua::EN::Inflect
Summary(pt):	Módulo de Perl Lingua::EN::Inflect
Summary(pt_BR):	Módulo Perl Lingua::EN::Inflect
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Lingua::EN::Inflect
Summary(sv):	Lingua::EN::Inflect Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Lingua::EN::Inflect
Summary(zh_CN):	Lingua::EN::Inflect Perl Ä£¿é
Name:		perl-Lingua-EN-Inflect
Version:	1.88
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::EN::Inflect - singular to plural conversions and "a"/"an"
selection for English words.

%description -l pl
Lingua::EN::Inflect - konwersja pomiêdzy liczb± pojedyncz± a mnog± z
wyborem "a"/"an" dla wyrazów w jêzyku angielskim.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Lingua/EN/Inflect.pm
%attr(755,root,root) %{perl_vendorlib}/Lingua/EN/demo_NO.pl
%attr(755,root,root) %{perl_vendorlib}/Lingua/EN/demo_NUM.pl
%attr(755,root,root) %{perl_vendorlib}/Lingua/EN/demo_PL.pl
%attr(755,root,root) %{perl_vendorlib}/Lingua/EN/demo_eq.pl
%attr(755,root,root) %{perl_vendorlib}/Lingua/EN/demo_inflect.pl
%{_mandir}/man3/*
