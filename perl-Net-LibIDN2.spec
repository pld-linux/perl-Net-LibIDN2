#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Net
%define		pnam	LibIDN2
Summary:	Net::LibIDN2 - Perl bindings for GNU Libidn2
Name:		perl-Net-LibIDN2
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d3bc7c71d4b42d6912e0710b1683b661
URL:		https://metacpan.org/release/Net-LibIDN2
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides bindings for GNU Libidn2, a C library for handling
internationalized domain names based on IDNA 2008, Punycode and TR46.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Net/LibIDN2.pm
%dir %{perl_vendorarch}/auto/Net/LibIDN2
%{perl_vendorarch}/auto/Net/LibIDN2/LibIDN2.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Net/LibIDN2/LibIDN2.so
%{_mandir}/man3/Net::LibIDN2.3*
