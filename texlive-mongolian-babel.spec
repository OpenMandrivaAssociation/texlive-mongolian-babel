Name:		texlive-mongolian-babel
Version:	15878
Release:	2
Summary:	A language definition file for Mongolian in Babel
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/mongolian/babel
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mongolian-babel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mongolian-babel.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mongolian-babel.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides support for Mongolian in a Cyrillic
alphabet. (The work derives from the earlier Russian work for
babel.).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mongolian-babel/mn.def
%{_texmfdistdir}/tex/latex/mongolian-babel/mongolian.ldf
%{_texmfdistdir}/tex/latex/mongolian-babel/mongolian.sty
%doc %{_texmfdistdir}/doc/latex/mongolian-babel/README
%doc %{_texmfdistdir}/doc/latex/mongolian-babel/mongolian.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mongolian-babel/mongolian.dtx
%doc %{_texmfdistdir}/source/latex/mongolian-babel/mongolian.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
