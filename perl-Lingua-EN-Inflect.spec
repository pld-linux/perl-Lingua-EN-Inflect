%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	EN-Inflect
Summary:	Lingua::EN::Inflect perl module
Summary(pl):	Modu� perla Lingua::EN::Inflect
Name:		perl-Lingua-EN-Inflect
Version:	1.87
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::EN::Inflect - singular to plural conversions and "a"/"an"
selection for English words.

%description -l pl
Lingua::EN::Inflect - konwersja pomi�dzy liczb� pojedyncz� a mnog� z
wyborem "a"/"an" dla wyraz�w w j�zyku angielskim.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
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
