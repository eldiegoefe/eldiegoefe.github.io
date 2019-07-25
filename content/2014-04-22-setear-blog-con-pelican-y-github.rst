Blog con Pelican y GitHub
#########################

:date: 2014-04-22 10:00
:category: tecnicismos
:tags: tutorial, blog, git, pelican
:author: El Diego Efe
:excerpt: Instrucciones para setear y actualizar blog con Pelican y
          GitHub Personal Pages
:disqus_identifier: blog con pelican y github

Actualización
=============

Pueden ver una actualización de estas instrucciones en `en este nuevo post`_

.. _en este nuevo post: {filename}/2015-05-20-actualizacion-de-instrucciones-para-blog-con-pelican.rst


Instrucciones
=============

El sitio con las intrucciones sobre Pelican `es este`_. Casi todo el
contenido siguiente está basado en las instrucciones de `Nicholas Tan
Jerome`_. Para instalar Pelican se puede usar "pip", más adelante hay
más detalles, pero como referencia veloz basta decir que se puede
hacer sencillamente (en la rama "source" y desde el ENV que se creará
más adelante):

.. code-block:: console

   (ENV) $ pip install pelican

La idea para trabajar Pelican con Git es tener un directorio para el
repositorio con el nombre de la página, y dentro de él un directorio
para el virtualenv donde va a correr el Pelican. Por ejemplo, algo así
(más adelante se explica en qué ramas del repositorio se almacenará el
código fuente del sitio, y las páginas del blog propiamente dichas):

.. code-block:: console

   $ ~/documentos/nombreUsuario.github.io      # para el sitio
   $ ~/documentos/nombreUsuario.github.io/ENV  # para el env

Primero armo un repositorio (vacío) en GitHub para alojar mi blog
personal. GitHub ofrece la dirección nombreUsuario.github.io con este
propósito. Luego clono el sitio en un directorio local donde se desea
mantener el blog:

.. code-block:: console

   $ cd ~/documentos
   $ git clone https://github.com/nombreUsuario/nombreUsuario.github.io

Como el repositorio lo creé vacío, sin más que el README.md, entonces
éste es el único archivo que existe en el directorio
~/documentos/nombreUsuario.github.io

Para instalar el virtualenv (medio ambiente virtual) en el directorio
deseado:

.. code-block:: console

   $ virtualenv ~/documentos/nombreUsuario.github.io/ENV
   $ cd ~/documentos/nombreUsuario.github.io/ENV
   $ . bin/activate


La última instrucción puede reemplazarse por "source ENV/bin/activate"

Esas instrucciones dejan el entorno listo con un Python funcional (y
sus librerías). Los directorios instalados dentro de ENV son:

- bin
- include
- lib
- lib64

La última orden (. bin/activate) activa este entorno y cambia el
prompt (que aparecerá precedido de ENV).

El directorio ENV no necesita ser mantenido en el repositorio de
GitHub (eso sí, si se trabaja el blog desde distintas computadoras,
hay que tenerlo instalado en cada una), así que conviene agregarlo al
.gitignore con la siguiente linea en ese archivo (**igual finalmente
lo saqué, así al clonar el repositorio del blog en una computadora
nueva no lo tengo que instalar**):

- ENV/

Tampoco interesa mantener los archivos de backup así que también
se puede agregar este renglón:

- \*~

Con git status veremos que estamos en la rama "master" y que falta el
commit para agregar el archivo .gitignore. Entonces hacemos:

.. code-block:: console

   (ENV) $ git add .
   (ENV) $ git commit -m "Commit inicial"


Nuestra rama local de master queda adelantada respecto de la rama
master en el repo externo. Esto lo avisa el sistema ante la última
orden ingresada.

Dado que al repositorio externo no vamos a necesitar subir los
archivos de Pelican y los que surjan de la configuración del sitio,
entonces instalamos este programa en una nueva rama que llamaré
"source":

.. code-block:: console

   (ENV) $ git branch source
   (ENV) $ git checkout source


(alternativamente estas dos instrucciones se pueden condensar en una
sola: git checkout -b source)

Para instalar Pelican hay 3 opciones (y no hay que olvidarse que se
instala en el ENV). Hay que estar atento a que no haya errores, porque
sino se instala mal y, por ejemplo, más tarde puede no funcionar "make
serve".

.. code-block:: console

   (ENV) $ pip install pelican     # opción 1
   (ENV) $ easy_install pelican    # opción 2
   (ENV) $ pip install -e git://github.com/getpelican/pelican#egg=pelican


La primera vez tras la instalación se debe ejecutar la orden
**pelican-quickstart** para configurarlo (va el guión entre las dos
palabras). Tras ese comando, y tras contestar todas las preguntas que
aparecen, no solamente se guarda la configuración deseada (en los
archivos pelicanconfig.py y publishconf.py), sino que se generan todos
los archivos que Pelican necesita (incluso dos directorios nuevos:
content y output). El site url que elijo es
http://nombreUsuario.github.io

El contenido de pelicanconf.py tras responder a las preguntas de
pelican-quickstart y además editar manualmente el archivo para
completar los datos, queda así:


.. code-block:: python
   :linenos:

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
   :linenos:

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

Guardo un post armado en Markdown o restructuredText dentro del
directorio content, así cuando vaya a generar el sitio voy a tener un
contenido (para que ver algo cuando cargue el blog).

Genero el sitio con make html (procesa todos los archivos del
directorio content y aloja el sitio resultante en el directorio
output) y ejecuto el servidor local con make serve:

.. code-block:: console

   (ENV) $ make html
   (ENV) $ make serve

El sitio lo puedo visitar en http://localhost:8000. Veo que tiene un
problema para encontrar el CSS, no sale bien formateado. Sin embargo,
luego cuando subo el sitio al repositorio externo, corroboro que la
página carga bien.

Una alternativa, que permite que la edición se refleje inmediatamente
en el sitio, es usar la siguientes dos instrucciones, la primera
combina *make html* junto con *make serve* (el sitio se regenera ante
cualquier edición de su contenido, y permanece accesible en el
localhost) y la segunda es para detener el servicio.

.. code-block:: console

   (ENV) $ make devserver
   (ENV) $ ./develop_server.sh stop


Voy a agregar todo al branch source:

.. code-block:: console

   (ENV) $ git add .
   (ENV) $ git commit -m "Commit inicial de la rama source"


Lo que sigue es casi textual de la página de `la página de Nicholas`_,
se explica como hacer push del sitio al repositorio externo:

Supongamos estar en la rama "source". Lo que se verá al acceder al
blog, es lo que esté en la rama "master", así que hay que copiar allí
las páginas html de la carpeta output. Nicholas propone usar un script
llamado ghp-import para facilitar esa tarea. Este script exporta el
contenido de la carpeta que se menciona en la linea de comandos (al
ejecutarlo) hacia la rama "gh-pages". Por eso es necesario durante la
puesta a punto inicial, crear una rama con ese nombre antes de correr
el script, y luego hacer un merge desde la rama "master" con la rama
"gh-pages"

Si no está instalado ghp-import, se puede instalar con:

.. code-block:: console

   (ENV) $ pip install ghp-import


Finalmente, eston son los pasos restantes:

.. code-block:: console

   (ENV)$ git branch gh-pages   # crea la rama gh-branches
   (ENV)$ ghp-import output     # exporta la carpeta output desde la rama actual (source) hacia la rama gh-pages
   (ENV)$ git checkout master   # cambia el head a la rama master
   (ENV)$ git merge gh-pages    #
   (ENV)$ git push --all        #


Cuando hice el merge creo que no estaba más .gitignore en la rama
master. Así que lo creé de vuelta, tuve que agregarlo y comitearlo.

Hay que esperar un rato hasta que el sitio esté accesible (sólo la
primera vez, las siguientes actualizaciones que se hagan permiten
acceder al nuevo contenido inmediatamente).

Se podría hacer un push que incluya sólo el contenido de la rama
"master", pero hacer un push de todas las ramas no molesta a nadie.

GitHub pregunta el nombre de usuario y la contraseña al hacer el push
al repositorio online.

La página para acceder al blog es nombreUsuario.github.io

Agregado de posts
-----------------

Al agregar nuevos posts (hechos con restructuredText o Markup, que
deben ser guardados en el directorio "content") es necesario efectuar
los siguientes pasos (suponiendo que uno está actualmente en la rama
"source":

.. code-block:: console

   $ cd /path/to/blog/ENV
   $ . bin/activate    # activa el entorno para que funcionen los progs de python (make serve, ghp-import, etc)
   (ENV)$ make html             # genera los archivos html que van a la carpeta "output"
   (ENV)$ ghp-import output     # exporta la carpeta output desde la rama actual (source) hacia la rama gh-pages
   (ENV)$ git add .             # sin add y commit no podremos cambiar a otra rama
   (ENV)$ git commit -m "mensaje del commit"
   (ENV)$ git checkout master   # cambia el head a la rama master
   (ENV)$ git merge gh-pages    #
   (ENV)$ git push --all        #

.. _Nicholas Tan Jerome: http://ntanjerome.org/blog/how-to-setup-github-user-page-with-pelican/
.. _es este: http://pelican.readthedocs.org/en/3.3.0
.. _la página de Nicholas: http://ntanjerome.org/blog/how-to-setup-github-user-page-with-pelican/


Ultimos detalles
----------------

Para usar el tema Elegant hay que instalar Beautiful Soup y para usar
el plugin que permite `embeber videos de youtube`_  hay que instalarlo:

.. code-block:: console

   (ENV) $ pip install beautifulsoup4
   (ENV) $ pip install pelican-youtube

.. _embeber videos de youtube: https://pypi.python.org/pypi/pelican_youtube


Problemas con GitHub
--------------------

Puede suceder que tras esperar media hora, luego de subir el sitio,
siga dando un mensaje de error (404) al intentar visitarlo en su
dirección final. Aparentemente esto puede evitarse si la subida se
realiza mediante SSH en vez de hacerlo mediante HTTP. Esto lo advertí
en las instrucciones de `Leonard Axelsson`_. Las instrucciones para
generar las llaves SSH (SSH keys) están en `esta ayuda de GitHub`_,
mientras que el cambio propiamente dicho se explica en `Changing a
remote's URL`_, también en GitHub.

.. _Changing a remote's URL: https://help.github.com/articles/changing-a-remote-s-url/
.. _esta ayuda de GitHub: https://help.github.com/articles/generating-ssh-keys/
.. _Leonard Axelsson: http://xlson.com/2010/11/09/getting-started-with-github-pages.html
