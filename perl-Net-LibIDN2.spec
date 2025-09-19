#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Net
%define		pnam	LibIDN2
Summary:	Net::LibIDN2 - Perl bindings for GNU Libidn2
Summary(pl.UTF-8):	Net::LibIDN2 - wiązania Perla do biblioteki GNU Libidn2
Name:		perl-Net-LibIDN2
Version:	1.02
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d3bc7c71d4b42d6912e0710b1683b661
URL:		https://metacpan.org/dist/Net-LibIDN2
BuildRequires:	libidn2-devel >= 2.0.0
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.10
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides bindings for GNU Libidn2, a C library for handling
internationalized domain names based on IDNA 2008, Punycode and TR46.

%description -l pl.UTF-8
Ten pakiet dostarcza wiązania do GNU Libidn2 - biblioteki C służącej
do obsługi międzynarodowych nazw domenowych, opartych na IDNA 2008,
Punycode oraz TR46.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	--config cc="%{__cc}" \
	--config optimize="%{rpmcflags} %{rpmcppflags}" \
	--installdirs=vendor

./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	destdir=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Net/LibIDN2/LibIDN2.bs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Net/LibIDN2.pm
%dir %{perl_vendorarch}/auto/Net/LibIDN2
%attr(755,root,root) %{perl_vendorarch}/auto/Net/LibIDN2/LibIDN2.so
%{_mandir}/man3/Net::LibIDN2.3*
