%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Clipboard history plugin for the Xfce panel
Name:		xfce4-clipman-plugin
Version:	1.2.6
Release:	3
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-clipman-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-clipman-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1.0)
BuildRequires:	pkgconfig(exo-1)
BuildRequires:	intltool
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(unique-1.0)
Requires:	xfce4-panel >= 4.4.2
Obsoletes:	xfce-clipman-plugin

%description
Clipboard history panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc README ChangeLog COPYING AUTHORS
%{_sysconfdir}/xdg/autostart/xfce4-clipman-plugin-autostart.desktop
%{_sysconfdir}/xdg/xfce4/panel/xfce4-clipman-actions.xml
%{_bindir}/xfce4-*
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/applications/xfce4-clipman.desktop
%{_iconsdir}/hicolor/*/apps/*.*g
%{_datadir}/xfce4/panel/plugins/xfce4-clipman-plugin.desktop
