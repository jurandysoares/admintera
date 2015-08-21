Dicas do Editor VIM
===================

Edição Básica
--------------

Movimentos do cursor:

* h - move para esquerda
* j - move para baixo
* k - move para cima
* l - move para direita
* w - jump by start of words (punctuation considered words)
* W - jump by words (spaces separate words)
* e - jump to end of words (punctuation considered words)
* E - jump to end of words (no punctuation)
* b - jump backward by words (punctuation considered words)
* B - jump backward by words (no punctuation)
* 0 - (zero) início da linha
* ^ - primeiro caracter não-branco da linha
* $ - fim da linha
* G - Go To command (prefix with number - 5G goes to line 5)

Nota: Prefix a cursor movement command with a number to repeat it. For example, 4j moves down 4 lines.

Modo de inserção - Inserir/Anexar texto

* i - inicia modo de inserção no cursor
* I - inicia modo de inserção no início da linha
* a - anexa após o cursor
* A - anexa no fim da linha
* o - abre (anexa) linha em branco abaixo da linha atual (sem necessidade de pressionar <ENTER>)
* O - abre uma linha em branco acima da linha atual
* ea - anexa no final da palavra
* Esc - sai do modo de inserção


Abrir dois arquivos em janelas separadas
----------------------------------------

* Horizontalmente::
  
    vim -o2 arq1.ext1 arq2.ext2

* Verticalmente::
  
    vim -O2 arq1.ext1 arq2.ext2

Referências:

.. [#split] `[SuperUser] How to open files in vertically/horizontal split windows in Vim from the command line <http://superuser.com/questions/486532/how-to-open-files-in-vertically-horizontal-split-windows-in-vim-from-the-command>`_
.. [#basic] `My vi/vim cheatsheet <http://www.worldtimzone.com/res/vi.html>`_
