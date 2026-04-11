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
  (rc/set-eat-gruvbox-dark-colors)
  :custom
  (eat-enable-shell-prompt-annotation t)
  (eat-shell-prompt-annotation-position 'right-margin))

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
  :custom
  (doom-themes-enable-bold t)
  (doom-themes-enable-italic t)
  :config
  (load-theme 'doom-gruvbox t)

  (doom-themes-visual-bell-config)
  (doom-themes-org-config))


(use-package elfeed
  :custom
  (elfeed-db-directory (expand-file-name "elfeed/" user-emacs-directory))
  ;; template for yt videos rss stream (replace CHANNEL_ID with actual id):
  ;; https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID
  (elfeed-feeds
      '("https://archlinux.org/feeds/news/"
        "https://9to5linux.com/feed/atom"))
  :config
  (global-set-key (kbd "C-c e") 'elfeed))

(use-package markdown-mode)

;;; Built-ins
(setq use-package-always-ensure nil)

(use-package recentf
  :bind ("C-c o" . recentf-open-files)
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
  :custom
  (c-default-style "linux")
  (c-backspace-function 'delete-backward-char)
  :config
  (defun rc/c-lineup-arglist-smart-offset (langelem)
    (save-excursion
      (let* ((paren-pos (c-langelem-pos langelem))
             (base-indent
              (save-excursion
                (goto-char paren-pos)
                (back-to-indentation)
                (current-column)))
             (is-block
              (save-excursion
                (goto-char paren-pos)
                (if (c-syntactic-re-search-forward "[{;]" nil t)
                    (string= (match-string 0) "{")
                  nil))))
        (if is-block
            (vector (+ base-indent (* 2 c-basic-offset)))
          (vector (+ base-indent c-basic-offset))))))

  (defun rc/c-mode-setup ()
    (c-set-offset 'arglist-intro 'rc/c-lineup-arglist-smart-offset)
    (c-set-offset 'arglist-cont-nonempty 'rc/c-lineup-arglist-smart-offset)
    (c-set-offset 'arglist-close 0)
    (c-set-offset 'substatement '+)
    (c-set-offset 'case-label '+)
    (c-set-offset 'statement-block-intro '+))

  (add-hook 'c-mode-common-hook 'rc/c-mode-setup))

(use-package which-key
  :init (which-key-mode 1))

(provide 'packages)
