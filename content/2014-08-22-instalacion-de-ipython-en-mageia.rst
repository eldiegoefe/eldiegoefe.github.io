:title: Instalando IPython en Mageia
:date: 2014-08-22 10:00
:category: tecnicismos
:tags: ipython, mageia, root, pip, instalacion
:author: El Diego Efe
:excerpt: Instalando IPython en Mageia
:disqus_identifier: instalando ipython en mageia

Para instalar IPython en Mageia, sin tener privilegios de root hay que
cumplir con los siguientes pasos:

- Contar con privilegios de root para poder correr el instalador
- Hay que instalar PIP
- Con PIP instalar IPython

Trabajar como root:
-------------------

Conviene agregar el usuario a la lista de usuarios con privilegios
para ejecutar *sudo*. Las instrucciones están en `Configuring sudo`_
de Mageia. Históricamente en UNIX este es el grupo Wheels.

.. _`Configuring sudo`: https://wiki.mageia.org/en/Configuring_sudo

Primero hay que crear el archivo */etc/sudoers.d/01wheel*

Después ejecutar lo siguiente en un terminal como root (es decir,
luego de hacer /usr/bin/su):

.. code-block:: console

  $ echo "%wheel ALL=(ALL)  ALL" > /etc/sudoers.d/01wheel
  $ chmod 440 /etc/sudoers.d/01wheel


Agregar el usuario al grupo "Wheel". Para ello hay que editar el
usuario (desde Configure su computador / Administrar usuarios del
sistema). Click derecho para el menú contextual sobre el nombre del
usuario a agregar y *editar*. En la pestaña de grupos agregar un tick
sobre el grupo **wheel** y aceptar.

Desloguearse y volver a entrar (en caso que el usuario modificado sea
el usuario que hizo la edición).

**IMPORTANTE**: para mejorar la seguridad del sistema conviene usar
sudo o su siempre precedidos de la ruta real al comando (la
explicación completa verla en el link original), es decir:

.. code-block:: console

 $ /usr/bin/sudo *comando*
 $ /usr/bin/su *comando*


Instalación de PIP
------------------

Esto es muy fácil:

.. code-block:: console

 $ /usr/bin/sudo urpmi python-setuptools
 $ /usr/bin/sudo easy_install pip


Instalación de IPython
----------------------

Igual de fácil:

.. code-block:: console

 $ /usr/bin/sudo pip install ipython
