Summary:	cpm - check for network interfaces in promiscuous mode
Summary(pl):	cpm - znajd¼ interfejsy sieciowe w trybie promiscuous
Name:		cpm
Version:	1.2
Release:	1
License:	custom (free)
Group:		Networking/Admin
Source0:	ftp://coast.cs.purdue.edu/pub/tools/unix/sysutils/%{name}/%{name}.%{version}.tar.gz
Patch0:		%{name}-include.patch
BuildRequires:	glibc-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cpm checks whether any network interface on a host is in promiscuous
mode.  Cpm uses standard BSD Unix socket(2) and ioctl(2) system calls to
determine a system's configured network interfaces, and to check whether
any of the network interfaces are currently in promiscuous mode.

%description -l pl
Cpm sprawdza, czy jaki¶ interfejs sieciowy jest w trybie promiscuous.
U¿ywa standardowych wywo³añ systemowych socket(2) i ioctl(2) do wyszukania
skonfigurowanych w systemie interfejsów sieciowych oraz do sprawdzenia,
czy które¶ z nich jest aktualnie w trybie promiscuous.

%prep
%setup -q -n %{name}.%{version}
%patch0 -p0

%build
%{__cc} cpm.c -o cpm %{rpmcflags}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%_bindir,%_mandir/man1}

install cpm   $RPM_BUILD_ROOT%{_bindir}
install cpm.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
