Summary:	Messager compatible with Aol Instant Messager (AIM)
Summary(pl):	Komunikator kompatybilny z Aol Instant Messager (AIM)
Name:		kaim	
Version:	0.62
Release:	0
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-configure.patch
Patch1:		%{name}-Makefile.patch
URL:		http://kaim.sourceforge.net/
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
KDE Aol Instant Messager (KAIM for short) is a replacement for classic
AIM for Linux. It lets you to meet new friends and keep in touch with
them. Something similar to ICQ. It is fully compatible with original
versions of AIM. It has "KDE" in its name but it can work and compile
properly without that environment.

%description -l pl
KDE Aol Instant Messager (KAIM w skrócie) jest zamiennikiem
klasycznego AIM dla Linuxa. Pozwala on poznawaæ nowych przyjació³ i z
nimi siê kontaktowaæ za jego pomoc±. Jestbardzo podobny do ICQ.
Zapewnia pe³n± kompatybilno¶æ z oryginaln± wersj± AIM. Posiada skrót
"KDE" w swojej nazwie, ale mo¿e doskonale obyæ siê bez tego
¶rodowiska.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

#gzip -9nf README ChangeLog 

%pre

%preun

%post

%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaim
%{_libdir}/liboptions.a
%{_datadir}/kaim
