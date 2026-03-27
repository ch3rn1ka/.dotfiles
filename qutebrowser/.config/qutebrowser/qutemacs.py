# Emacs-like binds for qutebrowser by Alex Chernika <me@chernika.dev>
#
# Originally based on:
# qutebrowser-emacs-config by Kaligule <me@schauderbasis.de>
# (https://gitlab.com/Kaligule/qutebrowser-emacs-config/blob/master/config.py)

config.unbind("<Ctrl-x>")
config.unbind("<Ctrl-u>")

### Normal mode binds
config.bind("<Ctrl-x><Ctrl-l>", "config-source")
config.bind("<Ctrl-g>", "fake-key --global <Escape>")

config.bind("<Ctrl-b>", "scroll-px -100 0")
config.bind("<Ctrl-n>", "scroll-px 0 100")
config.bind("<Ctrl-p>", "scroll-px 0 -100")
config.bind("<Ctrl-f>", "scroll-px 0 100")
config.bind("<Ctrl-a>", "back")
config.bind("<Ctrl-e>", "forward")

config.bind("n", "fake-key <Down>")
config.bind("p", "fake-key <Up>")

config.bind("<Ctrl-/>", "undo")
config.bind("<Ctrl-u><Ctrl-/>", "undo --window")

# Note: it's impossible to bind Alt-Shift-, or Alt-Shift-. because the < and >
# characters are reserved for bind syntax, and you can't even escape them
config.bind("<Alt-,>", "scroll-to-perc 0")
config.bind("<Alt-.>", "scroll-to-perc")

config.bind("<Ctrl-x><Ctrl-f>", "cmd-set-text -s :open")
config.bind("<Ctrl-u><Ctrl-x><Ctrl-f>", "cmd-set-text -s :open -t")
config.bind("<Ctrl-x><Ctrl-c>", "quit")
config.bind("<Ctrl-x>z", "cmd-repeat-last")
config.bind("<Ctrl-x>l", "reload")

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

config.bind("<Alt-w>", "yank")
config.bind("<Ctrl-u><Alt-w>d", "yank domain")
config.bind("<Ctrl-u><Alt-w>p", "yank pretty-url")
config.bind("<Ctrl-u><Alt-w>t", "yank title")

config.bind("<Ctrl-x>c",
            "config-cycle colors.webpage.darkmode.enabled true false")

config.bind("<Ctrl-x><Ctrl-m>", "spawn mpv {url}")
config.bind("<Ctrl-u><Ctrl-x><Ctrl-m>", "hint links spawn mpv {hint-url}")

### Insert mode binds
config.bind("<Ctrl-m>", "mode-enter insert")
config.bind("<Ctrl-g>", "mode-leave", mode="insert")

config.bind("<Alt-w>", "fake-key <Ctrl-c>", mode="insert")
config.bind("<Ctrl-y>", "fake-key <Ctrl-v>", mode="insert")
config.bind("<Ctrl-/>", "fake-key <Ctrl-z>", mode="insert")
config.bind("<Alt-Backspace>", "fake-key <Ctrl-Backspace>", mode="insert")
config.bind("<Alt-d>", "fake-key <Ctrl-Delete>", mode="insert")
config.bind("<Ctrl-k>", "fake-key <Shift-End><Delete>", mode="insert")
config.bind("<Ctrl-x><Ctrl-p>", "fake-key <Ctrl-Home><Ctrl-Shift-End>", mode="insert")
config.bind("<Ctrl-Shift-Backspace>", "fake-key <Home><Shift-End><Delete>", mode="insert")
config.bind("<Ctrl-Alt-Space>", "fake-key <Ctrl-Shift-Right>", mode="insert")
config.bind("<Ctrl-h>", "edit-text", mode="insert")

config.bind("<Alt-b>", "fake-key <Ctrl-Left>", mode="insert")
config.bind("<Alt-f>", "fake-key <Ctrl-Right>", mode="insert")
config.bind("<Ctrl-b>", "fake-key <Left>", mode="insert")
config.bind("<Ctrl-n>", "fake-key <Down>", mode="insert")
config.bind("<Ctrl-p>", "fake-key <Up>", mode="insert")
config.bind("<Ctrl-f>", "fake-key <Right>", mode="insert")
config.bind("<Ctrl-a>", "fake-key <Home>", mode="insert")
config.bind("<Ctrl-e>", "fake-key <End>", mode="insert")

# Since there are no marks in texboxes, I'm forced to use these awkward binds
# to continiously select text (I wonder if nyxt can do it any better)
config.bind("<Alt-Shift-b>", "fake-key <Ctrl-Shift-Left>", mode="insert")
config.bind("<Alt-Shift-f>", "fake-key <Ctrl-Shift-Right>", mode="insert")
config.bind("<Ctrl-Shift-b>", "fake-key <Shift-Left>", mode="insert")
config.bind("<Ctrl-Shift-n>", "fake-key <Shift-Down>", mode="insert")
config.bind("<Ctrl-Shift-p>", "fake-key <Shift-Up>", mode="insert")
config.bind("<Ctrl-Shift-f>", "fake-key <Shift-Right>", mode="insert")
config.bind("<Ctrl-Shift-a>", "fake-key <Shift-Home>", mode="insert")
config.bind("<Ctrl-Shift-e>", "fake-key <Shift-End>", mode="insert")

### Caret mode binds
config.bind("<Ctrl-Space>", "mode-enter caret")
config.bind("<Ctrl-g>", "mode-leave", mode="caret")

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

### *mark modes binds
config.bind("<Ctrl-x>r ", "mode-enter set_mark")
config.bind("<Ctrl-x>rj", "mode-enter jump_mark")

### Command mode binds
config.bind("<Alt-x>", "cmd-set-text :")
config.bind("<Ctrl-g>", "mode-leave", mode="command")

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

### Hint mode binds
config.bind("<Ctrl-w>", "hint")
config.bind("<Ctrl-g>", "mode-leave", mode="hint")

config.bind("<Ctrl-u><Ctrl-w>", "hint --rapid links tab-bg")
config.bind("<Ctrl-B>", "hint all tab-bg", mode="hint")
config.bind("<Ctrl-F>", "hint links", mode="hint")
config.bind("<Return>", "follow-hint", mode="hint")
config.bind("<Ctrl-m>", "follow-hint", mode="hint")

### Passthrough mode binds
config.bind("<Ctrl-g>", "mode-leave", mode="passthrough")
