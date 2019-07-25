Keybindings conflictivos en Emacs
#################################

:date: 2014-08-17 10:00
:category: tecnicismos
:tags: emacs, keybindings
:author: El Diego Efe
:excerpt: Keybindings conflictivos en Emacs
:disqus_identifier: keybindings conflictivos

Desde que empecé a usar Emacs probé dos grandes paquetes para
facilitar su uso. Uno ha sido **Ergoemacs**, que es buenísimo porque
remapea todos los accesos rápidos de teclado para poder usarlos de
forma más simple e intuitiva (por ejemplo: C-x C-f, que "visitaba" un
archivo, pasa a ser C-o, que es el comando stándard para "abrir
archivo" en casi todos los programas actuales). Sin embargo, luego
encontré buenas funcionalidades en otro llamado **Prelude**. Estando
sólo activo este último (ya que hay conflictos con ergoemacs) tuve el
siguiente problema:

al editar una tabla dentro de *org-mode*, el keybinding para eliminar
una fila debía ser M-S-<up> (es decir: alt-shift-flecha arriba) pero
en cambio al apretar esa secuencia de teclas lo que sucedía era que se
ejecutaba el comando *move-text-up* que está definido en prelude.

Esta combinación de teclas resultó que estaba definida en el archivo
**~/.emacs.d/core/prelude-mode.el**, en el cual se encuentra la
siguiente linea:

.. code-block:: cl

 (define-key map [(meta shift up)]  'move-text-up)

para recuperar el keybinding y que vuelva a funcionar como se espera
en org-mode, lo primero que probé fue comentar esa linea agregándole
dos ; al inicio. Pero de este modo, cuando toque actualizar el paquete
Prelude, el archivo prelude-mode.el se sobreescribirá desde el
servidor y el problema volverá a aparecer.

Entonces me puse a buscar cómo resolverlo y encontré que se puede
anular el keybinding correspondiente a un modo de Emacs con el
siguiente comando (que debe incluirse en el archivo de inicialización
personal, generalmente **~/.emacs** o en mi caso
**~/.emacs.d/personal/custom.el**):

.. code-block:: cl

 (define-key prelude-mode-map [(meta shift up)] nil)

Lo mismo puede hacerse para M-S-<down>:

.. code-block:: cl

 (define-key prelude-mode-map [(meta shift down)] nil)

Obviamente esta técnica es aplicable para anular el keybinding de
cualquier modo que se quiera desactivar.
