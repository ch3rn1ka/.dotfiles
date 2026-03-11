playerctld daemon >/dev/null 2>&1

[ ! -s $XDG_RUNTIME_DIR/mpd/mpd.pid ] &&
    mpd >/dev/null 2>&1 && {
        (mpdris2-rs >/dev/null 2>&1 &)
        mpc -q repeat on
    }
