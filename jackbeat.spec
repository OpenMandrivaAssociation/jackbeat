%define name 	jackbeat
%define version 0.7.3
%define release %mkrel 1

Summary: 	Drum machine styled audio sequencer
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://jackbeat.samalyse.org/
License: 	GPLv2+
Group: 		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: 	http://jackbeat.samalyse.org/downloads/%{name}-%{version}.tar.gz
Patch0:		jackbeat-0.7.3-mdv-fix-str-fmt.patch

BuildRequires:	imagemagick 
BuildRequires:  jackit-devel 
BuildRequires:  gtk+2-devel 
BuildRequires:  libsndfile-devel
BuildRequires:  libsamplerate-devel
BuildRequires:	portaudio-devel
BuildRequires:	liblo-devel

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
%patch0 -p1 -b .strfmt

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

#menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README 
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/%{name}

