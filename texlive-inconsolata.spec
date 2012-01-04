# revision 19721
# category Package
# catalog-ctan /fonts/inconsolata
# catalog-date 2010-09-07 15:05:43 +0200
# catalog-license ofl
# catalog-version undef
Name:		texlive-inconsolata
Version:	20100907
Release:	2
Summary:	A monospaced font, with support files for use with TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/inconsolata
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inconsolata.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inconsolata.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inconsolata.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Inconsolata is a monospaced font designed by Raph Levien. This
package contains the font (in both Adobe Type 1 and OpenType
formats), metric files for use with TeX, and LaTeX font
definition and other relevant files.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/fi4-ec.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/fi4-ei1.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/fi4-ot1tt.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/fi4-qxtt.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/fi4-texnansi.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/fi4-ts1.enc
%{_texmfdistdir}/fonts/map/dvips/inconsolata/fi4.map
%{_texmfdistdir}/fonts/opentype/public/inconsolata/Inconsolata.otf
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ec-inconsolata.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ei1-inconsolata.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-inconsolata.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/rm-inconsolata.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/texnansi-inconsolata.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ts1-inconsolata.tfm
%{_texmfdistdir}/fonts/type1/public/inconsolata/Inconsolata.pfb
%{_texmfdistdir}/tex/latex/inconsolata/ei1fi4.fd
%{_texmfdistdir}/tex/latex/inconsolata/inconsolata.sty
%{_texmfdistdir}/tex/latex/inconsolata/ly1fi4.fd
%{_texmfdistdir}/tex/latex/inconsolata/ot1fi4.fd
%{_texmfdistdir}/tex/latex/inconsolata/qxfi4.fd
%{_texmfdistdir}/tex/latex/inconsolata/t1fi4.fd
%{_texmfdistdir}/tex/latex/inconsolata/ts1fi4.fd
%doc %{_texmfdistdir}/doc/fonts/inconsolata/ChangeLog
%doc %{_texmfdistdir}/doc/fonts/inconsolata/GNUmakefile
%doc %{_texmfdistdir}/doc/fonts/inconsolata/NEWS
%doc %{_texmfdistdir}/doc/fonts/inconsolata/README
%doc %{_texmfdistdir}/doc/fonts/inconsolata/fonttable.pdf
%doc %{_texmfdistdir}/doc/fonts/inconsolata/inconsolata.pdf
%doc %{_texmfdistdir}/doc/fonts/inconsolata/inconsolata.tex
%doc %{_texmfdistdir}/doc/fonts/inconsolata/test-spacing.tex
%doc %{_texmfdistdir}/doc/fonts/inconsolata/test-textless.tex
%doc %{_texmfdistdir}/doc/fonts/inconsolata/test.pdf
%doc %{_texmfdistdir}/doc/fonts/inconsolata/test.tex
%doc %{_texmfdistdir}/doc/fonts/inconsolata/testmin.tex
#- source
%doc %{_texmfdistdir}/source/fonts/inconsolata/Inconsolata.sfd

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
