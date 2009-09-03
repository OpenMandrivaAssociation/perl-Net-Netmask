%define	module	Net-Netmask
%define	name	perl-%{module}
%define	version	1.9015
%define	release %mkrel 4

Summary:	%{module} module for Perl
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Public Domain
Group:		Development/Perl
Source0:	http://www.cpan.org/authors/id/M/MU/MUIR/modules/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	noarch
Requires:	perl >= 0:5.00503

%description
Net-Netmask module for perl

Net::Netmask parses and understands IPv4 CIDR blocks. It's built with an
object-oriented interface. Nearly all functions are methods that operate on a
Net::Netmask object.

There are methods that provide the nearly all bits of information about a
network block that you might want.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
%make test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%{makeinstall_std}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Net/*
%{_mandir}/*/*

