Summary:	Runs scripts with different group/user id
Name:		runsuid
Version:	1.5
Release:	%mkrel 2
License:	GPL
Group:		System/Base
Url:		http://www.ftp.uni-erlangen.de/~runsuid/
Source0:	http://www.ftp.uni-erlangen.de/~runsuid/%{name}-%{version}.tgz
BuildRequires:	glibc-devel

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


