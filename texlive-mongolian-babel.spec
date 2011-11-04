# revision 15878
# category Package
# catalog-ctan /language/mongolian/babel
# catalog-date 2010-06-08 01:06:42 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-mongolian-babel
Version:	1.2
Release:	1
Summary:	A language definition file for Mongolian in Babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/mongolian/babel
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mongolian-babel.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mongolian-babel.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mongolian-babel.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package provides support for Mongolian in a Cyrillic
alphabet. (The work derives from the earlier Russian work for
babel.).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
