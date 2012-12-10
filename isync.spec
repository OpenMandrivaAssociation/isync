Summary:	Utility to synchronize IMAP mailboxes with local maildir folders
Name:		isync
Version:	1.0.5
Release:	1
License:	GPLv2
Group:		Networking/Mail
URL:		http://isync.sf.net/
Source0:	http://prdownloads.sourceforge.net/isync/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig
BuildRequires:	openssl-devel
BuildRequires:	db-devel
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



%changelog
* Tue May 08 2012 Crispin Boylan <crisb@mandriva.org> 1.0.5-1
+ Revision: 797497
- New release

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-3mdv2011.0
+ Revision: 612422
- the mass rebuild of 2010.1 packages

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 1.0.4-2mdv2010.1
+ Revision: 537329
- rebuild

* Tue Feb 16 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.0.4-1mdv2010.1
+ Revision: 506849
- fix licence and update to 1.0.4

* Tue Jan 12 2010 Buchan Milne <bgmilne@mandriva.org> 1.0.3-5mdv2010.1
+ Revision: 490369
- Rebuild for db-4.8

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0.3-4mdv2010.0
+ Revision: 429575
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-3mdv2009.0
+ Revision: 247315
- rebuild

* Fri Jan 04 2008 Jérôme Soyer <saispo@mandriva.org> 1.0.3-1mdv2008.1
+ Revision: 144989
- New release

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 14 2007 Thierry Vignaud <tv@mandriva.org> 1.0.2-2mdv2008.1
+ Revision: 119832
- rebuild b/c of missing package on ia32
- import isync

