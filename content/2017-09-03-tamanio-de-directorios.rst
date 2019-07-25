Peso de los directorios en Linux
################################

:date: 2017-09-03 10:00
:category: tecnicismos
:tags: linux
:author: El Diego Efe
:excerpt: Peso de los directorios en Linux
:disqus_identifier: Peso de los directorios en Linux

Se me está por llenar el disco rígido externo, donde tengo fotos, películas,
documentos y demás. Un terabyte de porquerías, pero nada que quiera borrar. ¿O
sí? Ir directorio por directorio es tedioso y puede volverse una tarea
abrumadora si aparecen muchos subdirectorios anidados con incierto contenido
dentro de los mismos.

Se puede usar el comando *du* para obtener el tamaño de los directorios y
encadenarlo con un *sort* para que el resultado aparezca ordenado por el tamaño
de los mismos:

.. code-block:: terminal

   $ du -sh * | sort -hr

   368G	Vídeos
   178G	blogs
   41G	Descargas
   5,1G	VirtualBox VMs
   4,2G	Documentos
   2,2G	Imágenes
   1,5G	sistemas-operativos
   611M	calibre
   219M	opt
   143M	programas
   4,4M	bin
   3,2M	org
   1,9M	mis-proyectos
   1,1M	mis-configs
   744K	ordenar
   452K	temp
   8,0K	usr
   4,0K	Público
   4,0K	Plantillas
   4,0K	Música
   4,0K	Escritorio

Pero en StackExchange por supuesto que está la pregunta `How do I get the size
of a directory on the command line?`_ y entre las respuestas alguien sugería
usar *ncdu*, que es una versión con interfaz gráfica, y que además permite
navegar por los directorios, lo cual facilita encontrar aquellos que ocupan
mucho espacio.

En Debian, Ubuntu, Mint y semejantes se instala sencillamente con:

.. code-block:: terminal

   $ sudo apt-get install ncdu

Al ejecutarse, el programa lee todos los directorios a partir del directorio
local (desde el cual se está ejecutando), y al finalizar la lectura presenta una
pantalla como la que aparece debajo (click sobre ella para verla más grande).
Con la tecla *?* aparece una ayuda que indica las teclas que permiten la
navegación, seleccionar diferentes criterios de ordenamiento (por nombre, por
tamaño, etc), elegir el modo en que se presentan los porcentajes y también se
pueden borrar directorios (con la tecla *d*).

.. image:: https://c1.staticflickr.com/5/4352/36200585553_aaf8edc5de_b.jpg
   :scale: 100%
   :width: 100%
   :align: center
   :alt: pantalla de ncdu 
   :target: https://c1.staticflickr.com/5/4352/36200585553_532f72d9d6_o.png

.. _How do I get the size of a directory on the command line?: https://unix.stackexchange.com/questions/185764/how-do-i-get-the-size-of-a-directory-on-the-command-line

 
