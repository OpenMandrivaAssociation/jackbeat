%define name 	jackbeat
%define version 0.6.1
%define release %mkrel 2

Summary: 	Drum machine styled audio sequencer
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://www.xung.org/jackbeat/
License: 	GPL
Group: 		Sound
Source: 	http://www.xung.org/jackbeat/files/%{name}-%{version}.tar.bz2

Buildroot: 	%_tmppath/%name-%version-buildroot
BuildRequires:	ImageMagick 
BuildRequires:  jackit-devel 
BuildRequires:  gtk+2-devel 
BuildRequires:  libsndfile-devel
BuildRequires:  libsamplerate-devel

%description
Jackbeat is an audio sequencer with the following features :
    * drummachine-like interface for fast and easy edition
    * realtime operation : while playing, the pattern can be edited and
      resized, the bpm rate modified, and new samples loaded,
    * virtually unlimited number of tracks and beats
    * easy to use and yet powerful : just JACK it into jack-rack and you can
      apply LADSPA effect plugins on a per track basis, perform mastering
      with jackeq , etc...
    * loads and saves .jab files, Jackbeat's binary file format.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=JackBeat
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=AudioVideo;Sequencer;
EOF


%post
%update_menus

%postun
%update_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README 
%_bindir/%name
%{_datadir}/applications/mandriva-%{name}.desktop


