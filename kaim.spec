Summary:	Messager compatible with Aol Instant Messager (AIM)
Summary(pl):	Komunikator kompatybilny z Aol Instant Messager (AIM)
Name:		kaim
Version:	0.62
Release:	3
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/kinkatta/%{name}-%{version}.tar.gz
# Source0-md5:	2d941856dfc84df2b55c404baab2da64
#Source0:	http://dl.sourceforge.net/kinkatta/kinkatta-0.91.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-configure.patch
Patch1:		%{name}-Makefile.patch
URL:		http://sourceforge.net/projects/kinkatta/
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE AOL Instant Messager (KAIM for short) is a replacement for classic
AIM for Linux. It lets you to meet new friends and keep in touch with
them. Something similar to ICQ. It is fully compatible with original
versions of AIM. It has "KDE" in its name but it can work and compile
properly without that environment.

%description -l pl
KDE AOL Instant Messager (KAIM w skrócie) jest zamiennikiem
klasycznego AIM dla Linuksa. Pozwala on poznawaæ nowych przyjació³ i z
nimi siê kontaktowaæ za jego pomoc±. Jest bardzo podobny do ICQ.
Zapewnia pe³n± kompatybilno¶æ z oryginaln± wersj± AIM. Posiada skrót
"KDE" w swojej nazwie, ale mo¿e doskonale obyæ siê bez tego
¶rodowiska.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS PROTOCOL README TODO AUTHORS
%attr(755,root,root) %{_bindir}/kaim
%{_libdir}/liboptions.a
%{_datadir}/kaim
%{_desktopdir}/kaim.desktop
