# Emacs-like binds for qutebrowser by Alex Chernika <me@chernika.dev>
#
# Originally based on:
# qutebrowser-emacs-config by @Kaligule

import re

us='qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./' + '`1234567890-=~!@#$%^&*()_+'
ru='йцукенгшщзхъ\\фывапролджэячсмитьбю.' + 'ё1234567890-=!Ё"№;%:?*()_+'

lookup = {}
for i in range(len(us)):
    lookup[us[i]] = ru[i]
    lookup[us[i].upper()] = ru[i].upper()

keywords = ['Ctrl', 'Control', 'Alt', 'Mod1', 'Meta', 'Windows', 'Mod4',
            'Shift', 'Tab', 'Down', 'Up', 'Left', 'Right', 'Space', 'Return',
            'Enter', 'Backspace', 'Delete', 'Escape', 'Home', 'End', '<', '>']

def translate(word):
    """
    Translate an English word to its Russian cross-layout equivalent
    using the US/RU translation table.
    """

    if word in keywords: return word
    res = ''
    for letter in word:
        res += lookup.get(letter, letter)
    return res

def config_bind_multilang(keybind, cmd, mode='normal'):
    """
    Given `keybind` in English, bind it to `cmd` in the `mode` mode,
    and mirror it for the Russian layout.
    """

    parts = re.split(r'(<|-|>)', keybind)
    translated_keybind = ''
    for part in parts:
        translated_keybind += translate(part)

    config.bind(keybind, cmd, mode)
    config.bind(translated_keybind, cmd, mode)

# Unbind everything
c.bindings.default = {}

### Normal mode
config_bind_multilang('<Ctrl-x><Ctrl-l>', 'config-source')
config_bind_multilang('<Ctrl-g>', 'fake-key --global <Escape>')

config_bind_multilang('<Ctrl-b>', 'scroll-px -100 0')
config_bind_multilang('<Ctrl-n>', 'scroll-px 0 100')
config_bind_multilang('<Ctrl-p>', 'scroll-px 0 -100')
config_bind_multilang('<Ctrl-f>', 'scroll-px 0 100')
config_bind_multilang('<Ctrl-a>', 'back')
config_bind_multilang('<Ctrl-e>', 'forward')

config_bind_multilang('n', 'fake-key <Down>')
config_bind_multilang('p', 'fake-key <Up>')

config_bind_multilang('<Ctrl-/>', 'undo')
config_bind_multilang('<Ctrl-u><Ctrl-/>', 'undo --window')

# Note: it's impossible to bind Alt-< or Alt-> because the '<' and '>'
# characters are reserved for bind syntax, and you can't even escape them.
config_bind_multilang('<Alt-,>', 'scroll-to-perc 0')
config_bind_multilang('<Alt-.>', 'scroll-to-perc')

config_bind_multilang('<Ctrl-x><Ctrl-f>', 'cmd-set-text -s :open')
config_bind_multilang('<Ctrl-x>4<Ctrl-f>', 'cmd-set-text -s :open -b')
config_bind_multilang('<Ctrl-x>5<Ctrl-f>', 'cmd-set-text -s :open -w')
config_bind_multilang('<Ctrl-x>6<Ctrl-f>', 'cmd-set-text -s :open -p')
config_bind_multilang('<Ctrl-u><Ctrl-x><Ctrl-f>', 'cmd-set-text -s :open -t')
config_bind_multilang('<Ctrl-x><Ctrl-c>', 'quit')
config_bind_multilang('<Ctrl-x>z', 'cmd-repeat-last')
config_bind_multilang('<Ctrl-x>l', 'reload')

config_bind_multilang('<Ctrl-x><Ctrl-b>', 'tab-select')
config_bind_multilang('<Ctrl-x>b', 'cmd-set-text -s :tab-select')
config_bind_multilang('<Ctrl-x>k', 'tab-close')
config_bind_multilang('<Ctrl-x>0', 'tab-close')
config_bind_multilang('<Ctrl-x>1', 'tab-only')
config_bind_multilang('<Ctrl-x>o', 'tab-next')
config_bind_multilang('<Alt-a>', 'tab-prev')
config_bind_multilang('<Alt-e>', 'tab-next')
config_bind_multilang('<Ctrl-Alt-a>', 'tab-move -')
config_bind_multilang('<Ctrl-Alt-e>', 'tab-move +')

config_bind_multilang('<Ctrl-s>', 'cmd-set-text /')
config_bind_multilang('<Ctrl-r>', 'cmd-set-text ?')

config_bind_multilang('+', 'zoom-in')
config_bind_multilang('-', 'zoom-out')

config_bind_multilang('<Alt-w>', 'yank url')
config_bind_multilang('<Ctrl-c>cs', 'yank selection --sel')
config_bind_multilang('<Ctrl-c>cd', 'yank domain')
config_bind_multilang('<Ctrl-c>cp', 'yank pretty-url')
config_bind_multilang('<Ctrl-c>ct', 'yank title')

config_bind_multilang('<Ctrl-x>c',
                      'config-cycle colors.webpage.darkmode.enabled true false')

config_bind_multilang('<Ctrl-c>mu', 'spawn mpv {url}')
config_bind_multilang('<Ctrl-c>mh', 'hint links spawn mpv {hint-url}')

config_bind_multilang('<Ctrl-c>dr', 'download-remove')
config_bind_multilang('<Ctrl-c>dR', 'download-clear')
config_bind_multilang('<Ctrl-c>dc', 'download-cancel')
config_bind_multilang('<Ctrl-c>do', 'download-open')
config_bind_multilang('<Ctrl-c>dd', 'download-delete')
config_bind_multilang('<Ctrl-c>dr', 'download-retry')

### Insert mode
config_bind_multilang('<Ctrl-m>', 'mode-enter insert')
config_bind_multilang('<Ctrl-g>', 'mode-leave', mode='insert')
config_bind_multilang('<Escape>', 'mode-leave', mode='insert')

config_bind_multilang('<Alt-w>', 'yank selection --sel', mode='insert')
config_bind_multilang('<Ctrl-w>', 'yank selection --sel ;; fake-key <Ctrl-x>', mode='insert')
config_bind_multilang('<Ctrl-y>', 'fake-key <Ctrl-v>', mode='insert')
config_bind_multilang('<Ctrl-/>', 'fake-key <Ctrl-z>', mode='insert')
config_bind_multilang('<Alt-Backspace>',
                      'fake-key <Ctrl-Backspace>', mode='insert')
config_bind_multilang('<Alt-d>', 'fake-key <Ctrl-Delete>', mode='insert')
config_bind_multilang('<Ctrl-k>', 'fake-key <Shift-End><Delete>', mode='insert')
config_bind_multilang('<Ctrl-x><Ctrl-p>',
                      'fake-key <Ctrl-Home><Ctrl-Shift-End>', mode='insert')

# This doesn't behave *exactly* like C-S-<backspace> in Emacs since it would
# trip on empty lines otherwise. It's basically like pressing C-a C-k.
config_bind_multilang('<Ctrl-Shift-Backspace>',
                      'fake-key <Home><Home><Shift-End><Delete>', mode='insert')

config_bind_multilang('<Ctrl-Alt-Space>',
                      'fake-key <Ctrl-Shift-Right>', mode='insert')
config_bind_multilang('<Ctrl-h>', 'edit-text', mode='insert')

config_bind_multilang('<Ctrl-e>', 'fake-key <End><End>', mode='insert')
config_bind_multilang('<Ctrl-a>', 'fake-key <Home><Home>', mode='insert')
config_bind_multilang('<Ctrl-n>', 'fake-key <Down>', mode='insert')
config_bind_multilang('<Ctrl-p>', 'fake-key <Up>', mode='insert')
config_bind_multilang('<Ctrl-d>', 'fake-key <Delete>', mode='insert')
config_bind_multilang('<Alt-f>', 'fake-key <Ctrl-Right>', mode='insert')
config_bind_multilang('<Alt-b>', 'fake-key <Ctrl-Left>', mode='insert')
config_bind_multilang('<Ctrl-f>', 'fake-key <Right>', mode='insert')
config_bind_multilang('<Ctrl-b>', 'fake-key <Left>', mode='insert')
config_bind_multilang('<Alt-.>', 'fake-key <Ctrl-End>', mode='insert')
config_bind_multilang('<Alt-,>', 'fake-key <Ctrl-Home>', mode='insert')

# Since there are no marks in texboxes, I'm forced to use these awkward binds
# to continiously select text (I wonder if nyxt can do it any better)
config_bind_multilang('<Ctrl-Shift-e>', 'fake-key <Shift-End>', mode='insert')
config_bind_multilang('<Ctrl-Shift-a>', 'fake-key <Shift-Home>', mode='insert')
config_bind_multilang('<Alt-Shift-f>',
                      'fake-key <Ctrl-Shift-Right>', mode='insert')
config_bind_multilang('<Alt-Shift-b>',
                      'fake-key <Ctrl-Shift-Left>', mode='insert')
config_bind_multilang('<Ctrl-Shift-n>', 'fake-key <Shift-Down>', mode='insert')
config_bind_multilang('<Ctrl-Shift-b>', 'fake-key <Shift-Left>', mode='insert')
config_bind_multilang('<Ctrl-Shift-f>', 'fake-key <Shift-Right>', mode='insert')
config_bind_multilang('<Ctrl-Shift-p>', 'fake-key <Shift-Up>', mode='insert')
config_bind_multilang('<Alt-Ctrl-.>',
                      'fake-key <Ctrl-Shift-End>', mode='insert')
config_bind_multilang('<Alt-Ctrl-,>',
                      'fake-key <Ctrl-Shift-Home>', mode='insert')

### Caret mode
config_bind_multilang('<Ctrl-Space>', 'mode-enter caret')
config_bind_multilang('<Ctrl-g>', 'mode-leave', mode='caret')
config_bind_multilang('<Escape>', 'mode-leave', mode='caret')

config_bind_multilang('<Ctrl-e>', 'move-to-end-of-line', mode='caret')
config_bind_multilang('<Ctrl-a>', 'move-to-start-of-line', mode='caret')
config_bind_multilang('<Ctrl-n>', 'move-to-next-line', mode='caret')
config_bind_multilang('<Ctrl-p>', 'move-to-prev-line', mode='caret')
config_bind_multilang('<Alt-f>', 'move-to-end-of-word', mode='caret')
config_bind_multilang('<Alt-b>', 'move-to-prev-word', mode='caret')
config_bind_multilang('<Ctrl-f>', 'move-to-next-char', mode='caret')
config_bind_multilang('<Ctrl-b>', 'move-to-prev-char', mode='caret')
config_bind_multilang('<Alt-a>', 'move-to-start-of-prev-block', mode='caret')
config_bind_multilang('<Alt-e>', 'move-to-end-of-next-block', mode='caret')
config_bind_multilang('<Alt-.>', 'move-to-end-of-document', mode='caret')
config_bind_multilang('<Alt-,>', 'move-to-start-of-document', mode='caret')

### *mark modes
config_bind_multilang('<Ctrl-x>r ', 'mode-enter set_mark')
config_bind_multilang('<Ctrl-x>rj', 'mode-enter jump_mark')

### Command mode
config_bind_multilang('<Alt-x>', 'cmd-set-text :')
config_bind_multilang('<Ctrl-g>', 'mode-leave', mode='command')
config_bind_multilang('<Escape>', 'mode-leave', mode='command')

config_bind_multilang('<Up>', 'command-history-prev', mode='command')
config_bind_multilang('<Ctrl-p>', 'command-history-prev', mode='command')
config_bind_multilang('<Down>', 'command-history-next', mode='command')
config_bind_multilang('<Ctrl-n>', 'command-history-next', mode='command')
config_bind_multilang('<Return>', 'command-accept', mode='command')
config_bind_multilang('<Ctrl-m>', 'command-accept', mode='command')
config_bind_multilang('<Shift-Tab>',
                      'completion-item-focus prev', mode='command')
config_bind_multilang('<Ctrl-p>', 'completion-item-focus prev', mode='command')
config_bind_multilang('<Tab>', 'completion-item-focus next', mode='command')
config_bind_multilang('<Ctrl-n>', 'completion-item-focus next', mode='command')

config_bind_multilang('<Ctrl-s>', 'search-next', mode='command')
config_bind_multilang('<Ctrl-r>', 'search-prev', mode='command')

config_bind_multilang('<Ctrl-b>', 'rl-backward-char', mode='command')
config_bind_multilang('<Ctrl-f>', 'rl-forward-char', mode='command')
config_bind_multilang('<Alt-b>',  'rl-backward-word', mode='command')
config_bind_multilang('<Alt-f>',  'rl-forward-word', mode='command')
config_bind_multilang('<Alt-Backspace>', 'rl-backward-kill-word', mode='command')
config_bind_multilang('<Alt-d>',  'rl-kill-word', mode='command')
config_bind_multilang('<Ctrl-k>',  'rl-kill-line', mode='command')
config_bind_multilang('<Ctrl-a>',  'rl-beginning-of-line', mode='command')
config_bind_multilang('<Ctrl-e>',  'rl-end-of-line', mode='command')

config_bind_multilang('<Ctrl-y>', 'fake-key --global <Ctrl-v>', mode='command')

### Hint mode
config_bind_multilang('<Ctrl-w>', 'hint')
config_bind_multilang('<Ctrl-g>', 'mode-leave', mode='hint')
config_bind_multilang('<Escape>', 'mode-leave', mode='hint')

config_bind_multilang('<Ctrl-u><Ctrl-w>', 'hint --rapid')
config_bind_multilang('<Ctrl-B>', 'hint all tab-bg', mode='hint')
config_bind_multilang('<Ctrl-F>', 'hint links', mode='hint')
config_bind_multilang('<Return>', 'follow-hint', mode='hint')
config_bind_multilang('<Ctrl-m>', 'follow-hint', mode='hint')

### Passthrough mode
config_bind_multilang('<Ctrl-g>', 'mode-leave', mode='passthrough')
config_bind_multilang('<Escape>', 'mode-leave', mode='passthrough')
