%define	module	Net-Netmask

Summary:	%{module} module for Perl
Name:		perl-%{module}
Version:	1.9015
Release:	13
License:	Public Domain
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/authors/id/M/MU/MUIR/modules/%{module}-%{version}.tar.bz2
BuildArch: 	noarch
BuildRequires:	perl-devel

%description
Net-Netmask module for perl

Net::Netmask parses and understands IPv4 CIDR blocks. It's built with an
object-oriented interface. Nearly all functions are methods that operate on a
Net::Netmask object.

There are methods that provide the nearly all bits of information about a
network block that you might want.

%prep
%setup -qn %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Net/*
%{_mandir}/man3/*

