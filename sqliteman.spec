Summary:	Manager for sqlite - Sqlite Databases Made Easy
Summary(pl.UTF-8):	Zarządca baz sqlite
Name:		sqliteman
Version:	1.2.0
Release:	3
# src is GPLv2+, icons are LGPLv2+
License:	GPLv2+ and LGPLv2+
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/sqliteman/%{name}-%{version}.tar.bz2
# Source0-md5:	903aee0f7eae0d4af6c960ea755b12ac
URL:		http://www.sqliteman.com/
BuildRequires:	QtSql-devel
BuildRequires:	QtXml-devel
BuildRequires:	qscintilla2-devel
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

%build
%cmake . \
	-DCMAKE_INSTALL_PREFIX=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/*.png
%{_desktopdir}/*.desktop
%{_datadir}/%{name}
