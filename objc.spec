Summary:	Portable Object Compiler
Summary(pl):	Przenaszalny Kompilator Obiektowego C
Name:		objc
Version:	3.1.32
Release:	1
License:	LGPL
Group:		Development/Tools
Source0:	http://users.pandora.be/stes/objc-bootstrap-%{version}.tar.gz
# Source0-md5:	62fe18ed5caf288c4e73b115e81e6367
Source1:	http://users.pandora.be/stes/%{name}-%{version}.tar.gz
# Source1-md5:	ee713974b44d6bf8894b4ce8e8db914e
URL:		http://users.pandora.be/stes/compiler.html
BuildRequires:	automake
BuildRequires:	byacc
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Portable Object Compiler consists of a set of Objective-C class
libraries and a precompiler (translator) that generates plain C.

%description -l pl
Przenaszalny Kompilator Obiektowego C zawiera zbiór bibliotek
Obiektowego C oraz prekompilator (translator), który generuje kod
¼ród³owy w czystym C.

%prep
%setup -q -c -a1

%build
cd %{name}-bootstrap-%{version}
cp -f /usr/share/automake/config.* util
%configure2_13 \
	--prefix=$RPM_BUILD_DIR/%{name}-%{version}\
	--with-cplus
%{__make}
%{__make} install

cd ../%{name}-%{version}
cp -f /usr/share/automake/config.* util
PATH=$RPM_BUILD_DIR/%{name}-%{version}/bin:$PATH; export PATH
%configure2_13 \
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}-%{version}/{Books.txt,Changes.txt,Readme.txt,*.html}
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_mandir}/man?/*
