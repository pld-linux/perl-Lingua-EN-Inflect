#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Lingua
%define		pnam	EN-Inflect
Summary:	Lingua::EN::Inflect - convert singular to plural - select "a" or "an"
Summary(pl):	Lingua::EN::Inflect - konwersja liczby pojedynczej na mnog± z wyborem "a" lub "an"
Name:		perl-Lingua-EN-Inflect
Version:	1.88
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e5100ee54bfb389f7ccee88af70ab6a0
Patch0:		%{name}-paths.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The exportable subroutines of Lingua::EN::Inflect provide plural
inflections, "a"/"an" selection for English words, and manipulation of
numbers as words

%description -l pl
Eksportowalne procedury Lingua::EN::Inflect umo¿liwiaj± konwersjê
pomiêdzy liczb± pojedyncz± a mnog± z wyborem "a"/"an" dla wyrazów w
jêzyku angielskim oraz manipulacje na wielu wyrazach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

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
%{perl_vendorlib}/Lingua/EN/Inflect.pm
%attr(755,root,root) %{perl_vendorlib}/Lingua/EN/demo_NO.pl
%attr(755,root,root) %{perl_vendorlib}/Lingua/EN/demo_NUM.pl
%attr(755,root,root) %{perl_vendorlib}/Lingua/EN/demo_PL.pl
%attr(755,root,root) %{perl_vendorlib}/Lingua/EN/demo_eq.pl
%attr(755,root,root) %{perl_vendorlib}/Lingua/EN/demo_inflect.pl
%{_mandir}/man3/*
