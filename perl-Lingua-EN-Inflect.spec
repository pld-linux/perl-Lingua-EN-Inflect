%include	/usr/lib/rpm/macros.perl
Summary:	Lingua-EN-Inflect perl module
Summary(pl):	Modu³ perla Lingua-EN-Inflect
Name:		perl-Lingua-EN-Inflect
Version:	1.86
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Lingua/Lingua-EN-Inflect-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua-EN-Inflect - singular to plural conversions and "a"/"an"
selection for English words.

%description -l pl
Lingua-EN-Inflect - konwersja pomiêdzy liczb± pojedyncz± a mnog± z
wyborem "a"/"an" dla wyrazów w jêzyku angielskim.

%prep
%setup -q -n Lingua-EN-Inflect-%{version}
%patch -p1

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
%{perl_sitelib}/Lingua/EN/Inflect.pm
%{perl_sitelib}/Lingua/EN/demo_NO.pl
%{perl_sitelib}/Lingua/EN/demo_NUM.pl
%{perl_sitelib}/Lingua/EN/demo_PL.pl
%{perl_sitelib}/Lingua/EN/demo_eq.pl
%{perl_sitelib}/Lingua/EN/demo_inflect.pl
%{_mandir}/man3/*
