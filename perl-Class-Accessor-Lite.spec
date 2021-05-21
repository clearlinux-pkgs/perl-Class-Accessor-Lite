#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Accessor-Lite
Version  : 0.08
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/Class-Accessor-Lite-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/Class-Accessor-Lite-0.08.tar.gz
Summary  : 'a minimalistic variant of Class::Accessor'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Class-Accessor-Lite-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Install)

%description
NAME
Class::Accessor::Lite - a minimalistic variant of Class::Accessor
SYNOPSIS
package MyPackage;

%package dev
Summary: dev components for the perl-Class-Accessor-Lite package.
Group: Development
Provides: perl-Class-Accessor-Lite-devel = %{version}-%{release}
Requires: perl-Class-Accessor-Lite = %{version}-%{release}

%description dev
dev components for the perl-Class-Accessor-Lite package.


%package perl
Summary: perl components for the perl-Class-Accessor-Lite package.
Group: Default
Requires: perl-Class-Accessor-Lite = %{version}-%{release}

%description perl
perl components for the perl-Class-Accessor-Lite package.


%prep
%setup -q -n Class-Accessor-Lite-0.08
cd %{_builddir}/Class-Accessor-Lite-0.08

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Accessor::Lite.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Class/Accessor/Lite.pm
