Summary:	Clipboard history plugin for the Xfce panel
Name:		xfce4-clipman-plugin
Version:	0.8.1
Release:	%mkrel 5
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-clipman-plugin
Source0:	http://goodies.xfce.org/releases/%{name}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
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
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/clipman.desktop
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/*
