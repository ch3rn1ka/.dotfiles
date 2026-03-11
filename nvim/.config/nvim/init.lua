vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.smarttab = true
vim.opt.autoindent = false
vim.opt.expandtab = true
vim.opt.swapfile = false
vim.opt.cursorline = true
vim.opt.autochdir = true
vim.opt.wrap = false
vim.opt.laststatus = 3
vim.opt.termguicolors = true
vim.g.mapleader = " "

require("plugins")
require("autocmds")
require("binds")
