%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Clipboard history plugin for the Xfce panel
Name:		xfce4-clipman-plugin
Version:	1.1.3
Release:	%mkrel 2
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-clipman-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-clipman-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Patch0:		xfce4-clipman-plugin-1.1.3-fix-possible-null-values.patch
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	exo-devel
BuildRequires:	intltool
Requires:	xfce4-panel >= 4.4.2
Obsoletes:	xfce-clipman-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Clipboard history panel plugin for the Xfce Desktop Environment.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog COPYING AUTHORS
%{_sysconfdir}/xdg/autostart/xfce4-clipman-plugin-autostart.desktop
%{_sysconfdir}/xdg/xfce4/panel/xfce4-clipman-actions.xml
%{_bindir}/xfce4-*
%{_libdir}/xfce4/panel-plugins/%{name}
%{_datadir}/applications/xfce4-clipman-plugin.desktop
%{_iconsdir}/hicolor/*/apps/*.*g
%{_datadir}/xfce4/doc/*/images/*.*
%{_datadir}/xfce4/doc/*/xfce4-clipman-plugin.html
%{_datadir}/xfce4/panel-plugins/xfce4-clipman-plugin.desktop
