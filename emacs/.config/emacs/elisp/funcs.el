;;; funcs.el -- custom function definitions

(defun rc/duplicate-line ()
  "Duplicate current line"
  (interactive)
  (let ((column (- (point) (point-at-bol)))
        (line (let ((s (thing-at-point 'line t)))
                (if s (string-remove-suffix "\n" s) ""))))
    (move-end-of-line 1)
    (newline)
    (insert line)
    (move-beginning-of-line 1)
    (forward-char column)))

(defun rc/close-other-buffers ()
  "Kill all buffers except the current one and the *scratch* buffer."
  (interactive)
  (let ((current (current-buffer)))
    (dolist (buf (buffer-list))
      (unless (or (eq buf current)
                  (string-equal (buffer-name buf) "*scratch*"))
        (kill-buffer buf)))))

(defun rc/copy-files-to-clipboard (&optional plain-text)
  "Copy marked/opened files to the clipboard. With a prefix arg copy plain text; otherwise copy a text/uri-list."
  (interactive "P")
  (let ((files (cond
                ;; case 1: marked in Dired
                ((derived-mode-p 'dired-mode)
                 (dired-get-marked-files))
                ;; case 2: file-visiting buffer
                (buffer-file-name
                 (list buffer-file-name))
                (t (user-error "No file found to copy")))))
    (unless (executable-find "wl-copy")
      (user-error "wl-copy not found"))
    (with-temp-buffer
      (dolist (f files)
        (insert (if plain-text
                    (expand-file-name f)
                  (concat "file://" (expand-file-name f)))
                "\n"))
      (call-process-region
       (point-min) (point-max)
       "wl-copy" nil nil nil
       "-t" (if plain-text "text/plain" "text/uri-list")))
    (message "Copied %s as %s"
             (format "%d file(s)%s" (length files) (if (> (length files) 1) "s" ""))
             (if plain-text "plain text" "URI list"))))

(defun rc/set-default-font (&optional frame)
  (with-selected-frame (or frame (selected-frame))
    (set-face-attribute 'default nil
                        :font "UbuntuMono Nerd Font"
                        :height 180)
    (set-face-attribute 'line-number nil :inherit 'default :height 1.0)
    (set-face-attribute 'line-number-current-line nil :inherit 'default :height 1.0)))

(defun rc/yank-and-indent ()
  "Yank text and indent the newly inserted region."
  (interactive)
  (let ((beg (point)))
    (forward-line 0)
    (yank)
    (indent-region beg (point))))

(defun rc/toggle-gruvbox-theme ()
  "Toggle between gruvbox-dark-medium and gruvbox-light-medium."
  (interactive)
  (if (member 'gruvbox-dark-medium custom-enabled-themes)
      (progn
        (disable-theme 'gruvbox-dark-medium)
        (load-theme 'gruvbox-light-medium t))
    (progn
      (disable-theme 'gruvbox-light-medium)
      (load-theme 'gruvbox-dark-medium t))))

(provide 'funcs)
