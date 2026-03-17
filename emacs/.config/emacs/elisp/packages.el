;;; packages.el -- configuration for built-in and (m)elpa packages
;; for general configuration, check config.el

(require 'package)
(require 'use-package)

(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)

(unless package-archive-contents
  (package-refresh-contents))

;;; External packages
(setq use-package-always-ensure t)

(use-package rainbow-delimiters
  :hook (prog-mode . rainbow-delimiters-mode))

(use-package pdf-tools
  :config
  (pdf-loader-install)
  ;; silence non-critical warnings
  (with-eval-after-load 'pdf-cache
    (advice-add 'pdf-cache--prefetch-start
                :around
                (lambda (old-fun &rest args)
                  (ignore-errors
                    (apply old-fun args))))))

(use-package eshell-syntax-highlighting
  :hook (eshell-mode . eshell-syntax-highlighting-mode))

(use-package eat
  :ensure t
  :hook
  (eshell-load . eat-eshell-mode)
  (eshell-load . eat-eshell-visual-command-mode)
  :config
  (defun rc/set-eat-gruvbox-dark-colors ()
    (set-face-attribute 'eat-term-color-black nil :foreground "#282828")
    (set-face-attribute 'eat-term-color-red nil :foreground "#cc241d")
    (set-face-attribute 'eat-term-color-green nil :foreground "#98971a")
    (set-face-attribute 'eat-term-color-yellow nil :foreground "#d79921")
    (set-face-attribute 'eat-term-color-blue nil :foreground "#458588")
    (set-face-attribute 'eat-term-color-magenta nil :foreground "#b16286")
    (set-face-attribute 'eat-term-color-cyan nil :foreground "#689d6a")
    (set-face-attribute 'eat-term-color-white nil :foreground "#a89984")

    (set-face-attribute 'eat-term-color-bright-black nil :foreground "#928374")
    (set-face-attribute 'eat-term-color-bright-red nil :foreground "#fb4934")
    (set-face-attribute 'eat-term-color-bright-green nil :foreground "#b8bb26")
    (set-face-attribute 'eat-term-color-bright-yellow nil :foreground "#fabd2f")
    (set-face-attribute 'eat-term-color-bright-blue nil :foreground "#83a598")
    (set-face-attribute 'eat-term-color-bright-magenta nil :foreground "#d3869b")
    (set-face-attribute 'eat-term-color-bright-cyan nil :foreground "#8ec07c")
    (set-face-attribute 'eat-term-color-bright-white nil :foreground "#ebdbb2"))

  (rc/set-eat-gruvbox-dark-colors))

(use-package vterm
  :ensure t
  :custom-face
  (vterm-color-black ((t :foreground "#282828" :background "#282828")))
  (vterm-color-red ((t :foreground "#cc241d" :background "#cc241d")))
  (vterm-color-green ((t :foreground "#98971a" :background "#98971a")))
  (vterm-color-yellow ((t :foreground "#d79921" :background "#d79921")))
  (vterm-color-blue ((t :foreground "#458588" :background "#458588")))
  (vterm-color-magenta ((t :foreground "#b16286" :background "#b16286")))
  (vterm-color-cyan ((t :foreground "#689d6a" :background "#689d6a")))
  (vterm-color-white ((t :foreground "#a89984" :background "#a89984")))

  (vterm-color-bright-black ((t :foreground "#928374" :background "#928374")))
  (vterm-color-bright-red ((t :foreground "#fb4934" :background "#fb4934")))
  (vterm-color-bright-green ((t :foreground "#b8bb26" :background "#b8bb26")))
  (vterm-color-bright-yellow ((t :foreground "#fabd2f" :background "#fabd2f")))
  (vterm-color-bright-blue ((t :foreground "#83a598" :background "#83a598")))
  (vterm-color-bright-magenta ((t :foreground "#d3869b" :background "#d3869b")))
  (vterm-color-bright-cyan ((t :foreground "#8ec07c" :background "#8ec07c")))
  (vterm-color-bright-white ((t :foreground "#ebdbb2" :background "#ebdbb2"))))

(use-package magit)

(use-package lua-mode
  :custom
  (indent-tabs-mode nil)
  (lua-indent-level 4)
  (lua-indent-close-paren-align nil)
  (lua-indent-nested-block-content-align nil)
  :config
  (advice-add 'lua-calculate-indentation-block-modifier
              :around
              (lambda (old-fun &rest args)
              (let ((old-res (apply old-fun args)))
                (if (> old-res lua-indent-level)
                    lua-indent-level
                  old-res)))))

(use-package haskell-mode)
(use-package tuareg)

(use-package doom-themes
  :ensure t
  :custom
  (doom-themes-enable-bold t)
  (doom-themes-enable-italic t)
  :config
  (load-theme 'doom-gruvbox t)

  (doom-themes-visual-bell-config)
  (doom-themes-org-config))

;;; Built-ins
(setq use-package-always-ensure nil)

(use-package recentf
  :bind ("C-x C-r" . recentf-open-files)
  :custom (recentf-max-menu-items 25)
  :init (recentf-mode 1))

(use-package dired
  :custom
  (dired-listing-switches "-ABhl --sort=extension --group-directories-first")
  (dired-dwim-target t)
  (dired-kill-when-opening-new-dired-buffer t))

(use-package ido
  :init (ido-mode 1)
  :custom
  (ido-enable-flex-matching t)
  (ido-use-virtual-buffers t)
  (ido-everywhere t)
  (read-file-name-completion-ignore-case t))

(use-package eshell
  :custom
  (eshell-directory-name (expand-file-name "eshell/" (or (getenv "XDG_CONFIG_HOME") "~/.config")))
  (eshell-history-file-name (expand-file-name "eshell_history" (or (getenv "XDG_STATE_HOME") "~/.local/state"))))

(use-package whitespace
  :bind ("C-c w" . whitespace-mode)
  :custom (whitespace-line-column 80))

(use-package man
  :config
  (set-face-attribute 'Man-overstrike nil :inherit font-lock-type-face :bold t)
  (set-face-attribute 'Man-underline nil :inherit font-lock-keyword-face :underline t))

(use-package cc-mode
  :custom (c-default-style "gnu"))

(use-package which-key
  :init (which-key-mode 1))

(provide 'packages)
