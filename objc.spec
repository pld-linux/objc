Summary:	Portable Object Compiler
Summary(pl):	Przenaszalny Kompilator Obiektowego C
Name:		objc
Version:	3.1.24
Release:	1
License:	LGPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
URL:		http://users.pandora.be/stes/compiler.html
Source0:	http://users.pandora.be/stes/%{name}-%{version}-bootstrap.tar.gz
Source1:	http://users.pandora.be/stes/%{name}-%{version}.tar.gz
BuildRequires:	flex
BuildRequires:	byacc
BuildRequires:	tar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Portable Object Compiler consists of a set of Objective-C class
libraries and a precompiler (translator) that generates plain C.

%description -l pl
Przenaszalny Kompilator Obiektowego C zawiera zbiór bibliotek
Objektowego-C oraz prekompiler (translator), który generuje kod
¼ród³owy w czystym C.

%prep
%setup -q -c -a1

%build
cd %{name}-%{version}-bootstrap
%configure\
	--prefix=$RPM_BUILD_DIR/%{name}-%{version}\
	--with-cplus
%{__make}
%{__make} install

cd ../%{name}-%{version}
PATH=$RPM_BUILD_DIR/%{name}-%{version}/bin:$PATH; export PATH
%configure \
	--with-cplus
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
install -d $RPM_BUILD_ROOT{%{_prefix},%{_datadir}}

%{__make} install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_prefix}
mv	$RPM_BUILD_ROOT%{_prefix}/ma* \
	$RPM_BUILD_ROOT%{_datadir}

mv	$RPM_BUILD_ROOT%{_mandir}/man3/Object.3 \
	$RPM_BUILD_ROOT%{_mandir}/man3/ObjectO.3

gzip -9nf Books.txt Changes.txt Readme.txt *.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}-%{version}/{html,*.gz}
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_mandir}/man?/*
