Summary:	Utility to synchronize IMAP mailboxes with local maildir folders
Name:		isync
Version:	1.0.4
Release:	%mkrel 3
License:	GPLv2
Group:		Networking/Mail
URL:		http://isync.sf.net/
Source0:	http://prdownloads.sourceforge.net/isync/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig
BuildRequires:	openssl-devel
BuildRequires:	db4-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
isync is a command line utility which synchronizes mailboxes; currently Maildir
and IMAP4 mailboxes are supported. New messages, message deletions and flag
changes can be propagated both ways. It is useful for working in disconnected
mode, such as on a laptop or with a non-permanent internet collection (dIMAP).

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}%{_datadir}/doc/isync

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README TODO ChangeLog src/mbsyncrc.sample src/compat/isyncrc.sample
%attr(0755,root,root) %{_bindir}/isync
%attr(0755,root,root) %{_bindir}/mbsync
%attr(0755,root,root) %{_bindir}/mdconvert
%attr(0755,root,root) %{_bindir}/get-cert
%attr(0644,root,root) %{_mandir}/man1/isync.1*
%attr(0644,root,root) %{_mandir}/man1/mbsync.1*
%attr(0644,root,root) %{_mandir}/man1/mdconvert.1*

