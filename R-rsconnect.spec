#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-rsconnect
Version  : 1.0.2
Release  : 69
URL      : https://cran.r-project.org/src/contrib/rsconnect_1.0.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rsconnect_1.0.2.tar.gz
Summary  : Deploy Docs, Apps, and APIs to 'Posit Connect', 'shinyapps.io',
Group    : Development/Tools
License  : GPL-2.0
Requires: R-cli
Requires: R-curl
Requires: R-digest
Requires: R-jsonlite
Requires: R-lifecycle
Requires: R-openssl
Requires: R-packrat
Requires: R-renv
Requires: R-rlang
Requires: R-rstudioapi
Requires: R-yaml
BuildRequires : R-cli
BuildRequires : R-curl
BuildRequires : R-digest
BuildRequires : R-jsonlite
BuildRequires : R-lifecycle
BuildRequires : R-openssl
BuildRequires : R-packrat
BuildRequires : R-renv
BuildRequires : R-rlang
BuildRequires : R-rstudioapi
BuildRequires : R-webfakes
BuildRequires : R-yaml
BuildRequires : buildreq-R

%description
'shinyapps.io', and 'Posit Connect'. Supported content types include R
    Markdown documents, Shiny applications, Plumber APIs, plots, and
    static web content.

%prep
%setup -q -n rsconnect
pushd ..
cp -a rsconnect buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692306722

%install
export SOURCE_DATE_EPOCH=1692306722
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
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/rsconnect/Meta/vignette.rds
/usr/lib64/R/library/rsconnect/NAMESPACE
/usr/lib64/R/library/rsconnect/NEWS.md
/usr/lib64/R/library/rsconnect/R/rsconnect
/usr/lib64/R/library/rsconnect/R/rsconnect.rdb
/usr/lib64/R/library/rsconnect/R/rsconnect.rdx
/usr/lib64/R/library/rsconnect/cert/cacert.pem
/usr/lib64/R/library/rsconnect/cert/shinyapps.io.pem
/usr/lib64/R/library/rsconnect/doc/custom-http.R
/usr/lib64/R/library/rsconnect/doc/custom-http.Rmd
/usr/lib64/R/library/rsconnect/doc/custom-http.html
/usr/lib64/R/library/rsconnect/doc/index.html
/usr/lib64/R/library/rsconnect/examples/diamonds/server.R
/usr/lib64/R/library/rsconnect/examples/diamonds/ui.R
/usr/lib64/R/library/rsconnect/examples/sessioninfo/server.R
/usr/lib64/R/library/rsconnect/examples/sessioninfo/ui.R
/usr/lib64/R/library/rsconnect/help/AnIndex
/usr/lib64/R/library/rsconnect/help/aliases.rds
/usr/lib64/R/library/rsconnect/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/rsconnect/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/rsconnect/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/rsconnect/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/rsconnect/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/rsconnect/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/rsconnect/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/rsconnect/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/rsconnect/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/rsconnect/help/figures/logo.png
/usr/lib64/R/library/rsconnect/help/figures/logo.svg
/usr/lib64/R/library/rsconnect/help/paths.rds
/usr/lib64/R/library/rsconnect/help/rsconnect.rdb
/usr/lib64/R/library/rsconnect/help/rsconnect.rdx
/usr/lib64/R/library/rsconnect/html/00Index.html
/usr/lib64/R/library/rsconnect/html/R.css
/usr/lib64/R/library/rsconnect/resources/environment.py
/usr/lib64/R/library/rsconnect/tests/manual/appMode.Rmd
/usr/lib64/R/library/rsconnect/tests/manual/dependencies.Rmd
/usr/lib64/R/library/rsconnect/tests/manual/deploySite.Rmd
/usr/lib64/R/library/rsconnect/tests/manual/publishing-dialog.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat.R
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/account-find.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/accounts.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/appDependencies.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/appMetadata-quarto.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/appMetadata.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/applications.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/bundle.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/bundleFiles.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/bundlePackage.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/bundlePackagePackrat.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/bundlePackageRenv.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/bundlePython.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/cookies.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/deployApp.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/deployDoc.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/deploymentTarget.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/deployments-find.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/deployments.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/http-libcurl.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/http.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/ide.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/lint.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/linters.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/secret.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/servers-deprec.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/servers.md
/usr/lib64/R/library/rsconnect/tests/testthat/_snaps/writeManifest.md
/usr/lib64/R/library/rsconnect/tests/testthat/certs/invalid.crt
/usr/lib64/R/library/rsconnect/tests/testthat/certs/localhost.crt
/usr/lib64/R/library/rsconnect/tests/testthat/certs/sample.crt
/usr/lib64/R/library/rsconnect/tests/testthat/certs/store.crt
/usr/lib64/R/library/rsconnect/tests/testthat/certs/two-cas.crt
/usr/lib64/R/library/rsconnect/tests/testthat/helper-http.R
/usr/lib64/R/library/rsconnect/tests/testthat/helper-paths.R
/usr/lib64/R/library/rsconnect/tests/testthat/helper.R
/usr/lib64/R/library/rsconnect/tests/testthat/multibyte-characters/app.R
/usr/lib64/R/library/rsconnect/tests/testthat/project-MASS/MASS.R
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-doc-none/quarto-doc-none.qmd
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-proj-r-shiny/_quarto.yml
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-proj-r-shiny/quarto-proj-r-shiny.qmd
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-website-py/_quarto.yml
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-website-py/about.qmd
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-website-py/index.qmd
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-website-py/requirements.txt
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-website-py/styles.css
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-website-r-py/_quarto.yml
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-website-r-py/about.qmd
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-website-r-py/index.qmd
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-website-r-py/requirements.txt
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-website-r-py/styles.css
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-website-r/README.md
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-website-r/_quarto.yml
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-website-r/about.qmd
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-website-r/index.qmd
/usr/lib64/R/library/rsconnect/tests/testthat/quarto-website-r/styles.css
/usr/lib64/R/library/rsconnect/tests/testthat/renv-recommended/dependences.R
/usr/lib64/R/library/rsconnect/tests/testthat/renv-recommended/renv.lock
/usr/lib64/R/library/rsconnect/tests/testthat/shiny-app-in-subdir/my-app/server.R
/usr/lib64/R/library/rsconnect/tests/testthat/shiny-app-in-subdir/my-app/ui.r
/usr/lib64/R/library/rsconnect/tests/testthat/shiny-rmds/non-shiny-rmd.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/shiny-rmds/shiny-rmd-dashes.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/shiny-rmds/shiny-rmd-dots.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-appR/app.R
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-appR/rsconnect/colorado.posit.co/hadley/shinyapp-appR.dcf
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-simple/server.R
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-simple/ui.R
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-singleR/single.R
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-with-absolute-paths/ShinyDocument.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-with-absolute-paths/ShinyPresentation.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-with-absolute-paths/data/College.txt
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-with-absolute-paths/server.R
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-with-absolute-paths/ui.R
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-with-browser/server.R
/usr/lib64/R/library/rsconnect/tests/testthat/shinyapp-with-browser/ui.R
/usr/lib64/R/library/rsconnect/tests/testthat/static-with-quarto-yaml/_quarto.yml
/usr/lib64/R/library/rsconnect/tests/testthat/static-with-quarto-yaml/slideshow.html
/usr/lib64/R/library/rsconnect/tests/testthat/test-account-find.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-accounts.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-appDependencies.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-appMetadata-quarto.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-appMetadata.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-applications.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-bundle.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-bundleFiles.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-bundlePackage.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-bundlePackagePackrat.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-bundlePackageRenv.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-bundlePython.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-cert.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-client-cloud.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-client-connect.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-client.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-config.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-cookies.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-deployApp.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-deployDoc.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-deploySite.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-deploymentTarget.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-deployments-find.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-deployments.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-http-curl.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-http-internal.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-http-libcurl.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-http-rcurl.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-http.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-ide.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-lint.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-linters.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-locale.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-plumber/plumber.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-reticulate-rmds/implicit.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/test-reticulate-rmds/index.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/test-rmd-bad-case/img/RStudio.svg
/usr/lib64/R/library/rsconnect/tests/testthat/test-rmd-bad-case/index.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/test-rmds/index.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/test-rmds/parameterized.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/test-rmds/simple.Rmd
/usr/lib64/R/library/rsconnect/tests/testthat/test-secret.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-servers-deprec.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-servers.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-shinyApp/test-shinyApp.tar.gz
/usr/lib64/R/library/rsconnect/tests/testthat/test-title.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-utils.R
/usr/lib64/R/library/rsconnect/tests/testthat/test-writeManifest.R
