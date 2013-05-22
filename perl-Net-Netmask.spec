%define	module	Net-Netmask
%define	name	perl-%{module}
%define	version	1.9015
%define	release %mkrel 8

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



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.9015-7mdv2012.0
+ Revision: 765532
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.9015-6
+ Revision: 764056
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.9015-5
+ Revision: 667277
- mass rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.9015-4mdv2011.0
+ Revision: 426551
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.9015-3mdv2009.0
+ Revision: 223904
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.9015-2mdv2008.1
+ Revision: 180528
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 1.9015-1mdv2008.0
+ Revision: 20313
- 1.9015


* Thu May 25 2006 Buchan Milne <bgmilne@mandriva.org> 1.9012-2mdv2007.0
- use mkrel

* Fri Jul 29 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.9012-1mdk
- 1.9012

* Fri Jun 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.9011-1mdk
- 1.9011

* Wed Apr 21 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.9009-1mdk
- 1.9009

* Sat Jan 24 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.9007-1mdk
- 1.9007
- use %%makeinstall_std macro
- cosmetics
- drop $RPM_OPT_FLAGS, noarch..
- fix license
- add README file to %%doc

* Wed Aug 27 2003 François Pons <fpons@mandrakesoft.com> 1.9004-1mdk
- 1.9004.

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.9002-4mdk
- rebuild for new auto{prov,req}

