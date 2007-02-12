#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Lingua
%define		pnam	EN-Inflect
Summary:	Lingua::EN::Inflect - convert singular to plural - select "a" or "an"
Summary(pl.UTF-8):   Lingua::EN::Inflect - konwersja liczby pojedynczej na mnogą z wyborem "a" lub "an"
Name:		perl-Lingua-EN-Inflect
Version:	1.89
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ca864087a32754a8185d30fa677121ea
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The exportable subroutines of Lingua::EN::Inflect provide plural
inflections, "a"/"an" selection for English words, and manipulation of
numbers as words

%description -l pl.UTF-8
Eksportowalne procedury Lingua::EN::Inflect umożliwiają konwersję
pomiędzy liczbą pojedynczą a mnogą z wyborem "a"/"an" dla wyrazów w
języku angielskim oraz manipulacje na wielu wyrazach.

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

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Lingua/EN/Inflect

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Lingua/EN/Inflect
%{perl_vendorlib}/Lingua/EN/Inflect.pm
%attr(755,root,root) %{perl_vendorlib}/Lingua/EN/demo_NO.pl
%attr(755,root,root) %{perl_vendorlib}/Lingua/EN/demo_NUM.pl
%attr(755,root,root) %{perl_vendorlib}/Lingua/EN/demo_PL.pl
%attr(755,root,root) %{perl_vendorlib}/Lingua/EN/demo_eq.pl
%attr(755,root,root) %{perl_vendorlib}/Lingua/EN/demo_inflect.pl
%{_mandir}/man3/*
