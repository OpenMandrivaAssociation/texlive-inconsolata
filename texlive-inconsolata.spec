Name:		texlive-inconsolata
Epoch:		1
Version:	1.114
Release:	1
Summary:	A monospaced font, with support files for use with TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/inconsolata
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inconsolata.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inconsolata.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Inconsolata is a monospaced font designed by Raph Levien. This
package contains the font (in both Adobe Type 1 and OpenType
formats) in regular and bold weights, with additional glyphs
and options to control slashed zero, upright quotes and a
shapelier lower-case L, plus metric files for use with TeX, and
LaTeX font definition and other relevant files.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/inconsolata
%{_texmfdistdir}/fonts/map/dvips/inconsolata
%{_texmfdistdir}/fonts/opentype/public/inconsolata
%{_texmfdistdir}/fonts/tfm/public/inconsolata
%{_texmfdistdir}/fonts/type1/public/inconsolata
%{_texmfdistdir}/tex/latex/inconsolata
%doc %{_texmfdistdir}/doc/fonts/inconsolata

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
