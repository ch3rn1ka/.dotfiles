vim.pack.add({
    { src = "https://github.com/ellisonleao/gruvbox.nvim.git" },
    { src = "https://github.com/nvim-tree/nvim-web-devicons.git" },
    { src = "https://github.com/stevearc/oil.nvim.git" },
    { src = "https://github.com/ibhagwan/fzf-lua.git" },
    { src = "https://github.com/folke/which-key.nvim.git" },
    { src = "https://github.com/NMAC427/guess-indent.nvim.git" }
})

require("oil").setup()
require("guess-indent").setup()
require("which-key").setup({ delay = 1000 })
require("fzf-lua").setup({
    files = {
        fd_opts = [[--hidden --type f --exclude ".git"]],
        follow = true
    },
    fzf_colors = {
        ["pointer"] = "#b16286",
    }
})

vim.cmd("colorscheme gruvbox")
