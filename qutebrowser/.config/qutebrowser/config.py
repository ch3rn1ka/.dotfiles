config.load_autoconfig()

c.window.title_format = "qutebrowser"
c.fonts.default_family = "UbuntuMono Nerd Font"
c.fonts.default_size = "18pt"

c.editor.command = ["emacsclient", "-c", "-a ''", "{file}"]

c.url.default_page = "~/.config/qutebrowser/startpage.html"
c.url.start_pages = ["~/.config/qutebrowser/startpage.html"]
c.url.searchengines = {
    "DEFAULT":  "https://google.com/search?hl=en&q={}",
}

c.content.blocking.method = "both"

config.source("qutemacs.py") # keybinds
config.source("gruvbox.py") # colorscheme
