; Emacs keeps adding this line back. Leaving this commented line in.
;(package-initialize)

;; Temporary fix for emacs TLS issue
(setq gnutls-algorithm-priority "NORMAL:-VERS-TLS1.3")

;; We can't tangle without org!
(require 'org)

;; Open the configuration
(org-babel-load-file "~/.emacs.d/config.org")
