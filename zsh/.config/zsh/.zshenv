export XDG_CONFIG_HOME="$HOME/.config"
export XDG_CACHE_HOME="$HOME/.cache"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_STATE_HOME="$HOME/.local/state"
export XDG_BIN_HOME="$HOME/.local/bin"

export EDITOR="nvim"
export VISUAL="nvim"
export PDFREADER="emacsclient -c -a ''"
export BROWSER='qutebrowser'

export PATH="$PATH:$XDG_BIN_HOME"
export DOTFILES="$HOME/.dotfiles"
export WINEPREFIX="$XDG_DATA_HOME/wine"
export GTK2_RC_FILES="$XDG_CONFIG_HOME/gtkrc-2.0"
export GNUPGHOME="$XDG_DATA_HOME/gnupg"
export PASSWORD_STORE_DIR="$XDG_DATA_HOME/pass"
export PASSWORD_STORE_CLIP_TIME=5
export PYTHON_HISTORY="$XDG_STATE_HOME/python_history"
export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket"
export OPAMROOT="$XDG_DATA_HOME/opam"
export GHCUP_USE_XDG_DIRS=1
export STACK_XDG=1

export BEMENU_OPTS="
--fn \"UbuntuMono Nerd Font 14\" \
--list 14 \
--ignorecase \
--line-height 26 \
--ch 22 --cw 10 \
--scrollbar always \
--scb #3c3836 --scf #fabd2f \
--bdr #3c3836 --border 1 \
--tb #282828 --tf #ebdbb2 \
--fb #3c3836 --ff #ebdbb2 \
--nb #282828 --nf #ebdbb2 \
--hb #7c6f64 --hf #fbf1c7 \
--ab #665c54 --af #ebdbb2 \
--sb #504945 --sf #fbf1c7 \
--cb #282828 --cf #ebdbb2 \
--nb #504945 --nf #ebdbb2
"
