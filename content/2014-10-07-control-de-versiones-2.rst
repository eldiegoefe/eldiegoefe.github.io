Tutorial sobre control de versiones (parte 2)
#############################################

:date: 2014-10-08 10:00
:category: tecnicismos
:tags: git, control de versiones, tutorial
:author: El Diego Efe
:excerpt: Tutorial sob
:disqus_identifier: control de versiones parte 2

Indice del Tutorial
===================

   - `Parte 1`_. Cómo armar un repositorio local
   - `Parte 2`_. Cómo subir el repositorio local al remoto
   - `Parte 3`_. Cómo colaborar en un mismo repositorio remoto
   - `Parte 4`_. Cómo resolver conflictos

     .. _Parte 1: |filename|/2014-10-06-control-de-versiones-1.rst
     .. _Parte 2: |filename|/2014-10-07-control-de-versiones-2.rst
     .. _Parte 3: |filename|/2014-10-09-control-de-versiones-3.rst
     .. _Parte 4: |filename|/2014-10-10-control-de-versiones-4.rst

Para ver las versiones (en inglés) en las cuales se basa este
tutorial, podés visitar `la página de Software Carpentry`_

.. _la página de Software Carpentry: http://software-carpentry.org/v5/novice/git/

Armar un proyecto (repositorio) en GitHub
=========================================

Para subir el repositorio local a GitHub es indispensable tener una
cuenta allí (que es gratis, así que a relajarse y disfrutar). Es
bastante intuitivo el modo de crear un repositorio. Pero pongo un par
de imágenes, a modo de muestra.

.. figure:: https://farm8.staticflickr.com/7500/16103637368_e5b482f6aa_o.png
   :scale: 100%
   :width: 100%
   :align: center
   :alt: pantalla principal de github (siendo un usuario)
   :target: https://farm8.staticflickr.com/7500/16103637368_e5b482f6aa_o.png

En la pantalla anterior hay que hacer click sobre el botón verde que
dice "*+ New repository*", que nos deposita en la imagen de abajo.

.. figure:: https://farm9.staticflickr.com/8661/15668754054_413938acf0_o.png
   :scale: 100%
   :width: 75%
   :align: center
   :alt: formulario para ingresar los datos del nuevo repositorio
   :target: https://farm9.staticflickr.com/8661/15668754054_413938acf0_o.png

Solamente ponemos el nombre y la descripción del repositorio. Los
repositorios privados son pagos, así que por lo general uno elige
"*Public*". No hace falta inicializarlo con un *readme*, ni agregar un
*.gitignore*, ni seleccionar una licencia. Basta con apretar el botón
verde de "*Create repository*" y chan, ya tenemos repositorio sin
tener que acercarnos a la farmacia.

La imagen que sigue es para mostrar que la dirección del nuevo
repositorio, aún vacío, pero listo para clonarse sin parecerse a la
oveja Dolly, se encuentra sobre el panel de la izquierda, donde dice
"HTTPS clone URL". Copiamos de ahí esa dirección y nos dirigimos con
presteza y gráciles movimientos al terminal, que debería estar ubicado
(controlar con pwd) en el directorio de nuestro repositorio
local. Escribimos (en mi caso estoy trabajando sobre un nuevo
repositorio para alojar la configuración de mi Emacs):

.. figure:: https://farm8.staticflickr.com/7515/16290337352_9a8d0da905_o.png
   :scale: 100%
   :width: 75%
   :align: center
   :alt: de aqui se saca la url para la clonación
   :target: https://farm8.staticflickr.com/7515/16290337352_9a8d0da905_o.png


Setear el repositorio remoto desde nuestro repo local
=====================================================

En la siguiente orden le estamos diciendo a Git que agregue como
repositorio remoto la URL que le pasamos, y además a esa dirección le
asignamos el alias "*origin*" (se suele utilizar *origin* por
convención, pero podríamos haberlo llamado
"*farodelfindelmundo*"). Podemos chequearlo con *git remote -v*.

.. code-block:: console

   $ git remote add origin https://github.com/eldiegoefe/emacs.git
   $ git remote -v
   origin  https://github.com/eldiegoefe/emacs.git (fetch)
   origin  https://github.com/eldiegoefe/emacs.git (push)

Subir repo local al remoto
==========================

Ahora es superfacil subir los archivos de nuestro repositorio local
hacia el repositorio remoto (en github.com):

.. code-block:: console

   $ git push origin master

Cuando te dicen "master" es porque sos grosso, sabelo. Además
"*master*" es la única rama (branch) que por el momento tenemos en el
recientemente creado repositorio remoto y vacío (se me cae un
lagrimón). También es la única rama que tenemos en el repo local (lo
podemos chequear con *git branch*). Al ejecutar el *git push* el
sistema les va a pedir primero el nombre de usuario y luego la
contraseña (que se hicieron en github, porque hacia allí está subiendo
los archivos).

¿Problemas?
-----------

Si acaso diera un error, como me sucedió en el ejemplo que les estoy
relatando, es porque el repositorio remoto en vez de estar vacío tiene
algún contenido. Debemos entonces, antes de subir cosas, bajar ese
contenido que no tenemos en el repositorio local (en mi caso el
archivo con la licencia), con la orden "*git pull*" (*git push* empuja
desde el local hacia el remoto, *git pull* tira desde el remoto hacia
el local):

.. code-block:: console

   $ git pull origin master
   warning: no common commits
   remote: Counting objects: 3, done.
   remote: Compressing objects: 100% (2/2), done.
   remote: Total 3 (delta 0), reused 0 (delta 0)
   Unpacking objects: 100% (3/3), done.
   From https://github.com/eldiegoefe/emacs
    * branch            master     -> FETCH_HEAD
    * [new branch]      master     -> origin/master
   Merge made by the 'recursive' strategy.
    LICENSE | 675 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    1 file changed, 675 insertions(+)
    create mode 100644 LICENSE

Cuando se agregan cosas (al repo local) hay que comitearlas, como de
costumbre. Por eso, al ejecutar el comando anterior el sistema pide un
mensaje de "*commit*" y luego da el resultado que muestro (por ahora
es un jeroglífico, pero tiene sentido, eh). En mi caso, el archivo
LICENCE que sólo estaba en el remoto, ahora está también en el local,
lo cual puede verse haciendo:

.. code-block:: console

   $ ls
   custom.el  LICENSE  preload

Podemos chequear el estado del repo local:

.. code-block:: console

   $ git status
   # On branch master
   nothing to commit, working directory clean

No problem
----------

Ahora sí volvemos a intentar subir los archivos que faltan hacia
origin (el repo remoto, solo, triste y abandonado):

.. code-block:: console

   $ git push origin master
   Counting objects: 12, done.
   Delta compression using up to 4 threads.
   Compressing objects: 100% (8/8), done.
   Writing objects: 100% (11/11), 2.88 KiB | 0 bytes/s, done.
   Total 11 (delta 2), reused 0 (delta 0)
   To https://github.com/eldiegoefe/emacs.git
      e23c676..2c817b6  master -> master

"Joyines", diría el Tano. Si ahora hiciésemos un pull desde el remoto,
no debería pasar nada porque ambos repos son iguales. Veamos:

.. code-block:: console

   git pull origin master
   From https://github.com/eldiegoefe/emacs
    * branch            master     -> FETCH_HEAD
   Already up-to-date.

En cambio, si alguien actualizó el remoto con algún archivo nuevo, o
modificó los existentes, al hacer el pull se incorporarían al repo
local esos cambios (lo cual siempre hay que hacer antes de hacer un
push hacia el remoto).

::

    La bandera '-u'

    Es común encontrar que git push se acompañe de la bandera
    '-u'. Vamos a dejar eso para después, pero es casi seguro que se
    usa para fijar origen y destino, de manera que un git push
    desnudo, funcionará después con las ramas origen y destino que
    acompañaban al -u (que es algo de --upstream nosecuanto). Pero
    estoy tocando de oido, mejor veamos más adelante.

Nos vemos en la `parte 3`_.

.. _parte 3: |filename|/2014-10-09-control-de-versiones-3.rst
