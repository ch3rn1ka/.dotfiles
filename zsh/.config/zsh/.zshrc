setopt share_history
setopt extendedglob
setopt NO_CASE_GLOB

HISTFILE="$XDG_STATE_HOME/zsh_history"
HISTSIZE=5000
SAVEHIST=5000

export LESS='-R --use-color -Dd+c$Du+b$'
export MANROFFOPT='-P -c'
export GPG_TTY=$(tty)

alias ls='ls --color=auto'
alias ll='ls -lAh --color=auto --sort=extension --group-directories-first'
alias ec="TERM=xterm-direct emacsclient -nw -a ''"
alias wget="wget --hsts-file $XDG_STATE_HOME/wget_hosts"
alias ghci="ghci -ghci-script $XDG_CONFIG_HOME/ghci"
alias tmux='tmux -T 256'

[ "$TERM" = "linux" ] ||
    PROMPT='%B%F{10}[I]%f%b %F{15}[%F{12}%n%F{15}@%F{11}%m%F{15}]%F{9}[%~]%f$ '

bindkey -e
bindkey "^[p" up-line-or-search
bindkey "^[n" down-line-or-search

# completion
autoload -Uz compinit
compinit -C -d "$XDG_CACHE_HOME/zsh_zcompdump"
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}' \
       'r:|[._-]=* r:|=*' 'l:|=* r:|=*'

# zsh-syntax-highlighting
(( ${+ZSH_HIGHLIGHT_STYLES} )) || typeset -A ZSH_HIGHLIGHT_STYLES
ZSH_HIGHLIGHT_STYLES[path]=none
ZSH_HIGHLIGHT_STYLES[path_prefix]=none
ZSH_HIGHLIGHT_STYLES[unknown-token]='fg=#fb4934'

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

# eat-shell integration
[ -n "$EAT_SHELL_INTEGRATION_DIR" ] &&
    source "$EAT_SHELL_INTEGRATION_DIR/zsh"

# ocaml package manager
OPAM_INIT="$OPAMROOT/opam-init/init.zsh"
[[ ! -r "$OPAM_INIT" ]] || source "$OPAM_INIT"

# haskell installer
GHCUP_ENV="$XDG_DATA_DIR/ghcup/env"
[[ ! -r "$GHCUP_ENV" ]] || source "$GHCUP_ENV"
