[ ! -s $XDG_RUNTIME_DIR/mpd/mpd.pid ] &&
    mpd >/dev/null 2>&1 && mpc -q repeat on

# if [ "$(tty)" = "/dev/tty1" ]; then
#     if uwsm check may-start; then
#         exec uwsm start labwc.desktop
#     fi
# fi
