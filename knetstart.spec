Summary:	A simple ethernet setup tool for RedHat systems
Summary(pl):	Prosty konfigurator sieci dla KDE
Name:		knetstart
Version:	0.7
Release:	1
License:	GPL
Group:		Networking/Utilities
#Source0:	ftp.slinuxmachines.com:/pub/Linux/%{name}-%{version}.tar.gz   host not found
Source0:	ftp://ftp.kde.org/pub/kde/unstable/apps/network/%{name}-%{version}.tar.gz
# Source0-md5:	1575bcfaa7665c384eb46783acc9f83f
#Source0:	ftp://ftp.kde.com/pub/Administration/Network/KNetstart/knetstart-1.0.tar.gz
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This KDE program is a simple ethernet setup tool for RedHat systems.
It will connect a computer to the network quickly needing only a
maximum of three IP addresses.

Not only does Knetstart configure the local computer, it is smart
enough to test the relevant network connections such as the Gateway
and Nameserver. There is a bit of cool animation and a network map
that illustrates this search.

Knetstart has an embedded DHCP client based on RedHat's Pump code
v0.6.7. This client can automatically configure an ethernet card using
the DHCP protocol. The ip address, netmask, gateway, and nameservers
are all given by the server and inserted in the correct places by
Knetstart. The DHCP protocol is becoming increasingly popular with DSL
and other large networks.

%description -l pl
Ten program KDE jest prostym konfiguratorem sieci. Potrzebuje znaæ
najwy¿ej 3 adresy IP. KNetstart nie tylko konfiguruje lokalny
komputer, mo¿e tak¿e sprawdziæ bramkê i serwer DNS. Podczas
poszukiwania wy¶wietla siê animacja.

KNetstart ma wbudowanego klienta DHCP bazuj±cego na pump 0.6.7. Ten
klient mo¿e automatycznie ustawiæ kartê u¿ywaj±c protoko³u DHCP. Adres
IP, maska sieci, adres bramki i serwerów DNS s± brane z serwera i
wpisywane do odpowiednich plików.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knetstart
%{_applnkdir}/Internet/knetstart.kdelnk
%{_pixmapsdir}/knetstart.xpm
%{_pixmapsdir}/mini/knetstart.xpm
