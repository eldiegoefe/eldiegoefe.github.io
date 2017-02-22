:title: Mis configuraciones del sistema
:date: 2016-01-04 10:00
:category: tecnicismos
:tags: linux, emacs
:author: El Diego Efe
:excerpt: Mis configuraciones del sistema
:disqus_identifier: Mis configuraciones del sistema
:status: draft
   
Con cierta frecuencia instalo o reinstalo algún linux y trato de replicar el
mismo setup en todos: misma ubicación de archivos de configuración, idénticos
atajos de teclado, etc. Resumo acá algunos detalles.

* Repositorio de archivos de configuración (repo privado en bitbucket):

  + ohmyzsh
  + emacs (spacemacs)

* Archivos de org-mode (repo privado en bitbucket):

  + en la carpeta ~/org (que se crea automáticamente, no se cómo)

* Snippets (repo privado en bitbucket):

  + clono el repo dentro de ~/.emacs.d/private/
  + contiene snippets para:

    - rst-mode
    - org-mode

En algunos lugares clave coloco symlinks con la orden, que es válida tanto para
archivos como para directorios (que en linux deben ser también archivos, como
los puertos, etc.):

.. code-block:: terminal

   ln -s /path/to/file /path/to/symlink

Por ejemplo, en la PC con el disco externo conteniendo mi archivos personal de
org-mode, coloco un symlink desde el directorio ~/org hacia
/media/diego/toshiba/mis-archivos-org/ (al menos esta ruta es válida con Linux
Mint 17.3).

.. code-block:: terminal
   
   ln -s /media/diego/toshiba/mis-archivos-org/ /home/org/

También enlazo el contenido de ~/.spacemacs/init.el hacia
~/mis-configs/.spacemacs (y borro el archivo .spacemacs que se haya creado
espontáneamete en el home, porque sino el que determina la configuración de
emacs es éste último).

.. code-block:: terminal

   ln -s ~/mis-configs/.spacemacs ~/.spacemacs/init.el
