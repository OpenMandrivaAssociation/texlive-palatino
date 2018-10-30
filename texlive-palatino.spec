# revision 31835
# category Package
# catalog-ctan /fonts/urw/base35
# catalog-date 2012-06-06 22:57:48 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-palatino
Version:	20180303
Release:	3
Summary:	URW "Base 35" font pack for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/urw/base35
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/palatino.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: - Century Schoolbook (substituting for
Adobe's New Century Schoolbook); - Dingbats (substituting for
Adobe's Zapf Dingbats); - Nimbus Mono L (substituting for
Abobe's Courier); - Nimbus Roman No9 L (substituting for
Adobe's Times); - Nimbus Sans L (substituting for Adobe's
Helvetica); - Standard Symbols L (substituting for Adobe's
Symbol); - URW Bookman; - URW Chancery L Medium Italic
(substituting for Adobe's Zapf Chancery); - URW Gothic L Book
(substituting for Adobe's Avant Garde); and - URW Palladio L
(substituting for Adobe's Palatino).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/palatino/config.upl
%{_texmfdistdir}/fonts/afm/adobe/palatino/pplb8a.afm
%{_texmfdistdir}/fonts/afm/adobe/palatino/pplbi8a.afm
%{_texmfdistdir}/fonts/afm/adobe/palatino/pplr8a.afm
%{_texmfdistdir}/fonts/afm/adobe/palatino/pplri8a.afm
%{_texmfdistdir}/fonts/afm/urw/palatino/uplb8a.afm
%{_texmfdistdir}/fonts/afm/urw/palatino/uplbi8a.afm
%{_texmfdistdir}/fonts/afm/urw/palatino/uplr8a.afm
%{_texmfdistdir}/fonts/afm/urw/palatino/uplri8a.afm
%{_texmfdistdir}/fonts/map/dvips/palatino/upl.map
%{_texmfdistdir}/fonts/tfm/adobe/palatino/eurbo10.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/eurmo10.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb9c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb9d.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb9e.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb9o.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb9t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi9c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi9d.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi9e.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi9o.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi9t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbij8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbj8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbo.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbo7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbo8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbo8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbo8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbu.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbu8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr8rn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr9c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr9d.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr9e.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr9o.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr9t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrc8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrc9d.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrc9e.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrc9o.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrc9t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri9c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri9d.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri9e.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri9o.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri9t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrij8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplro.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplro7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplro8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplro8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplro8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrr8re.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrre.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrrn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplru.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplru8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/zppleb7m.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/zppleb7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/zppleb7y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/zppler7m.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/zppler7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/zppler7v.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/zppler7y.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplb7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplb8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplb8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplb8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbi7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbi8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbi8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbi8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbo7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbo8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbo8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbo8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplr7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplr8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplr8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplr8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplrc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplrc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplri7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplri8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplri8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplri8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplro7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplro8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplro8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplro8t.tfm
%{_texmfdistdir}/fonts/type1/urw/palatino/uplb8a.pfb
%{_texmfdistdir}/fonts/type1/urw/palatino/uplb8a.pfm
%{_texmfdistdir}/fonts/type1/urw/palatino/uplbi8a.pfb
%{_texmfdistdir}/fonts/type1/urw/palatino/uplbi8a.pfm
%{_texmfdistdir}/fonts/type1/urw/palatino/uplr8a.pfb
%{_texmfdistdir}/fonts/type1/urw/palatino/uplr8a.pfm
%{_texmfdistdir}/fonts/type1/urw/palatino/uplri8a.pfb
%{_texmfdistdir}/fonts/type1/urw/palatino/uplri8a.pfm
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb8c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb8t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb9c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb9d.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb9e.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb9o.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb9t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbc.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi8c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi8t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi9c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi9d.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi9e.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi9o.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi9t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbo.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbo7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbo8c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbo8t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbu.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr8c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr8t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr9c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr9d.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr9e.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr9o.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr9t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrc.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrc9d.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrc9e.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrc9o.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrc9t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri8c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri8t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri9c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri9d.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri9e.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri9o.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri9t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplro.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplro7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplro8c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplro8t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrre.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrrn.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplru.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/zppleb7m.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/zppleb7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/zppleb7y.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/zppler7m.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/zppler7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/zppler7v.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/zppler7y.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplb7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplb8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplb8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplbc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplbc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplbi7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplbi8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplbi8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplbo7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplbo8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplbo8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplr7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplr8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplr8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplrc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplrc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplri7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplri8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplri8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplro7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplro8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplro8t.vf
%{_texmfdistdir}/tex/latex/palatino/8rupl.fd
%{_texmfdistdir}/tex/latex/palatino/omlupl.fd
%{_texmfdistdir}/tex/latex/palatino/omsupl.fd
%{_texmfdistdir}/tex/latex/palatino/ot1upl.fd
%{_texmfdistdir}/tex/latex/palatino/t1upl.fd
%{_texmfdistdir}/tex/latex/palatino/ts1upl.fd

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex %{buildroot}%{_texmfdistdir}
