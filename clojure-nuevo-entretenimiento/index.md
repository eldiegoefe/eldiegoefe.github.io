# Clojure, nuevo entretenimiento


En el mundo Emacs se menciona bastante el lenguaje Clojure, como un dialecto de Lisp que corre sobre el Java Virtual Machine, lo cual constituye para mi un dato casi completamente inutil, puesto que desconozco Java y su JVM. De cualquier manera, mientras continúo leyendo ANSI Common Lisp, me dieron ganas de probar, así que guardo aquí las instrucciones de instalación para usar Clojure con Emacs en Linux.

La cuestión no es tan complicada, primero verificamos desde un terminal
que Java está instalado:

``` console
$ java -version
java version "1.7.0_65"
OpenJDK Runtime Environment (IcedTea 2.5.2) (Arch Linux build 7.u65_2.5.2-3-x86_64)
OpenJDK 64-Bit Server VM (build 24.65-b04, mixed mode)
```

Como en mi caso obtuve el mensaje precedente, no me tuve que preocupar
de instalar Java.

Las instrucciones de instalación están en [Clojure with
Emacs](http://clojure-doc.org/articles/tutorials/emacs.html). En
resumen, lo que hice fue visitar la página de
[Leiningen](http://leiningen.org/) y entonces:

-   Bajar el script de bash (de nombre \"*lein*\")
-   Copiarlo en una carpeta (*\~/programas/lein/*)
-   Ir a */usr/bin* y crear allí un symlink a lein (con \"*sudo ln -s
    \~/programas/lein/lein*\"). El directorio /usr/bin está en el PATH
    así que todo lo que ahí se almacena puede ser encontrado para su
    ejecución. El symlink guardado allí apunta al programa en la
    dirección donde lo guardamos, así que ahora podremos ejecutar lein
    desde cualquier lugar.
-   Pero aún falta volver ejecutable el script (con \"*chmod a+x
    lein*\")
-   Finalmente hay que ejecutar lein, lo cual hace que se baje Leiningen
    y se instale en el directorio *\~/.lein*.

El directorio creado originalmente (\~/programas/lein) debe permanecer
porque allí sigue estando lein, que se ejecutará siempre que se cree un
proyecto (lo que se baja en \~/.lein no lo sustituye).

*Agregado*: no hace falta copiar *lein* en un directorio como
*\~/programas/lein/* y luego armar un symlink desde */usr/bin*, se puede
directamente copiar lein en este último y listo.

En Emacs instalé CIDER, y además como tengo Prelude habilité en el
archivo prelude-modules.el la linea (require \'prelude-clojure). Así que
si no lo instalaba yo, el mismo Prelude hubiese bajado CIDER.

El tutorial de Clojure with Emacs indica que hay que ejecutar estas dos
órdenes desde un terminal (el resultado es la creación de un proyecto
llamado *command-line-args* dentro de un subdirectorio que se ubica
dentro del directorio actual en que se encuentra el terminal):

``` console
$ lein new command-line-args
$ cd command-line-args
```

Luego desde Emacs se abre el archivo /command-line-args/project.clj y se
lo edita para agregar al texto que ya tiene, la siguiente linea (siempre
según el tutorial):

``` clojure
:profiles {:dev {:plugins [[cider/cider-nrepl "0.7.0"]]}}
```

Hay que cambiar la versión que allí se coloca, puesto que ya no será la
\"0.7.0\". En el [github de
cider-nrepl](https://github.com/clojure-emacs/cider-nrepl) figura la
última versión. Una vez que hayamos agregado esta linea hay que guardar
el archivo y hacer desde allí mismo **M-x cider-jack-in**. Si todo va
bien se abre un buffer con el prompt del repl.

Tuve que dar varias vueltas hasta que esto último funcionó porque
aparecían mensajes de error antes de abrir el buffer o en el mismo
buffer. Lo que sucede es que debe coincidir la versión del cider-nrepl
con la versión de cider instalada. Cuando sustituía \"0.7.0\" por
\"0.8.2\" daba un mensaje diciendo que no encontraba esa versión para
bajar desde los repositorios y cuando intentaba con \"0.8.1\" me decía

    WARNING: CIDERs version (0.8.2-snapshot) does not match cider-nrepl version (0.8.1)

Todo se solucionó cuando en vez de poner \"0.8.2\" escribí
\"0.8.2-SNAPSHOT\" (por eso hay que prestar atención a cuál es la
versión de CIDER que está instalada y copiar el mismo código, el cual
seguramente coincide con la versión que indica el [github de
cider-nrepl](https://github.com/clojure-emacs/cider-nrepl)). Y **ojo, es
todo con mayúsculas**, no importa cómo aparezca la versión de CIDER. Y
voilá:

``` clojure
; CIDER 0.8.2alpha (package: 20141126.715) (Java 1.7.0_65, Clojure 1.6.0, nREPL 0.2.6)
user>
```

Para averiguar la versión instalada de cider:

``` terminal
M-x cider-version
```

## Un nuevo comienzo

Ahora, con todo listo para usarse, podemos seguir algún tutorial, como
el de [Clojure for the brave and true](http://www.braveclojure.com/). El
primer capítulo ya nos permite probar las cosas más básicas, como armar
un proyecto nuevo con *lein*, armar el ejecutable java para distribuir,
y jugar con el repl.

