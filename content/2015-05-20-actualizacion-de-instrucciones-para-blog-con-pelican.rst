:title: Actualización de las instrucciones para armar un blog con
        Pelican y GitHub
:date: 2015-05-20 10:00
:category: tecnicismos
:tags: tutorial, blog, git, pelican
:author: El Diego Efe
:excerpt: Actualización de las instrucciones para armar un blog con
          Pelican y GitHub Personal Pages
:disqus_identifier: actualizacion de las instrucciones para blog con
                    pelican y github

El sitio oficial de Pelican, con sus intrucciones de instalación y uso
`es este`_. Originalmente, este post estuvo basado en las
instrucciones de `Nicholas Tan Jerome`_. El post original `pueden
verlo en este enlace`_

Por un lado vamos a configurar un entorno virtual de Python donde
vamos a instalar Pelican, y por otro lado vamos a utilizar un
directorio subdividido en un subdirectorio para nuestro blog y dos
subdirectorios más para herramientas de Pelican (themes y plugins de
Pelican). Supongo que GIT ya está instalado en el sistema.

Instalación de Pelican en un entorno virtual
============================================

Vamos a utilizar virtualenvwrapper para este propósito (tengo
pendiente escribir el tutorial correspondiente). Creamos un entorno
llamado *blogs* y dentro de él instalamos Pelican y también otras
herramientas que utilizaremos posteriormente:

.. code-block:: console

   $ mkvirtualenv blogs
   (blogs)$ pip install pelican
   (blogs)$ pip install beautifulsoup4
   (blogs)$ pip install pelican-youtube
   (blogs)$ pip install ghp-import

Estructura de directorios
=========================

Vamos a utilizar un directorio que va a contener tanto nuestro blog
como otros subdirectorios con algunas herramientas de Pelican. La
organización será la siguiente:

- misBlogs/

  #. eldiegoefe.github.io/
  #. pelican-themes/
  #. pelican-plugins/

Para ello debemos ejecutar las siguientes instrucciones (supongo que
el entorno virtual sigue activado, lo cual se refleja en el prompt):

.. code-block:: console

   (blogs)$ mkdir ~/misBlogs
   (blogs)$ cd ~/misBlogs
   (blogs)$ git clone --recursive https://github.com/getpelican/pelican-themes
   (blogs)$ git clone --recursive https://github.com/getpelican/pelican-plugins

Aún falta crear el directorio para los archivos del blog. Para ello
creamos un repositorio vacío en GitHub. Este sitio ofrece la dirección
nombreUsuario.github.io justamente para alojar blogs personales. Asumo
que ya sabés crear el repositorio (en mi caso el nombre del
repositorio debe ser: eldiegoefe.github.io) y que GIT no te resulta
completamente ajeno, de lo contrario este tutorial parecerá sánscrito
avanzado. El repositorio recientemente creado debe clonarse en el
directorio que fijamos anteriormente, si seguimos de la secuencia de
comandos anteriores sólo debemos tipear:

.. code-block:: console

   (blogs)$ git clone https://github.com/nombreUsuario/nombreUsuario.github.io

En el archivo .gitignore (dentro del directorio
~/misBlogs/nombreUsuario.github.io) se deben colocar todos los
archivos que no se desea incluir en el control de versiones. Por
ejemplo, mi .gitignore se ve así (ya que descarta distintos tipos de
archivos de backup):

::

  *~
  *#
  *.pid
  .#*

Por otra parte, al inicializar el repositorio ya quedó creada la rama
**master** pero vamos a crear también otras dos ramas llamadas
**source** y **gh-pages**. La rama **source** contendrá los archivos
de configuración de Pelican para nuestro sitio, los archivos de texto
con el contenido de cada post que vayamos escribiendo, etc. La rama
*gh-pages* es necesaria para el procedimiento de generación del sitio
estático. Creamos entonces ambas ramas y cambiamos hacia **source**:

.. code-block:: console

   (blogs)$ cd nombreUsuario.github.io
   (blogs)$ git branch gh-pages
   (blogs)$ git branch source
   (blogs)$ git checkout source

Ejecución inicial de Pelican
============================

Dentro de la recientemente creada rama *source*, dentro del directorio
del sitio (nombreUsuario.github.io) se debe ejecutar por única vez la
orden **pelican-quickstart** para que se generen los archivos de
configurción de Pelican (va el guión entre las dos palabras):

.. code-block:: console

   (blogs)$ pelican-quickstart

Tras ese comando, y tras contestar todas las preguntas que aparecen,
no solamente se guarda la configuración deseada (en los archivos
*pelicanconfig.py* y *publishconf.py*), sino que se generan todos los
archivos que Pelican necesita (incluso dos directorios nuevos: content
y output). Una de las preguntas, sobre el site url debe contestarse
con: http://nombreUsuario.github.io

El contenido de pelicanconf.py tras responder a las preguntas de
pelican-quickstart y además editar manualmente el archivo para
completar los datos, queda así:

.. code-block:: python

   #!/usr/bin/env python
   # -*- coding: utf-8 -*- #
   from __future__ import unicode_literals

   AUTHOR = u'El Diego Efe'
   SITENAME = u'Certezas Dudosas'
   SITEURL = 'http://nombreUsuario.github.io'

   TIMEZONE = 'America/Argentina/Buenos_Aires'

   DEFAULT_LANG = u'es'

   # Feed generation is usually not desired when developing
   FEED_ALL_ATOM = None
   CATEGORY_FEED_ATOM = None
   TRANSLATION_FEED_ATOM = None

   # Blogroll
   LINKS =  (('Pelican', 'http://getpelican.com/'),
	     ('Python.org', 'http://python.org/'),
	     ('Jinja2', 'http://jinja.pocoo.org/'),
	     ('You can modify those links in your config file', '#'),)

   # Social widget
   SOCIAL = (('Twitter', 'http://twitter.com/nombreUsuario'),
	     ('Github', 'https://github.com/nombreUsuario'),
	     ('Facebook', 'http://www.facebook.com/nombreUsuario'),
	     ('Google+', 'https://plus.google.com/+DiegoEfe'),
   )

   DEFAULT_PAGINATION = 10

   # Uncomment following line if you want document-relative URLs when developing
   #RELATIVE_URLS = True


Y el contenido de publishconf.py queda así:


.. code-block:: python

   #!/usr/bin/env python
   # -*- coding: utf-8 -*- #
   from __future__ import unicode_literals

   # This file is only used if you use `make publish` or
   # explicitly specify it as your config file.

   import os
   import sys
   sys.path.append(os.curdir)
   from pelicanconf import *

   SITEURL = 'http://nombreUsuario.github.io'
   RELATIVE_URLS = False

   FEED_ALL_ATOM = 'feeds/all.atom.xml'
   CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

   DELETE_OUTPUT_DIRECTORY = True

   # Following items are often useful when publishing

   #DISQUS_SITENAME = ""
   #GOOGLE_ANALYTICS = ""


Escribir el primer post
=======================

Las entradas de nuestro nuevo blog se escriben como un archivo de
texto plano con el formato de Markdown o restructuredText, y se deben
guardar con la extensión correspondiente (.md o .rst) dentro del
directorio content. De este modo, cuando emita el comando para generar
el sitio habrá un contenido (sino el blog queda vacío).

Por ejemplo, podemos guardar el archivo *2015-05-20-prueba.rst* con el
siguiente contenido:

::

  :title: Primera prueba
  :date: 2015-05-20 10:00
  :category: ejemplos
  :tags: ejemplo, tutorial, pruebas, blog
  :author: El Diego Efe
  :excerpt: Solo una prueba

  Mi titulo
  =========

  Hola. Este es mi primer post. Chau.

Generación del blog
===================

Ahora que el blog ya está configurado y tiene un contenido vamos a
generar el sitio y chequear cómo se ve. La generación (que procesa
todos los archivos del directorio *content*, produce los archivos
*html* y los aloja en el directorio *output*) se logra con **make
html** y luego se ejecuta un servidor local con **make serve** que
permite visitar el blog en la dirección http://localhost:8000:

.. code-block:: console

   (blogs)$ make html
   (blogs)$ make serve

En la primera corrida puede haber problemas de formato, sin embargo
tras subir el sitio al repositorio externo, se corrobora que la página
carga bien. El servidor se detiene tecleando Ctrl-C Ctrl-C en el
terminal.

Regeneración del sitio ante ediciones sucesivas
-----------------------------------------------

En vez de usar *make html* y *make serve*, que se vuelve tedioso si
uno realiza muchas modificaciones en sus posteos es utilizar *make
regenerate* en vez de *make html*.

Con *make regenerate*, cualquier edición de los posts (ya sea el
agregado de nuevos archivos *.md* o *.rst*, tanto como la modificación
de los existentes) se refleja inmediatamente en cómo se ve el sitio
desde el servidor local.

Para usarlo se requiere prestar atención. Activar el entorno virtual *blogs* en
dos terminales distintos. A continuación lo muestro con el uso de pyenv, aunque
no haya explicado nada antes sobre esta alternativa de manejo de virtualenvs.
Vayamos al grano, en un terminal ejecutar esto:

.. code-block:: console

   $ pyenv activate blogs
   (blogs)$ cd ~/blogs/eldiegoefe.github.io/
   (blogs)$ make regenerate

En otro terminal, hacer lo propio:

.. code-block:: console

   $ pyenv activate blogs
   (blogs)$ cd ~/blogs/eldiegoefe.github.io/
   (blogs)$ make serve

De este modo el sitio se regenera ante cualquier edición de su
contenido, y permanece accesible en http://localhost:8000 (no hay que
olvidar que el navegador debe recargar las páginas editadas para ver
los cambios). Tengan presente que si hay algún error, el *regenerate* finaliza
indicando cuál fue el problema (lo muestra en el terminal) y por más que
actualicemos la página en el navegador no veremos cambios. Habrá que corregir
los errores de las páginas que estemos modificando y luego volver a ejecutar
el *make regenerate*.

Subir el sitio al repositorio remoto
====================================

Una vez que estamos conformes con el contenido vamos a agregar todo al
branch **source**:

.. code-block:: console

   (blogs)$ git add .
   (blogs)$ git commit -m "Commit inicial de la rama source"

De este modo nuestros archivos ya quedaron almacenados en la rama
**source** de nuestro repositorio local. Pero lo que se verá al
acceder al blog, es lo que esté en la rama **master**, así que hay que
copiar allí las páginas html de la carpeta output. Nicholas propone
usar un script llamado ghp-import para facilitar esa tarea (que ya
instalamos en la parte inicial de este tutorial). Este script exporta
el contenido de la carpeta que se menciona en la linea de comandos (al
ejecutarlo) hacia la rama "gh-pages" (que también ya creamos
anteriormente, porque somos gente muy prevenida...). Finalmente se
debe hacer un merge desde la rama **master** con la rama **gh-pages**
y subir todo al repositorio externo. Estos son los pasos mencionados:

.. code-block:: console

   (blogs)$ ghp-import output
   (blogs)$ git checkout master
   (blogs)$ git merge gh-pages
   (blogs)$ git push --all

Hay que esperar un rato hasta que el sitio esté accesible (sólo la
primera vez, las siguientes actualizaciones que se hagan permiten
acceder al nuevo contenido inmediatamente).

GitHub pregunta el nombre de usuario y la contraseña al hacer el push
al repositorio online. La página para acceder al blog es
http://nombreUsuario.github.io

Agregado de posts
=================

En sesiones posteriores, los nuevos posts se escriben con
restructuredText (o Markdown) y se deben guardar en el directorio
*content*, en la rama **source**. Tampoco hay que olvidarse de activar
el entorno virtual correcto para que funcione Pelican y las órdenes
como *make html* y *make serve*.

.. code-block:: console

   $ source /usr/local/bin/virtualenvwrapper.sh
   $ workon blogs
   (blogs)$ cd ~/misBlogs/nombreUsuario.github.io/
   (blogs)$ git checkout source
   (blogs)$ cd content

Con las órdenes anteriores se activó el entorno virtual, nos
aseguramos de estar en la rama **source** y llegamos al directorio
*content* que es donde debemos almacenar los archivos de contenido
(*.rst* o *.md*)

Generamos el blog y arrancamos el servidor local con:

.. code-block:: console

   (blogs)$ make html
   (blogs)$ make serve

Visitamos el blog con nuestro navegador en la dirección
http://localhost:8000

Si no estamos conformes detenemos el servidor local desde el terminal
con Ctrl-c Ctrl-c y luego de editar los cambios volvemos a ejecutar
*make html* y *make serve* (o utilizamos la alternativa de *make
regenerate* y *make serve* en dos terminales distintos, como expliqué
antes). Una vez que estemos conformes con el contenido tenemos que
ejecutar las siguientes órdenes para subir el blog al repositorio
externo:

.. code-block:: console

   (blogs)$ git add .
   (blogs)$ git commit -m "mensaje del commit"
   (blogs)$ ghp-import output
   (blogs)$ git checkout master
   (blogs)$ git merge -X theirs gh-pages
   (blogs)$ git push --all

Atención: navegación offline
============================

Para que la navegación offline sea posible se debe editar el archivo
pelicanconf.py y comentar/descomentar la linea *RELATIVE_URLS = True*.
Si la linea está habilitada (sin la marca de comentario *#*) entonces
se puede navegar sin contratiempos en el servidor local
(http://localhost:8000), de lo contrario los enlaces nos llevarán
fuera del servidor local y se cargarán las páginas alojadas en el
repositorio remoto.

Pero si usamos esta opción de las direcciones (url) relativas, para
que después no haya inconvenientes en el sitio externo
(http://nombreUsuario.github.io), se debe deshabilitar esta opción
antes de subir el sitio.

En otras palabras, no hay que olvidar de generar el sitio con *make
html* o *make regenerate* con la linea *RELATIVE_URLS = True*
deshabilitada, antes de subir nuestro blog al repositorio remoto. De
lo contrario, herramientas como Disqus (que se utiliza para gestionar
comentarios en cada entrada) tendrán dificultades de funcionamiento.

Problemas con GitHub
====================

Puede suceder que tras esperar media hora, luego de subir el sitio,
siga dando un mensaje de error (404) al intentar visitarlo en su
dirección final. Aparentemente esto puede evitarse si la subida se
realiza mediante SSH en vez de hacerlo mediante HTTP. Esto lo advertí
en las instrucciones de `Leonard Axelsson`_. Las instrucciones para
generar las llaves SSH (SSH keys) están en `esta ayuda de GitHub`_,
mientras que el cambio propiamente dicho se explica en `Changing a
remote's URL`_, también en GitHub.

.. _pueden verlo en este enlace: {filename}/2014-04-22-setear-blog-con-pelican-y-github.rst
.. _Changing a remote's URL: https://help.github.com/articles/changing-a-remote-s-url/
.. _esta ayuda de GitHub: https://help.github.com/articles/generating-ssh-keys/
.. _Leonard Axelsson: http://xlson.com/2010/11/09/getting-started-with-github-pages.html
.. _Nicholas Tan Jerome: http://ntanjerome.org/blog/how-to-setup-github-user-page-with-pelican/
.. _es este: http://pelican.readthedocs.org/
.. _la página de Nicholas: http://ntanjerome.org/blog/how-to-setup-github-user-page-with-pelican/
