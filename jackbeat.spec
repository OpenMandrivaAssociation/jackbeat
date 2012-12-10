Summary:		Drum machine styled audio sequencer
Name:		jackbeat
Version:		0.7.6
Release:		2
Url:		http://bitbucket.org/olivierg/jackbeat/wiki/Home
License:		GPLv2+
Group:		Sound
Source0:		http://bitbucket.org/olivierg/%{name}/downloads/%{name}-%{version}.tar.gz
Patch0:		jackbeat-0.7.3-mdv-fix-str-fmt.patch
BuildRequires:	imagemagick 
BuildRequires:	jackit-devel 
BuildRequires:	gtk+2-devel >= 2.12
BuildRequires:	libalsa-devel >= 1.0.0
BuildRequires:	sndfile-devel >= 1.0.15
BuildRequires:	libsamplerate-devel >= 0.1.2
BuildRequires:	portaudio-devel
BuildRequires:	pulseaudio-devel >= 0.9.10
BuildRequires:	liblo-devel >= 0.22
BuildRequires:	libxml2-devel >= 2.6

%description
Jackbeat is an audio sequencer with the following features:
    * drummachine-like interface for fast and easy edition;
    * realtime operation : while playing, the pattern can be edited and
      resized, the bpm rate modified, and new samples loaded;
    * virtually unlimited number of tracks and beats;
    * easy to use and yet powerful : just JACK it into jack-rack and you
      can apply LADSPA effect plugins on a per track basis, perform
      mastering with jackeq , etc...
    * loads and saves .jab files, Jackbeat's binary file format.


%prep
%setup -q
%patch0 -p1 -b .strfmt


%build
LDFLAGS="-lgmodule-2.0" %configure
%make


%install
%makeinstall

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=JackBeat
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=AudioVideo;Sequencer;
EOF


%files
%doc AUTHORS ChangeLog COPYING README 
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}



%changelog
* Fri Nov 02 2012 Giovanni Mariani <mc2374@mclink.it> 0.7.6-2
- Dropped useless %%defines, BuildRoot, %mkrel, %defattr and %%clean
- Updated URL tag
- Updated BReqs according to the configure output
- Fix linking error with libgmodule-2.0

* Mon Dec 06 2010 Frank Kober <emuse@mandriva.org> 0.7.6-1mdv2011.0
+ Revision: 612559
- new version 0.7.6

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Tue Apr 27 2010 Frank Kober <emuse@mandriva.org> 0.7.5-1mdv2010.1
+ Revision: 539894
- new version (gtk bugfix) 0.9.5

* Sun Dec 06 2009 J√©r√¥me Brenier <incubusss@mandriva.org> 0.7.4-1mdv2010.1
+ Revision: 474151
- new version 0.7.4 (bugfix)

* Fri Nov 27 2009 J√©r√¥me Brenier <incubusss@mandriva.org> 0.7.3-1mdv2010.1
+ Revision: 470639
- new version 0.7.3
- use %%configure
- add Buildrequires : portaudio-devel and liblo-devel
- fix str fmt (Patch0 added)
- fix license tag
- fix %%files section
- $RPM_BUILD_ROOT -> %%{buildroot}

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.6.3-2mdv2010.0
+ Revision: 429580
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Fri Jun 20 2008 Austin Acton <austin@mandriva.org> 0.6.3-1mdv2009.0
+ Revision: 227335
- new version
- fix URL

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 08 2007 Emmanuel Andry <eandry@mandriva.org> 0.6.1-2mdv2008.0
+ Revision: 82448
- drop old menu

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Thu Mar 15 2007 Austin Acton <austin@mandriva.org> 0.6.1-1mdv2007.1
+ Revision: 144167
- new release
- Import jackbeat

* Mon Sep 04 2006 Emmanuel Andry <eandry@mandriva.org> 0.5.4-5mdv2007.0
- xdg menu

* Fri Apr 28 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 0.5.4-4mdk
- Fix BuildRequires

* Fri Apr 28 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 0.5.4-3mdk
- Fix BuildRequires

* Sat Nov 05 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.5.4-2mdk
- Fix BuildRequires
- %%mkrel

* Fri Nov 04 2005 Austin Acton <austin@mandriva.org> 0.5.4-1mdk
- New release 0.5.4

* Fri Oct 07 2005 Austin Acton <austin@mandriva.org> 0.5.3-1mdk
- New release 0.5.3

* Tue Jun 28 2005 Austin Acton <austin@mandriva.org> 0.5.2-1mdk
- New release 0.5.2

* Thu May 26 2005 Austin Acton <austin@mandriva.org> 0.5.1-1mdk
- New release 0.5.1

* Mon Apr 18 2005 Austin Acton <austin@mandrake.org> 0.4.3-1mdk
- New release 0.4.3

* Fri Apr 01 2005 Austin Acton <austin@mandrake.org> 0.4.2-1mdk
- New release 0.4.2
- fix source URL

* Thu Mar 17 2005 Austin Acton <austin@mandrake.org> 0.4.1-1mdk
- New release 0.4.1

* Fri Mar 04 2005 Austin Acton <austin@mandrake.org> 0.4.0-1mdk
- 0.4.0
- source URL

* Sun Feb 20 2005 Austin Acton <austin@mandrake.org> 0.3.3-1mdk
- 0.3.3

* Sat Jul 10 2004 Austin Acton <austin@mandrake.org> 0.2.1-1mdk
- 0.2.1

