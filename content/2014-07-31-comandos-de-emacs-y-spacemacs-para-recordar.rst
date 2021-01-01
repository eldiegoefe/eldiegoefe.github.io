Comandos de Emacs y Spacemacs para recordar
###########################################

:date: 2014-07-31 10:00
:category: tecnicismos
:tags: blog, restructuredtext, cheat sheet, emacs
:author: El Diego Efe
:excerpt: Comandos de Emacs y Spacemacs para recordar
:disqus_identifier: comandos de emacs y spacemacs para recordar

Yasnippets / Company
====================

En `la documentación de Spacemacs`_ están los keybindings. No funciona más SPC i
s (que mostraba una lista de snippets habilitados para el modo actual).

- reemplaza la clave previa al punto por el contenido del snippet
  correspondiente: M-/

.. _la documentación de Spacemacs:
   https://github.com/syl20bnr/spacemacs/tree/master/layers/%2Bcompletion/auto-completion#key-bindings

Búsqueda
========

La búsqueda habitual con i-search (C-s) se potencia al instalar `swiper`_, que
ofrece un listado de las lineas del documento donde se encuentran los resultados
de la búsqueda.

También se puede buscar con evil-search-forward (/) que es una variante de
i-search, pero sólo va a la próxima aparición de la búsqueda y hay que recordar
cómo ir a los resultados siguientes (C-s) y anteriores (C-r). Es menos visual.

.. _swiper: https://github.com/abo-abo/swiper

Movimiento
==========

Se puede saltar facilmente a letras o lineas que aparezcan en pantalla. Dentro
de Spacemacs las opciones para este tipo de salto están bajo el prefijo SPC j.
El sistema de búsqueda funciona así: primero se determina qué elemento se busca
(un caracter, una linea, etc). En caso de que sean letras se ingresa cuál es la
letra buscada. Como resultado el sistema resalta la ubicación de cada letra o
linea y muestra en cada lugar un código de dos letras, que se deben pulsar para
llegar hasta allí. Para ir a:

- un caracter: SPC j j caracter. Por ejemplo, para mostrar las letras z: SPC j
  j z.
- una linea: SPC j l linea.

Otros movimientos habituales:

- gg: se mueve al principio del documento
- 15 gg: se mueve a la línea 15. Obviamente '15' es un ejemplo.
- G: se mueve al final del documento

Ventanas
========

- dividir ventana verticalmente: SPC w /
- dividir ventana horizontalmente: SPC w -

Dired
=====

- convertir buffer en texto editable: C-x C-q
- aceptar los cambios realizados y finalizar edición: C-c C-c

Enlaces
=======

Armé un snippet para colocar links más fácilmente (`lo pueden ver aca`_), pero
igual dejo acá la sintaxis para poner hiperlinks en restructuredText:

.. _lo pueden ver aca: |filename|/2014-10-07-emacs-y-restructuredtext.rst

::

    External hyperlinks, like Python_.

    .. _Python: http://www.python.org/

    External hyperlinks, like `Python <http://www.python.org/>`_.

    Wikipedia es `mi sitio favorito`_.

    .. _mi sitio favorito: http://www.wikipedia.org/


Indentación
===========

Primero se selecciona un bloque de texto y luego:

- indent-region. Indenta todo, pero no resguarda las indentaciones que el bloque
  pudo haber tenido, como es usual en los códigos de programación.

- indent-rigidly (C-x TAB, SPC x TAB). Mueve todo el bloque manteniendo las
  indentaciones que el bloque haya tenido antes. El movimiento se determina
  presionando las flechas (o las teclas 'h' y 'l') luego de invocar el comando.

Ayuda
=====

Para pedir ayuda sobre una función:

- Si se sabe el nombre: C-h f nombre-de-la-función
- Si se sabe el keybinding: C-h k keybinding

Caracteres
==========

Todo esto cambia de acuerdo al teclado (en el `Ergodox`_ tengo teclas
programables) y con la distribución elegida. De todos modos, actualmente son las
siguientes: (uso la letra M para referirme más precisamente al Alt Derecho)

::

    < M . > M , ` M 0 \ M º

.. _Ergodox: http://deskthority.net/wiki/ErgoDox


.. figure:: https://farm9.staticflickr.com/8577/16108048537_1601cc1b60_b.jpg
   :scale: 100%
   :width: 100%
   :align: center
   :alt: ergodox
   :target: https://farm9.staticflickr.com/8577/16108048537_d0db2cc098_o.jpg
