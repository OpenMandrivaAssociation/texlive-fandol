# revision 31345
# category Package
# catalog-ctan /fonts/fandol
# catalog-date 2013-08-04 11:01:13 +0200
# catalog-license gpl
# catalog-version 0.2
Name:		texlive-fandol
Version:	0.2
Release:	5
Summary:	Four basic fonts for Chinese typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/fandol
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fandol.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fandol.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Fandol fonts designed for Chinese typesetting. The current
version contains four styles: Song, Hei, Kai, Fang. All fonts
are in OpenType format.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/opentype/public/fandol/FandolFang-Regular.otf
%{_texmfdistdir}/fonts/opentype/public/fandol/FandolHei-Bold.otf
%{_texmfdistdir}/fonts/opentype/public/fandol/FandolHei-Regular.otf
%{_texmfdistdir}/fonts/opentype/public/fandol/FandolKai-Regular.otf
%{_texmfdistdir}/fonts/opentype/public/fandol/FandolSong-Bold.otf
%{_texmfdistdir}/fonts/opentype/public/fandol/FandolSong-Regular.otf
%doc %{_texmfdistdir}/doc/fonts/fandol/COPYING
%doc %{_texmfdistdir}/doc/fonts/fandol/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
