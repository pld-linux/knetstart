%define kdeprefix /usr

Summary:	A simple ethernet setup tool for RedHat systems
Name:		knetstart
Version:	0.7
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Source0:	ftp.slinuxmachines.com:/pub/Linux/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
Requires:	qt kdelibs

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

%prep
%setup -q

%build
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install

%files
%defattr(644,root,root,755)

%{kdeprefix}/share/doc/HTML/en/knetstart/index-1.html
%{kdeprefix}/share/doc/HTML/en/knetstart/index-2.html
%{kdeprefix}/share/doc/HTML/en/knetstart/index-3.html
%{kdeprefix}/share/doc/HTML/en/knetstart/index-4.html
%{kdeprefix}/share/doc/HTML/en/knetstart/index-5.html
%{kdeprefix}/share/doc/HTML/en/knetstart/index-6.html
%{kdeprefix}/share/doc/HTML/en/knetstart/index.html

%{kdeprefix}/bin/knetstart
%{kdeprefix}/share/applnk/Internet/knetstart.kdelnk
%{kdeprefix}/share/icons/knetstart.xpm
%{kdeprefix}/share/icons/mini/knetstart.xpm

%clean
rm -rf $RPM_BUILD_ROOT
