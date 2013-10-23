%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Clipboard history plugin for the Xfce panel
Name:		xfce4-clipman-plugin
Version:	1.2.3
Release:	7
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-clipman-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-clipman-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfce4ui-devel >= 4.9.1
BuildRequires:	exo-devel
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


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 1.2.3-2
+ Revision: 791551
- Rebuild

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - update to new version 1.2.3

* Sun Apr 08 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.2-1
+ Revision: 789912
- add uniqie-1.0 to the buildrequires
- fix file list
- add xtst to buildrequires
- fix br
- drop patch 0
- update to new version 1.2.2
- drop old stuff from spec file

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Mon Mar 29 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.3-2mdv2010.1
+ Revision: 528650
- Patch0: fix possible null values

* Thu Nov 19 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.3-1mdv2010.1
+ Revision: 467488
- update to new version 1.1.3

* Tue Oct 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.1-1mdv2010.0
+ Revision: 455244
- update to new version 1.1.1
- adapt to new URL schemas for Xfce sources

* Mon Sep 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.0-1mdv2010.0
+ Revision: 432906
- update to new version 1.1.0
- fix file list

* Wed Jul 01 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.2-1mdv2010.0
+ Revision: 391133
- update to new version 1.0.2
- fix file list

* Thu May 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.1-1mdv2010.0
+ Revision: 375807
- update to new version 1.0.1

* Fri May 01 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-1mdv2010.0
+ Revision: 369239
- update to new version 1.0.0
- fix file list

* Mon Apr 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.1-1mdv2009.1
+ Revision: 364417
- update to new version 0.9.1

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.0-2mdv2009.1
+ Revision: 349446
- rebuild for xfce-4.6.0

* Tue Jan 20 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.0-1mdv2009.1
+ Revision: 331472
- add buildrequires on exo-devel
- update to new version 0.9.0

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.1-5mdv2009.1
+ Revision: 294990
- rebuild for new Xfce4.6 beta1

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.8.1-4mdv2009.0
+ Revision: 262354
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.8.1-3mdv2009.0
+ Revision: 256816
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Mar 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.1-1mdv2008.1
+ Revision: 182065
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.0-1mdv2008.1
+ Revision: 110097
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- use upstram name

* Thu May 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.8.0-2mdv2008.0
+ Revision: 33206
- add macros to %%post and %%postun
- spec file clean

