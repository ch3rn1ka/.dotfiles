import os

config.load_autoconfig()

c.window.title_format = "qutebrowser"
c.fonts.default_family = "UbuntuMono Nerd Font"
c.fonts.default_size = "18pt"

c.editor.command = ["emacsclient", "-c", "-a ''", "{file}"]

c.url.default_page = "~/.config/qutebrowser/startpage.html"
c.url.start_pages = ["~/.config/qutebrowser/startpage.html"]
c.url.searchengines = { "DEFAULT":  "https://www.duckduckgo.com/lite/?q={}" }

c.content.blocking.method = "both"
c.content.javascript.enabled = False

# Add something like https://*.youtube.com/* to js_whitelist.txt to enable
# JavaScript on that website. Won't recommend it though.
js_whitelist_path = os.path.join(config.configdir, "js_whitelist.txt")
if os.path.exists(js_whitelist_path):
    with open(js_whitelist_path, 'r') as f:
        for line in f:
            pattern = line.strip()
            if pattern and not pattern.startswith('#'):
                config.set("content.javascript.enabled", True, pattern)

config.source("qutemacs.py")
config.source("gruvbox.py")
