%global packname  snowfall
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.83
Release:          1
Summary:          Easier cluster computing (based on snow).
Group:            Sciences/Mathematics
License:          GPL
URL:              None
Source0:          http://cran.r-project.org/src/contrib/Archive/snowfall/snowfall_1.83.tar.gz
Requires:         R-snow 
Requires:         R-Rmpi 
BuildRequires:    R-devel texlive-collection-latex R-snow
BuildRequires:    R-Rmpi 

%description
Usability wrapper around snow for easier development of parallel R
programs. This package offers e.g. extended error checks, and additional
functions. All functions work in sequential mode, too, if no cluster is
present or wished. Package is also designed as connector to the cluster
management tool sfCluster, but can also used without it.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
