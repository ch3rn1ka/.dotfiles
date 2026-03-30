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
c.content.cookies.accept = 'never'
c.content.javascript.enabled = False

# Add something like https://*.youtube.com/* to whitelist.txt to enable
# JavaScript and save cookies on that website. Won't recommend it though.
whitelist_path = os.path.join(config.configdir, 'whitelist.txt')
if os.path.exists(whitelist_path):
    with open(whitelist_path, 'r') as f:
        for line in f:
            pattern = line.strip()
            if pattern and not pattern.startswith('#'):
                config.set('content.cookies.accept', 'all', pattern)
                config.set('content.javascript.enabled', True, pattern)

config.source('qutemacs.py')
config.source('gruvbox.py')
