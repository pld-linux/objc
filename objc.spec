Summary:	Portable Object Compiler
Summary(pl):	Przenaszalny Kompilator Obiektowego C
Name:		objc
Version:	3.1.32
Release:	2
License:	LGPL
Group:		Development/Tools
Source0:	http://users.pandora.be/stes/objc-bootstrap-%{version}.tar.gz
# Source0-md5:	62fe18ed5caf288c4e73b115e81e6367
Source1:	http://users.pandora.be/stes/%{name}-%{version}.tar.gz
# Source1-md5:	ee713974b44d6bf8894b4ce8e8db914e
Patch0:		%{name}-lib64.patch
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

%if "%{_lib}" == "lib64"
%patch0 -p0
mv -f %{name}-%{version}/{lib,lib64}
ln -sf lib64 %{name}-%{version}/lib
%endif

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
install -d $RPM_BUILD_ROOT{%{_prefix}/lib,%{_libdir},%{_datadir}}

%{__make} install -C %{name}-%{version} \
	INSTALLDIR=$RPM_BUILD_ROOT%{_prefix}

mv	$RPM_BUILD_ROOT%{_prefix}/ma* \
	$RPM_BUILD_ROOT%{_datadir}

mv	$RPM_BUILD_ROOT%{_mandir}/man3/Object.3 \
	$RPM_BUILD_ROOT%{_mandir}/man3/ObjectO.3

%if "%{_lib}" != "lib"
mv -f $RPM_BUILD_ROOT{%{_libdir}/*.txt,%{_prefix}/lib}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}-%{version}/{Books.txt,Changes.txt,Readme.txt,*.html}
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.o
%{_libdir}/*.ld
%{_prefix}/lib/*.txt
%{_mandir}/man?/*
