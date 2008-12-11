%define name 	jackbeat
%define version 0.6.3
%define release %mkrel 1

Summary: 	Drum machine styled audio sequencer
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://jackbeat.samalyse.org/
License: 	GPL
Group: 		Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: 	http://jackbeat.samalyse.org/downloads/jackbeat-0.6.3.tar.gz

BuildRequires:	imagemagick 
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


%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%update_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README 
%_bindir/%name
%{_datadir}/applications/mandriva-%{name}.desktop


