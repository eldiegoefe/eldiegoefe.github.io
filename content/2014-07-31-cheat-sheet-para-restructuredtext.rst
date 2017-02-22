:title: Cheat sheet para programación
:date: 2014-07-31 10:00
:category: tecnicismos
:tags: blog, restructuredtext, cheat sheet, emacs
:author: El Diego Efe
:excerpt: Cosas útiles para restructuredText
:disqus_identifier: cheat sheat para programacion

Enlaces:
========

Armé un snippet para colocar links más fácilmente (`lo pueden ver
aca`_), pero igual dejo acá la sintaxis para poner hiperlinks en
restructuredText:

.. _lo pueden ver aca: |filename|/2014-10-07-emacs-y-restructuredtext.rst

::

    External hyperlinks, like Python_.

    .. _Python: http://www.python.org/

    External hyperlinks, like `Python <http://www.python.org/>`_.

    Wikipedia es `mi sitio favorito`_.

    .. _mi sitio favorito: http://www.wikipedia.org/


Indentación
===========

comando: indent-region. Indenta todo, pero no resguarda las
indentaciones que el bloque pudo haber tenido, como es usual en los
códigos de programación.

comando: indent-code-rigidly. Mueve todo el bloque a la derecha,
manteniendo las indentaciones que el bloque haya tenido antes.


Caracteres
==========

Todo esto cambia de acuerdo al teclado (en el `Ergodox`_ tengo teclas
programables) y con la distribución elegida. De todos modos,
actualmente son las siguientes: (uso la letra M para referirme más
precisamente al Alt Derecho)

::

    < M .
    > M ,
    ` M 0
    \ M º

.. _Ergodox: http://deskthority.net/wiki/ErgoDox


.. figure:: https://farm9.staticflickr.com/8577/16108048537_1601cc1b60_b.jpg
   :scale: 100%
   :width: 100%
   :align: center
   :alt: ergodox
   :target: https://farm9.staticflickr.com/8577/16108048537_d0db2cc098_o.jpg
