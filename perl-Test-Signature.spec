#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%define		pdir	Test
%define		pnam	Signature
Summary:	Test::Signature - automatic signature testing
Summary(pl.UTF-8):	Test::Signature - automatyczne sprawdzanie sygnatur
Name:		perl-Test-Signature
Version:	1.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e4bc208d3a07c0d24009a12029c8cc94
URL:		http://search.cpan.org/dist/Test-Signature/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::Signature allows you to verify that a distribution has not
been tampered with. "Test::Signature" lets that be tested as part of
the distribution's test suite.

%description -l pl.UTF-8
Module::Signature pozwala sprawdzić, czy dystrybucyjna paczka nie
została naruszona. Test::Signature pozwala na sprawdzenie tego jako
część zestawu testów dystrybucyjnych.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/Signature.pm
%{_mandir}/man3/*
