Summary:	Portable Object Compiler
Summary(pl):	Przenaszalny Kompilator Obiektowego C
Name:		objc
Version:	3.2.5
Release:	0.1
License:	LGPL
Group:		Development/Tools
Source0:	http://users.pandora.be/stes/%{name}-%{version}.tar.gz
# Source0-md5:	f75bbdf6ab6e1267e6e2f55609094341
Patch0:		%{name}-lib64.patch
URL:		http://users.pandora.be/stes/compiler.html
BuildRequires:	automake
BuildRequires:	byacc
BuildRequires:	flex
BuildRequires:	objc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Portable Object Compiler consists of a set of Objective-C class
libraries and a precompiler (translator) that generates plain C.

%description -l pl
Przenaszalny Kompilator Obiektowego C zawiera zbiór bibliotek
Obiektowego C oraz prekompilator (translator), który generuje kod
¼ród³owy w czystym C.

%prep
%setup -q

%if "%{_lib}" == "lib64"
%patch0 -p1
mv -f lib lib64
%endif

%build
cp -f /usr/share/automake/config.* util
%{__aclocal}
%{__autoconf}
%configure \
	--with-cplus
%{__make} \
	OPT_MFLAGS="%{rpmcflags} -DNDEBUG"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/lib,%{_libdir},%{_datadir}}

%{__make} install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_prefix}

mv	$RPM_BUILD_ROOT%{_prefix}/ma* \
	$RPM_BUILD_ROOT%{_datadir}

mv	$RPM_BUILD_ROOT%{_mandir}/man3/Object.3 \
	$RPM_BUILD_ROOT%{_mandir}/man3/ObjectO.3

%if "%{_lib}" != "lib"
mv -f $RPM_BUILD_ROOT{%{_libdir}/*.txt,%{_prefix}/lib}
%endif

find $RPM_BUILD_ROOT -type -d -name CVS |xargs rm -rf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Books.txt Changes.txt Readme.txt *.html
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.o
%{_libdir}/*.ld
%{_prefix}/lib/*.txt
%{_mandir}/man?/*
