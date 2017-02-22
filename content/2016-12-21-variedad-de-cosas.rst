
:title: Variedad de cosas 01
:date: 2016-12-21 10:00
:category: blog
:tags: variedades
:author: El Diego Efe
:excerpt: Variedad de cosas 01
:disqus_identifier: Variedad de cosas 01
:status: draft

Entré a mirar la web de Digikam (el software para gestionar colecciones de
fotos) y me di cuenta que tengo instalada la versión 4.12 a pesar de que
permanentemente actualizo el software según me lo va indicando el gestor de
Linux Mint. La cuestión es que la rama 4 de Digikam no se actualiza más y para
instalar la versión 5 (que cambia el esqueleto interno del programa para que
dependa menos de KDE para lo cual se pasa a Qt5) hay que instalar otro PPA que
nos habilite a un sudo apt install digikam5 (noten el 5 al final de digikam).
Los pasos concretos serían:

$ sudo add-apt-repository ppa:philip5/extra
$ sudo apt update
$ sudo apt install digikam5


Instalación de ejecutables en Linux

Hay programas como el buscador pt (the platinum searcher) que son ejecutables
aislados, no pertenecen a un paquete y sólo se actualizará manualmente (hay que
acordarse). En StackExchange encontré un comentario (en la respuesta a la
pregunta `How can I make a program executable from everywhere`_ que me pareció
razonable y copio acá para recordarlo:

Unless I'm setting up a program that I expect other users to use, that's not
what I usually do: I create a bin directory just for me in my home directory,
and I edit my shell profile to add ~/bin/ to my PATH environment variable. I
find it easier to keep track of the programs I've installed that way, because it
is separated from the rest of the system.

Para agregar un directorio al path lo que hice fue modificar el archivo
~/.bash_profile y agregué esta linea:

..
   PATH=$PATH:~/bin:.

Significa que al path original (que desconozco cuál es, pero cuyo contenido está
en la variable $PATH) le agregué, siempre separando con dos puntos (:) el path
del nuevo directorio (~/bin) y de paso agregué también el path actual
(simbolizado con el punto). Esto último hace que al ejecutar un comando el
sistema también vea si éste se encuentra en el directorio actual. Para que el
cambio se realice hay que salir y volver a entrar al sistema (reloguearse).

.. _How can I make a program executable from everywhere: http://unix.stackexchange.com/questions/3809/how-can-i-make-a-program-executable-from-everywhere
