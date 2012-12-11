Summary:	Runs scripts with different group/user id
Name:		runsuid
Version:	1.5
Release:	%mkrel 7
License:	GPL
Group:		System/Base
Url:		http://www.ftp.uni-erlangen.de/~runsuid/
Source0:	http://www.ftp.uni-erlangen.de/~runsuid/%{name}-%{version}.tgz
BuildRequires:	glibc-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
runsuid runs a script with another user-id/group-id, when 
the user has the right to do so according to the configuration file.
If used in the right combination with access restrictions this can 
ease the life of system administrators. Additionally, it can be used 
for running CGI-scripts as different fixed users.

%prep
%setup -q %{name}-%{version}

%build
perl -pi -e "s/MAKE_CFLAGS=-O3 -Wall/MAKE_CFLAGS=%{optflags}/" Makefile

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
install -d  %{buildroot}%{_sbindir}
install -D %{name} %{buildroot}%{_sbindir}/%{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README runsuid.rc.example
%attr(755,root,root) %{_sbindir}/%{name}




%changelog
* Sat Apr 16 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5-7mdv2011.0
+ Revision: 653313
- rebuild

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.5-6mdv2010.0
+ Revision: 433598
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 1.5-5mdv2009.0
+ Revision: 260459
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 1.5-4mdv2009.0
+ Revision: 251827
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.5-2mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Jan 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5-2mdv2007.0
+ Revision: 113482
-fix group
- Import runsuid

