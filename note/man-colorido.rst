Página de Manual Colorida
==========================

Adicionar as linhas abaixo a um dos arquivos:

* ``~/.bashrc`` (Por usuário)
* ``/etc/bash.bashrc`` (Global, no Debian/Ubuntu) 
* ``/etc/bashrc`` (Global, no RedHat/Fedora/CentOS)

.. code-block:: sh

  man() {
  	env \
  		LESS_TERMCAP_mb=$(printf "\e[1;31m") \
  		LESS_TERMCAP_md=$(printf "\e[1;31m") \
  		LESS_TERMCAP_me=$(printf "\e[0m") \
  		LESS_TERMCAP_se=$(printf "\e[0m") \
  		LESS_TERMCAP_so=$(printf "\e[1;44;33m") \
  		LESS_TERMCAP_ue=$(printf "\e[0m") \
  		LESS_TERMCAP_us=$(printf "\e[1;32m") \
  			man "$@"
  }

Referência: http://www.cyberciti.biz/faq/linux-unix-colored-man-pages-with-less-command/
