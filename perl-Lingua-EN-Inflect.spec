%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Lingua-EN-Inflect perl module
Summary(pl):	Modu³ perla Lingua-EN-Inflect
Name:		perl-Lingua-EN-Inflect
Version:	1.84
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Lingua/Lingua-EN-Inflect-%{version}.tar.gz
Patch:		perl-Lingua-EN-Inflect-paths.patch
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Lingua-EN-Inflect - singular to plural conversions and "a"/"an" selection 
for English words.

%description -l pl
Lingua-EN-Inflect - konwersja pomiêdzy liczb± pojedyncz± a mnog± z wyborem
"a"/"an" dla wyrazów w jêzyku angielskim. 

%prep
%setup -q -n Lingua-EN-Inflect-%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Lingua/EN/Inflect
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

%{perl_sitelib}/Lingua/EN/Inflect.pm
%{perl_sitelib}/Lingua/EN/demo_NO.pl
%{perl_sitelib}/Lingua/EN/demo_NUM.pl
%{perl_sitelib}/Lingua/EN/demo_PL.pl
%{perl_sitelib}/Lingua/EN/demo_eq.pl
%{perl_sitelib}/Lingua/EN/demo_inflect.pl
%{perl_sitearch}/auto/Lingua/EN/Inflect

%{_mandir}/man3/*
