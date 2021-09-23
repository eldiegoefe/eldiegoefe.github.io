# Emacs y restructuredText


Estuve escribiendo algunas entradas para el blog y encontré algunas cosas que
vale la pena recordar, que quedan anotadas aca.

El modo abbrev tendría que desactivarlo globalmente porque cada vez que escribo
la palabra \"*con*\" (en modo restructuredText) y hago un espacio me lo expande
a un texto que no deseo (content\...). Se desactiva con *M-x abbrev-mode*. Mejor
aún, encontré cómo editar la lista de abreviaturas. Es así: *M-x list-abbrevs* y
se abre un buffer con las abreviaturas, que se puede editar. Ver de paso
\"[Using Emacs Abbrev Mode for
Abbreviation](http://ergoemacs.org/emacs/emacs_abbrev_mode.html) para un facil
tutorial sobre el uso elegante de abbrev-mode.

Para seleccionar un rectángulo hay que poner la marca (con C-SPC) en un
extremo del mismo y el punto (es decir el cursor) en el otro extremo.
Así, para borrar ese rectángulo se usa *kill-rectangle* (C-x r k).

Para indentar un párrafo, se lo selecciona y luego se aprieta C-x TAB.
Esto sube la indentación en uno. Se puede repetir C-x TAB (aunque
parezca que no hay región seleccionada).

Agregué dos nuevos snippets para escribir en restructuredtext. Los copio
debajo.

## Links

    # -*- mode: snippet;
    # name: link
    # key: lk
    # --
    \`${1:texto del link}\`_
    .. _$1: ${2:path}
    $0

## Imágenes

    # -*- mode: snippet;
    # name: imagen
    # key: im
    # expand-env: ((yas-indent-line 'fixed))
    # --

    .. image:: ${1:path}
       :scale: ${2:100}%
       :width: ${3:100}%
       :align: ${4:$$(yas-choose-value '("right" "center" "left"))}
       :alt: $5

    $0

