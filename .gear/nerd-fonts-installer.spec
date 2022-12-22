%define binname nerd-install

Name: nerd-fonts-installer
Version: 0.4
Release: alt1

Summary: Install Nerd Fonts 
License: MIT
Group: System/Configuration/Other

Url: https://www.nerdfonts.com
Source: %name-%version.tar

BuildArch: noarch

%description
Nerd Fonts installer

%prep
%setup -q

%install
mkdir -p %buildroot%_bindir
cp install.sh %buildroot%_bindir/%binname

%files
%doc LICENSE
%_bindir/%binname


%changelog
* Thu Dec 22 2022 fl0pp5 <fl0pp5@altlinux.org>
- Initial build for ALT
