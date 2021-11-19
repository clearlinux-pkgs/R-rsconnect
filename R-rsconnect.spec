#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rsconnect
Version  : 0.8.25
Release  : 49
URL      : https://cran.r-project.org/src/contrib/rsconnect_0.8.25.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rsconnect_0.8.25.tar.gz
Summary  : Deployment Interface for R Markdown Documents and Shiny
Group    : Development/Tools
License  : GPL-2.0
Requires: R-curl
Requires: R-digest
Requires: R-jsonlite
Requires: R-openssl
Requires: R-packrat
Requires: R-rstudioapi
Requires: R-yaml
BuildRequires : R-curl
BuildRequires : R-digest
BuildRequires : R-jsonlite
BuildRequires : R-openssl
BuildRequires : R-packrat
BuildRequires : R-rstudioapi
BuildRequires : R-yaml
BuildRequires : buildreq-R

%description
'RStudio Connect'. Supported content types include R Markdown documents,
    Shiny applications, Plumber APIs, plots, and static web content.

%prep
%setup -q -c -n rsconnect
cd %{_builddir}/rsconnect

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637337803

%install
export SOURCE_DATE_EPOCH=1637337803
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rsconnect
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rsconnect
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rsconnect
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rsconnect || :


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
/usr/lib64/R/library/rsconnect/NEWS.md
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
/usr/lib64/R/library/rsconnect/help/figures/logo.png
/usr/lib64/R/library/rsconnect/help/figures/logo.svg
/usr/lib64/R/library/rsconnect/help/paths.rds
/usr/lib64/R/library/rsconnect/help/rsconnect.rdb
/usr/lib64/R/library/rsconnect/help/rsconnect.rdx
/usr/lib64/R/library/rsconnect/html/00Index.html
/usr/lib64/R/library/rsconnect/html/R.css
/usr/lib64/R/library/rsconnect/resources/environment.py
/usr/lib64/R/library/rsconnect/tests/testthat.R
/usr/lib64/R/library/rsconnect/tests/testthat/certs/invalid.crt
/usr/lib64/R/library/rsconnect/tests/testthat/certs/localhost.crt
/usr/lib64/R/library/rsconnect/tests/testthat/certs/sample.crt
/usr/lib64/R/library/rsconnect/tests/testthat/certs/store.crt
/usr/lib64/R/library/rsconnect/tests/testthat/certs/two-cas.crt
/usr/lib64/R/library/rsconnect/tests/testthat/helper.R
/usr/lib64/R/library/rsconnect/tests/testthat/multibyte-characters/app.R
/usr/lib64/R/library/rsconnect/tests/testthat/project-MASS/MASS.R
/usr/lib64/R/library/rsconnect/tests/testthat/shiny-app-in-subdir/my-app/server.R
/usr/lib64/R/library/rsconnect/tests/testthat/shiny-app-in-subdir/my-app/ui.r
/usr/lib64/R/library/rsconnect/tests/testthat/shiny-rmds/non-shiny-rmd.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/shiny-rmds/shiny-rmd-dashes.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/shiny-rmds/shiny-rmd-dots.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-appR/app.R
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-simple/server.R
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-simple/ui.R
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-singleR/single.R
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-with-absolute-paths/College.txt
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-with-absolute-paths/ShinyDocument.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-with-absolute-paths/ShinyPresentation.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-with-absolute-paths/server.R
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-with-absolute-paths/subdir/Genetics.txt
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-with-absolute-paths/ui.R
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-with-browser/server.R
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-with-browser/ui.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-bundle.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-cert.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-connect.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-cookies.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-detection.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-hashes.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-http.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-lint.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-plumber/plumber.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-reticulate-rmds/implicit.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/test-reticulate-rmds/index.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/test-rmd-bad-case/RStudio.svg
/usr/lib64/R/library/rsconnect/tests/testthat/test-rmd-bad-case/index.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/test-rmds/index.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/test-rmds/parameterized.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/test-rmds/simple.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/test-shinyApp/test-shinyApp.tar.gz
/usr/lib64/R/library/rsconnect/tests/testthat/test-title.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-utils.R
/usr/lib64/R/library/rsconnect/tests/testthat/tf-human-readable-saved-model/1/saved_model.pbtxt
/usr/lib64/R/library/rsconnect/tests/testthat/tf-saved-model-rootdir/saved_model.pb
/usr/lib64/R/library/rsconnect/tests/testthat/tf-saved-model/1/saved_model.pb
