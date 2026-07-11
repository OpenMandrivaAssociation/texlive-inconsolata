%global tl_name inconsolata
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.121
Release:	%{tl_revision}.1
Summary:	A monospaced font, with support files for use with TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/inconsolata
License:	ofl apache2 lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inconsolata.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inconsolata.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Inconsolata is a monospaced font designed by Raph Levien. This package
contains the font (in both Adobe Type 1 and OpenType formats) in regular
and bold weights, with additional glyphs and options to control slashed
zero, upright quotes and a shapelier lower-case L, plus metric files for
use with TeX, and LaTeX font definition and other relevant files.

