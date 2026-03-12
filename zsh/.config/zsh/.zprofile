[ ! -s $XDG_RUNTIME_DIR/mpd/mpd.pid ] &&
    mpd >/dev/null 2>&1 && mpc -q repeat on
