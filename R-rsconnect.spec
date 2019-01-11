#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rsconnect
Version  : 0.8.13
Release  : 17
URL      : https://cran.r-project.org/src/contrib/rsconnect_0.8.13.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rsconnect_0.8.13.tar.gz
Summary  : Deployment Interface for R Markdown Documents and Shiny
Group    : Development/Tools
License  : GPL-2.0
Requires: R-openssl
BuildRequires : R-PKI
BuildRequires : R-RCurl
BuildRequires : R-RJSONIO
BuildRequires : R-openssl
BuildRequires : R-packrat
BuildRequires : R-rmarkdown
BuildRequires : R-rstudioapi
BuildRequires : R-shiny
BuildRequires : R-yaml
BuildRequires : buildreq-R

%description
rsconnect
=======================================================
[![CRAN status](https://www.r-pkg.org/badges/version/rsconnect)](https://cran.r-project.org/package=rsconnect)
[![Build Status](https://travis-ci.org/rstudio/rsconnect.svg?branch=master)](https://travis-ci.org/rstudio/rsconnect)
[![lifecycle](https://img.shields.io/badge/lifecycle-stable-brightgreen.svg)](https://www.tidyverse.org/lifecycle/#stable)

%prep
%setup -q -c -n rsconnect

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547174466

%install
export SOURCE_DATE_EPOCH=1547174466
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rsconnect
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rsconnect
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rsconnect
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library rsconnect|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rsconnect/DESCRIPTION
/usr/lib64/R/library/rsconnect/INDEX
/usr/lib64/R/library/rsconnect/Meta/Rd.rds
/usr/lib64/R/library/rsconnect/Meta/features.rds
/usr/lib64/R/library/rsconnect/Meta/hsearch.rds
/usr/lib64/R/library/rsconnect/Meta/links.rds
/usr/lib64/R/library/rsconnect/Meta/nsInfo.rds
/usr/lib64/R/library/rsconnect/Meta/package.rds
/usr/lib64/R/library/rsconnect/NAMESPACE
/usr/lib64/R/library/rsconnect/R/rsconnect
/usr/lib64/R/library/rsconnect/R/rsconnect.rdb
/usr/lib64/R/library/rsconnect/R/rsconnect.rdx
/usr/lib64/R/library/rsconnect/cert/cacert.pem
/usr/lib64/R/library/rsconnect/cert/shinyapps.io.pem
/usr/lib64/R/library/rsconnect/examples/diamonds/server.R
/usr/lib64/R/library/rsconnect/examples/diamonds/ui.R
/usr/lib64/R/library/rsconnect/examples/sessioninfo/server.R
/usr/lib64/R/library/rsconnect/examples/sessioninfo/ui.R
/usr/lib64/R/library/rsconnect/help/AnIndex
/usr/lib64/R/library/rsconnect/help/aliases.rds
/usr/lib64/R/library/rsconnect/help/paths.rds
/usr/lib64/R/library/rsconnect/help/rsconnect.rdb
/usr/lib64/R/library/rsconnect/help/rsconnect.rdx
/usr/lib64/R/library/rsconnect/html/00Index.html
/usr/lib64/R/library/rsconnect/html/R.css
/usr/lib64/R/library/rsconnect/resources/environment.py
