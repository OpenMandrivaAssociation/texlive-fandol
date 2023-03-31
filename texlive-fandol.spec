Name:		texlive-fandol
Version:	37889
Release:	2
Summary:	Four basic fonts for Chinese typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/fandol
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fandol.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fandol.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/fonts/opentype/public/fandol
%doc %{_texmfdistdir}/doc/fonts/fandol

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
