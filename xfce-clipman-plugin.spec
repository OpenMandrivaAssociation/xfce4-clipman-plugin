Summary:	Clipboard history plugin for the Xfce panel
Name:		xfce-clipman-plugin
Version:	0.8.0
Release:	%mkrel 2
Epoch:		1
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-clipman-plugin
Source0:	xfce4-clipman-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.3.0
BuildRequires:	xfce-panel-devel >= 4.3.0
BuildRequires:	libxfcegui4-devel >= 4.3.90.2
BuildRequires:	intltool
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Clipboard history panel plugin for the Xfce Desktop Environment.

%prep
%setup -qn xfce4-clipman-plugin-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

#rm $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.a

%find_lang xfce4-clipman

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf %{buildroot}

%files -f xfce4-clipman.lang
%defattr(-,root,root)
%doc README ChangeLog COPYING AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/clipman.desktop
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/*
