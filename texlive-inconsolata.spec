# revision 32983
# category Package
# catalog-ctan /fonts/inconsolata
# catalog-date 2014-02-15 09:25:11 +0100
# catalog-license ofl
# catalog-version 1.04
Name:		texlive-inconsolata
Epoch:		1
Version:	1.04
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
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ly1-0.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ly1-1.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ly1-2.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ly1-3.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ly1-4.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ly1-5.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ly1-6.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ly1-7.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ot1-0.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ot1-1.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ot1-2.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ot1-3.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ot1-4.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ot1-5.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ot1-6.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ot1-7.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-qx-0.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-qx-1.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-qx-2.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-qx-3.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-qx-4.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-qx-5.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-qx-6.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-qx-7.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-t1-0.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-t1-1.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-t1-2.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-t1-3.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-t1-4.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-t1-5.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-t1-6.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-t1-7.enc
%{_texmfdistdir}/fonts/enc/dvips/inconsolata/i4-ts1.enc
%{_texmfdistdir}/fonts/map/dvips/inconsolata/zi4.map
%{_texmfdistdir}/fonts/opentype/public/inconsolata/Inconsolatazi4-Bold.otf
%{_texmfdistdir}/fonts/opentype/public/inconsolata/Inconsolatazi4-Regular.otf
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4b-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4b-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4b-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4b-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4b-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4b-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4b-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4b-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4r-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4r-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4r-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4r-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4r-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4r-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4r-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ly1-zi4r-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4b-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4b-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4b-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4b-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4b-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4b-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4b-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4b-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4r-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4r-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4r-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4r-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4r-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4r-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4r-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ot1-zi4r-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4b-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4b-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4b-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4b-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4b-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4b-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4b-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4b-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4r-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4r-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4r-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4r-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4r-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4r-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4r-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/qx-zi4r-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4b-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4b-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4b-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4b-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4b-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4b-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4b-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4b-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4r-0.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4r-1.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4r-2.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4r-3.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4r-4.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4r-5.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4r-6.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/t1-zi4r-7.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ts1-zi4b.tfm
%{_texmfdistdir}/fonts/tfm/public/inconsolata/ts1-zi4r.tfm
%{_texmfdistdir}/fonts/type1/public/inconsolata/Inconsolata-zi4b.pfb
%{_texmfdistdir}/fonts/type1/public/inconsolata/Inconsolata-zi4r.pfb
%{_texmfdistdir}/tex/latex/inconsolata/inconsolata.sty
%{_texmfdistdir}/tex/latex/inconsolata/ly1zi4.fd
%{_texmfdistdir}/tex/latex/inconsolata/ot1zi4.fd
%{_texmfdistdir}/tex/latex/inconsolata/qxzi4.fd
%{_texmfdistdir}/tex/latex/inconsolata/t1zi4.fd
%{_texmfdistdir}/tex/latex/inconsolata/ts1zi4.fd
%{_texmfdistdir}/tex/latex/inconsolata/zi4.sty
%doc %{_texmfdistdir}/doc/fonts/inconsolata/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/inconsolata/README
%doc %{_texmfdistdir}/doc/fonts/inconsolata/afmcmds.txt
%doc %{_texmfdistdir}/doc/fonts/inconsolata/inconsolata-doc.pdf
%doc %{_texmfdistdir}/doc/fonts/inconsolata/inconsolata-doc.tex
%doc %{_texmfdistdir}/doc/fonts/inconsolata/novarqu-crop.pdf
%doc %{_texmfdistdir}/doc/fonts/inconsolata/novarqu-noupq-crop.pdf
%doc %{_texmfdistdir}/doc/fonts/inconsolata/varqu-noupq-crop.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
