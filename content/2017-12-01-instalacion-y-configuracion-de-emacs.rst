Instalación y configuración de Emacs 
####################################

:date: 2017-12-01 10:00
:category: tecnicismos
:tags: emacs
:author: El Diego Efe
:excerpt: Instalación de Emacs
:disqus_identifier: Instalación de Emacs

Estos son los pasos que sigo cuando instalo Emacs y Spacemacs, junto con el
archivo de configuración que guardo en un repositorio privado.

Paso 1: Modos de instalación
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Opción A: repositorio con la última versión de Emacs
----------------------------------------------------

Esta es la manera más facil de instalación, para un un sistema descendiente de
Debian (Ubuntu, Mint, etc).

.. code-block:: sh

   $ sudo add-apt-repository ppa:ubuntu-elisp/ppa
   $ sudo apt-get update
   $ sudo apt-get install emacs-snapshot emacs-snapshot-el

Opción B: compilación desde un terminal
---------------------------------------

Bajar la versión a instalar desde http://ftp.gnu.org/gnu/emacs/ son dos archivos
.tar.gz y .tar.gz.sig (o sino .tar.xz y .tar.xz.sig). Tiene la ventaja de
optimizar el programa de acuerdo a la máquina específica en la que va a correr. 

.. code-block:: sh

   $ tar -xf emacs-??.?.tar.gz            ; descomprimir el archivo
   $ cd emacs-??.?                        ; entrar al directorio
   $ sudo apt-get install build-essential ; instalar dependencias
   $ sudo apt-get build-dep emacs24       ; instalar dependencias
   $ ./configure       ; preparar para compilar
   $ make              ; compilar
   $ sudo make install ; instalar

--------------------------------------------------------------

Paso 2: Instalar Spacemacs
^^^^^^^^^^^^^^^^^^^^^^^^^^

Las instrucciones son muy fáciles y están en el `github de spacemacs
<https://github.com/syl20bnr/spacemacs>`__. Hay que borrar (o guardar en otro
lado) el directorio ~/.emacs.d/ y luego clonar spacemacs allí con la siguiente
orden:

.. code-block:: sh

   $ git clone https://github.com/syl20bnr/spacemacs ~/.emacs.d

Spacemacs se instalará recién la próxima vez que se inicie Emacs.

--------------------------------------------------------------

Paso 3: Clonar archivo de configuración
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En un repositorio de Bitbucket tengo guardados los archivos de configuración de
distintos programas o sistemas. Principalmente las del sistema operativo y de
Emacs. Les recomiendo hacer lo mismo, para no tener que reconfigurar el sistema
de vuelta tras cada reinstalación.

.. code-block:: sh

   $ git clone https://bitbucket.org/mi-usuario/mis-configs

Luego hay que colocar symlinks desde los lugares en los que estos archivos de
configuración deberían ser encontrados por el sistema, hacia los archivos en
cuestión dentro del directorio ~/mis-configs.

La fórmula es: ln -s /path/to/file /path/to/symlink

Por ejemplo:

.. code-block:: sh

   $ ln -s ~/.spacemacs ~/.mis-configs/.spacemacs

--------------------------------------------------------------

Paso 4: Iniciar Emacs
^^^^^^^^^^^^^^^^^^^^^

Se va a actualizar spacemacs de acuerdo a las configuraciones que recuperamos
del repositorio. Quizás haya que salir y volver a entrar a Emacs varias veces
hasta que la instalación se complete exitosamente.
