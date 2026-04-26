import os

config.load_autoconfig()

c.window.title_format = 'qutebrowser'
c.fonts.default_family = 'UbuntuMono Nerd Font'
c.fonts.default_size = '18pt'

c.editor.command = ['emacsclient', '-c', "-a ''", '{file}']

c.url.default_page = '~/.config/qutebrowser/startpage.html'
c.url.start_pages = ['~/.config/qutebrowser/startpage.html']
c.url.searchengines = { 'DEFAULT': 'https://www.duckduckgo.com/lite/?q={}' }

c.content.blocking.method = 'both'
c.content.headers.referer = 'same-domain'
c.content.cookies.accept = 'no-3rdparty'
c.content.javascript.enabled = True

config.source('qutemacs.py')
config.source('gruvbox.py')
