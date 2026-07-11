%global tl_name fandol
%global tl_revision 37889

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Four basic fonts for Chinese typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/fandol
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fandol.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fandol.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Fandol fonts designed for Chinese typesetting. The current version
contains four styles: Song, Hei, Kai, Fang. All fonts are in OpenType
format.

