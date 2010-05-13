
%define		qtver	4.4.3

Summary:	Manager for sqlite - Sqlite Databases Made Easy
Summary(pl.UTF-8):	Zarządca baz sqlite
Name:		sqliteman
Version:	1.2.1
Release:	3
# src is GPLv2+, icons are LGPLv2+
License:	GPLv2+ and LGPLv2+
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/sqliteman/%{name}-%{version}.tar.bz2
# Source0-md5:	1ad603d38e4eda63f1386c6ee22a2838
Patch0:		%{name}-desktop.patch
URL:		http://www.sqliteman.com/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	cmake >= 2.6.2
BuildRequires:	qscintilla2-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
Requires:	QtSql-sqlite3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sqliteman is handy tool for tuning SQL statements, manage tables,
views, or triggers, administrate the database space and index
statistics.

%description -l pl.UTF-8
Sqliteman jest przydatnym narzędziem pozwalającym na optymalizację
zapytań SQL, zarządzanie tabelami, widokami czy triggerami,
administracją przestrzenią bazy i statystyk indeksów.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake  \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sqliteman
%{_iconsdir}/*.png
%{_desktopdir}/*.desktop
%{_datadir}/%{name}
