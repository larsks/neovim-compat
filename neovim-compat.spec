Name: neovim-compat
Version: 0.1.0
Release:        1%{?dist}
Summary: Provide vim symlink for neovim users
BuildArch: noarch

License: GPL
URL: http://github.com/larsks/neovim-compat

Requires: neovim
Conflicts: vim-enhanced

%description
Provide vim symlink for neovim users

%prep


%build


%install
install -m 755 -d %{buildroot}%{_bindir}
ln -s nvim %{buildroot}%{_bindir}/vim

%check


%files
%{_bindir}/vim

%changelog
* Tue Feb 07 2023 Lars Kellogg-Stedman <lars@oddbit.com> - 0.1.0
- Initial build
