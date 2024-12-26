Name:           openqa-client-completion
Version:        1.0
Release:        0
Summary:        The official auto-completion script for openqa-cli.
License:        GPL-2.0-or-later
Url:            
Requires:       openQA-client

%package client-bash-completion
￼Summary:        Bash Completion for %{name}
￼Requires:       bash-completion
￼Supplements:    (%{name}-client and bash)
￼
￼%description client-bash-completion
￼The official bash completion script for openqa-cli.
￼
￼%package client-zsh-completion
￼Summary:        Zsh Completion for %{name}
￼Supplements:    (%{name}-client and zsh)
￼
￼%description client-zsh-completion
￼The official zsh completion script for openqa-cli.

%prep
%setup -q

%build

%install
# completion
￼install -Dm 0644 contrib/completions/openqa-cli-completion.bash %{buildroot}%{_datadir}/bash-completion/completions/openqa-cli
￼install -Dm 0644 contrib/completions/openqa-cli-completion.zsh %{buildroot}%{_datadir}/zsh/site-functions/_openqa-cli

%files client-bash-completion
%{_datadir}/bash-completion/completions/openqa-cli
%files client-zsh-completion
%{_datadir}/zsh/site-functions/_openqa-cli

%changelog
