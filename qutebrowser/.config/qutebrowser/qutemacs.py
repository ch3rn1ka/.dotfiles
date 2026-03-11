# emacs-like binds for qutebrowser by Kaligule <code@schauderbasis.de>
#
# Taken from https://gitlab.com/Kaligule/qutebrowser-emacs-config/blob/master/config.py
# and slightly modified since the command naming is different now

config.unbind("<Ctrl-x>")
config.unbind("<Ctrl-u>")

config.bind("<Ctrl-x><Ctrl-l>", "config-source")

config.bind("<Ctrl-e>", "edit-text", mode="insert")
config.bind("<Ctrl-g>", "mode-leave", mode="insert")

# note: it's impossible to bind Alt-Shift-, and Alt-Shift-.
# because the < and > characters are reserved for bind syntax
# and you can't even escape them
config.bind("<Alt-,>", "scroll-to-perc 0")
config.bind("<Alt-.>", "scroll-to-perc")

config.bind("<Ctrl-g>", "fake-key --global <Escape>")
config.bind("n", "fake-key <Down>")
config.bind("p", "fake-key <Up>")

config.bind("<Ctrl-b>", "scroll-px -100 0")
config.bind("<Ctrl-n>", "scroll-px 0 100")
config.bind("<Ctrl-p>", "scroll-px 0 -100")
config.bind("<Ctrl-f>", "scroll-px 0 100")
config.bind("<Ctrl-a>", "back")
config.bind("<Ctrl-e>", "forward")

config.bind("<Ctrl-u><Ctrl-x><Ctrl-f>", "cmd-set-text -s :open -t")
config.bind("<Ctrl-x><Ctrl-f>", "cmd-set-text -s :open")
config.bind("<Ctrl-x><Ctrl-c>", "quit")
config.bind("<Ctrl-x>z", "cmd-repeat-last")
config.bind("<Ctrl-x>l", "reload")

config.bind("<Ctrl-m>", "mode-enter insert")

config.bind("<Ctrl-Space>", "mode-enter caret")
config.bind("<Ctrl-e>", "move-to-end-of-line", mode="caret")
config.bind("<Ctrl-a>", "move-to-start-of-line", mode="caret")
config.bind("<Ctrl-n>", "move-to-next-line", mode="caret")
config.bind("<Ctrl-p>", "move-to-prev-line", mode="caret")
config.bind("<Alt-f>", "move-to-end-of-word", mode="caret")
config.bind("<Alt-b>", "move-to-prev-word", mode="caret")
config.bind("<Ctrl-b>", "move-to-prev-char", mode="caret")
config.bind("<Ctrl-f>", "move-to-next-char", mode="caret")
config.bind("<Alt-a>", "move-to-start-of-prev-block", mode="caret")
config.bind("<Alt-e>", "move-to-end-of-next-block", mode="caret")
config.bind("<Alt-.>", "move-to-end-of-document", mode="caret")
config.bind("<Alt-,>", "move-to-start-of-document", mode="caret")

config.bind("<Ctrl-x>r ", "mode-enter set_mark")
config.bind("<Ctrl-x>rj", "mode-enter jump_mark")

config.bind("<Ctrl-/>", "undo")
config.bind("<Ctrl-u><Ctrl-/>", "undo --window")

config.bind("<Ctrl-x><Ctrl-b>", "tab-select")
config.bind("<Ctrl-x>b", "cmd-set-text -s :tab-select")
config.bind("<Ctrl-x>k", "tab-close")
config.bind("<Ctrl-x>0", "tab-close")
config.bind("<Ctrl-x>1", "tab-only")
config.bind("<Ctrl-x>o", "tab-next")
config.bind("<Alt-a>", "tab-prev")
config.bind("<Alt-e>", "tab-next")
config.bind("<Ctrl-Alt-a>", "tab-move -")
config.bind("<Ctrl-Alt-e>", "tab-move +")

config.bind("<Ctrl-s>", "cmd-set-text /")
config.bind("<Ctrl-r>", "cmd-set-text ?")
config.bind("<Ctrl-s>", "search-next", mode="command")
config.bind("<Ctrl-r>", "search-prev", mode="command")

config.bind("+", "zoom-in")
config.bind("-", "zoom-out")

config.bind("<Alt-x>", "cmd-set-text :")
config.bind("<Up>", "command-history-prev", mode="command")
config.bind("<Ctrl-p>", "command-history-prev", mode="command")
config.bind("<Down>", "command-history-next", mode="command")
config.bind("<Ctrl-n>", "command-history-next", mode="command")
config.bind("<Return>", "command-accept", mode="command")
config.bind("<Ctrl-m>", "command-accept", mode="command")
config.bind("<Shift-Tab>", "completion-item-focus prev", mode="command")
config.bind("<Ctrl-p>", "completion-item-focus prev", mode="command")
config.bind("<Tab>", "completion-item-focus next", mode="command")
config.bind("<Ctrl-n>", "completion-item-focus next", mode="command")
config.bind("<Escape>", "mode-leave", mode="command")
config.bind("<Ctrl-g>", "mode-leave", mode="command")

config.bind("<Ctrl-w>", "hint")
config.bind("<Ctrl-u><Ctrl-w>", "hint --rapid links tab-bg")
config.bind("<Ctrl-B>", "hint all tab-bg", mode="hint")
config.bind("<Ctrl-F>", "hint links", mode="hint")
config.bind("<Return>", "follow-hint", mode="hint")
config.bind("<Ctrl-m>", "follow-hint", mode="hint")
config.bind("<Escape>", "mode-leave", mode="hint")
config.bind("<Ctrl-g>", "mode-leave", mode="hint")

config.bind("<Ctrl-g>", "mode-leave", mode="passthrough")

config.bind("<Alt-w>", "yank")
config.bind("<Ctrl-u><Alt-w>d", "yank domain")
config.bind("<Ctrl-u><Alt-w>p", "yank pretty-url")
config.bind("<Ctrl-u><Alt-w>t", "yank title")

config.bind("<Ctrl-x>c", "config-cycle colors.webpage.darkmode.enabled true false")

config.bind("<Ctrl-x><Ctrl-m>", "spawn mpv {url}")
config.bind("<Ctrl-u><Ctrl-x><Ctrl-m>", "hint links spawn mpv {hint-url}")
