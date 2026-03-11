;;; init.el -- a dirty starting point for my Emacs configuration
;; for real configs, check elisp/

;;; Hide junk in $XDG_DATA_HOME
(setq user-emacs-directory
      (expand-file-name "emacs/"
                        (or (getenv "XDG_DATA_HOME") "~/.local/share/")))

(setq package-user-dir (expand-file-name "elpa" user-emacs-directory))
(unless (file-exists-p user-emacs-directory)
  (make-directory user-emacs-directory t))

(setq custom-file (expand-file-name "custom.el" user-emacs-directory))
(when (file-exists-p custom-file)
  (load custom-file))

(make-directory (expand-file-name "auto-save/" user-emacs-directory) t)
(setq auto-save-file-name-transforms
      `((".*" ,(expand-file-name "auto-save/" user-emacs-directory) t)))
(setq auto-save-list-file-prefix
      (expand-file-name "auto-save/.saves-" user-emacs-directory))

(make-directory (expand-file-name "backups/" user-emacs-directory) t)
(setq backup-directory-alist
      `(("." . ,(expand-file-name "backups/" user-emacs-directory))))

(make-directory (expand-file-name "eln-cache/" user-emacs-directory) t)
(setq native-comp-eln-load-path
      (list (expand-file-name "eln-cache/" user-emacs-directory)))

;;; Organize config directory
(defconst rc/emacs-config-dir (file-name-directory user-init-file))
(add-to-list 'load-path (expand-file-name "elisp" rc/emacs-config-dir))

(require 'config)
(require 'packages)
