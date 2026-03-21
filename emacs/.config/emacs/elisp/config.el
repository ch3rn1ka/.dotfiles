;;; config.el -- general configuration
;; for package-specific settings, check packages.el
;; for custom function definitions, check funcs.el

(tool-bar-mode -1)
(menu-bar-mode -1)
(scroll-bar-mode -1)
(delete-selection-mode 1)
(global-font-lock-mode 1)
(column-number-mode 1)

(setq create-lockfiles nil
      scroll-conservatively 101
      scroll-margin 0
      scroll-step 1
      inhibit-startup-screen 1
      display-line-numbers-type 'relative
      display-line-numbers-width-start 1
      vc-follow-symlinks 1)

(setq-default indent-tabs-mode nil
              fringe-indicator-alist
              (assq-delete-all 'continuation
                               (assq-delete-all 'truncation fringe-indicator-alist)))

(add-to-list 'auto-mode-alist '("/tmp/neomutt-" . text-mode))
(add-to-list 'auto-mode-alist '("/tmp/qutebrowser-" . text-mode))

(require 'funcs)
(global-set-key (kbd "C-c r") 'recompile)
(global-set-key (kbd "C-c c") 'rc/copy-files-to-clipboard)
(global-set-key (kbd "C-c k") 'rc/close-other-buffers)
(global-set-key (kbd "C-c y") 'rc/yank-and-indent)
(global-set-key (kbd "C-,") 'rc/duplicate-line)

(add-hook 'prog-mode-hook 'display-line-numbers-mode)
(add-hook 'conf-mode-hook 'display-line-numbers-mode)
(add-hook 'text-mode-hook 'display-line-numbers-mode)
(add-hook 'before-save-hook 'delete-trailing-whitespace)
(add-hook 'window-setup-hook 'rc/set-default-font)
(add-hook 'after-make-frame-functions 'rc/set-default-font)

(provide 'config)
