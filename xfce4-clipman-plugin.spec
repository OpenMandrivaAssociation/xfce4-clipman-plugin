Summary:	Clipboard history plugin for the Xfce panel
Name:		xfce4-clipman-plugin
Version:	0.8.0
Release:	%mkrel 1
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-clipman-plugin
Source0:	xfce4-clipman-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.3.0
BuildRequires:	xfce-panel-devel >= 4.3.0
BuildRequires:	libxfcegui4-devel >= 4.3.90.2
BuildRequires:	intltool
Obsoletes:	xfce-clipman-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Clipboard history panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#rm $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.a

%find_lang %{name}

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog COPYING AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/clipman.desktop
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/*
