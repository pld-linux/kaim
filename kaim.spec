Summary:	Messager compatible with Aol Instant Messager (AIM)
#Summary(pl):	-
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
kaim

#%description -l pl

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
%attr(755,root,root) /usr/X11R6/bin/kaim
#whatfor?
/usr/X11R6/lib/liboptions.a
/usr/X11R6/share/kaim
