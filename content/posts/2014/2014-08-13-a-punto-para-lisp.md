---
title: A punto para Lisp
date: 2014-08-13T10:00:00
categories: [tecnicismos]
tags: [lisp, programacion, common-lisp]
author: Diego Efe
toc: false
---

Cuando empecé a leer [Practical Common Lisp](http://www.gigamonkeys.com/book/),
de Peter Seibel, tras escuchar [el reportaje de Sacha Chua a Bozhidar
Batsov](https://www.youtube.com/watch?v=-8DO0_pqLNA), tuve algunos
inconvenientes para poder instalar Lisp en mi compu, hasta que encontré el
tutorial [Installing Common Lisp](https://www.youtube.com/watch?v=VnWVu8VVDbI).
Estas notas resumen la información del video (sus instrucciones se muestran en
un entorno Windows mientras que mi transcripción es para Linux), para poder
instalar un Lisp en cualquier máquina con Emacs:


Allí dice que se puede [bajar sbcl](http://www.sbcl.org/platform-table.html)
(**elegir el binario**, de la tabla para las distintas plataformas, en mi caso
Linux AMD64, *que no implica que esa deba ser la marca de nuestro
microprocesador*) e instalarlo. Prestar atención a que el archivo bajado sea
efectivamente un binario (posee la palabra \"binary\" en el nombre, antes de la
extensión) y descomprimirlo, lo cual se hace con la orden:

``` console
# sh install.sh
```

(**necesita permisos de root**, así que hay que anteponer un sudo o
ejecutar el terminal como root). Al final aparecen algunos mensajes
diciendo que no se instalaron los manuales, pero más allá de eso todo
parece andar bien, puesto que en la ventana puede leerse:

``` console
SBCL has been installed:
 binary /usr/local/bin/sbcl
 core and contribs in /usr/local/lib/sbcl/
```

Luego hay que [bajar quicklisp](http://www.quicklisp.org/beta/), el
hecho de que sea \"beta\" no importa, porque anda bien así desde hace
años.

Luego hay que ejecutar esto:

``` console
$ sbcl --load quicklisp.lisp
```

Luego hay que seguir las instrucciones que aparecen, primeramente
teclear (el prompt dentro de Lisp en mi sistema es sólo un asterisco):

``` cl
* (quicklisp-quickstart:install)
```

El sistema se pone a bajar cosas, así que supongo que es necesaria la
conexión a internet. Finaliza con este mensaje:

``` console
==== quicklisp installed ====

   To load a system, use: (ql:quickload "system-name")

   To find systems, use: (ql:system-apropos "term")

   To load Quicklisp every time you start Lisp, use: (ql:add-to-init-file)

   For more information, see http://www.quicklisp.org/beta/

NIL
```

Seguimos ejecutando en el mismo terminal la siguiente instrucción:

``` cl
* (ql:add-to-init-file)
```

Funciona independientemente del directorio desde el cual hayamos
ejecutado el terminal. Ofrece el siguiente mensaje como resultado:

``` console
I will append the following lines to #P"/home/diego/.sbclrc":

  ;;; The following lines added by ql:add-to-init-file:
  #-quicklisp
  (let ((quicklisp-init (merge-pathnames "quicklisp/setup.lisp"
                                         (user-homedir-pathname))))
    (when (probe-file quicklisp-init)
      (load quicklisp-init)))

Press Enter to continue.

#P"/home/diego/.sbclrc"
```

Luego se instala slime, pero no como hacía yo desde adentro de emacs,
sino desde el mismo terminal en el que venimos trabajando:

``` console
* (ql:quickload "quicklisp-slime-helper")
```

Nuevamente se pone a bajar cosas de la red y termina con el siguiente
mensaje, así que sabemos que lo hizo exitosamente:

``` console
slime-helper.el installed in "/home/diego/quicklisp/slime-helper.el"

To use, add this to your ~/.emacs:

  (load (expand-file-name "~/quicklisp/slime-helper.el"))
  ;; Replace "sbcl" with the path to your implementation
  (setq inferior-lisp-program "sbcl")


("quicklisp-slime-helper")
*
```

Yo no tengo archivo \~/.emacs porque instalé Prelude, así que esas tres
lineas (desde **(load** hasta **\"sbcl\")**) van en el archivo de
configuraciones personales *\~/.emacs.d/personal/custom.el*. No hace
falta cambiar nada, es un copy+paste, o mejor dicho un kill+yank.

Al ejecutar emacs correrá brevemente el script que acabamos de decirle
que corra.

Podemos abrir (visitar en la jerga de emacs) un nuevo archivo con
extensión .lisp usando C-x C-f. Luego, en otro buffer, puedo hacer M-x
slime. Da como resultado una máquina REPL como la que se espera en los
ejemplos del capítulo 2 de Practical Common Lisp.

``` cl
; SLIME 2014-06-17
CL-USER>
```

Al principio había algo diferente en el video, porque cuando se pone a
teclear en el otro buffer, el que tiene el archivo de texto con
extensión .lisp no me aparecían en el minibuffer las ayudas (una
descripción de lo que se va tecleando, con la sintaxis sugerida), sin
embargo, luego empezó a funcionar igual, también con el coloreado de las
palabras clave.

Aca una versión del Hola, Mundo! para probar en el archivo .lisp (se
compila con C-c C-c):

``` cl
(defun hihi-world ()
  (format t "hola mundo!"))
```
