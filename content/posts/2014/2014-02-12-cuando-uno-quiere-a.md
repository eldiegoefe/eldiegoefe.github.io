---
title: Cuando uno quiere A y termina haciendo B
date:  2014-02-12T10:30:00
lastmod: 2015-02-11T10:30:00
categories: [tecnicismos]
tags: [boot, instalacion, windows, grub]
author: Diego Efe
featuredImagePreview: https://live.staticflickr.com/65535/51501594746_629515728e.jpg
---

Estoy leyendo sobre [IPython](http://ipython.org/), que instalé en
Windows a través de
[Anaconda](https://store.continuum.io/cshop/anaconda/).

Durante ese viaje me enteré de que Windows tiene dos shells, el más viejo y
limitado es \'cmd.exe\' mientras que el recomendado es \'Windows PowerShell\',
ya que tiene los mismos comandos que Unix. En cualquiera de los dos, IPython se
corre con la orden *ipython*

Hay ayudas de IPython en:

-   [Documentación Oficial](http://ipython.org/documentation.html)
-   [StackOverflow](http://stackoverflow.com/questions/tagged/ipython)
-   [Lista de
    correos](http://mail.scipy.org/mailman/listinfo/ipython-user)

¡Debe haber muchas más!

## Sos un nabo. Crónica de una batalla menor.

Mientras leía sobre Python un pájaro carpintero taladraba mi cabeza
repitiéndome: *sos un nabo, todavía no pudiste reinstalar Linux*. Por lo
cual debí poner manos a la obra para brindarle un hogar al Pingüino.
Tras infructuosos intentos de instalación de [Linux
Mint](http://www.linuxmint.com/) en sus versiones Mate y Cinnamon usando
[YUMI -- Multiboot USB
Creator](http://www.pendrivelinux.com/yumi-multiboot-usb-creator/) como
instalador de LiveUSB, cosa que muchas veces me había funcionado
perfecto en el pasado, terminé absorto en la lectura de sitios sobre el
nuevo estándar de booteo UEFI, instrucciones sobre habilitaciones y
deshabilitaciones de CSM (Compatibility Support Module) y otras términos
de Magia Oscura. Finalmente terminé optando por instalar
[Fedora](https://fedoraproject.org/) en su versión 20 y leyendo sobre
las recomendaciones de particionado que son distintas a las de Linux
Mint. No fue sencillo, finalmente decidí dejar el disco de estado sólido
de 128 GB exclusivamente destinado a Windows, y permitir que el
instalador de Fedora organice las particiones que se le ocurra armar por
defecto en el disco de 500 GB, por lo cual todo ese disco recibió un
backup ya que todos los archivos se iban a perder con el formateo. *Lo
bueno es que tras raspar y raspar las superficies de las paredes con las
que nos golpeamos la cabeza siempre algo se termina aprendiendo*.

Ahí descubrí que no todas las distribuciones requieren la misma organización en
el disco rígido. Linux Mint arma dos particiones para funcionar: la partición
*[root]* que es el punto de montaje básico de todo el sistema de archivos
**/**) y la partición *[swap]*. A esto Fedora le agrega una partición
*[boot]* de 500 MB, y una partición *[efi]*, ubicada en **/boot/efi** de 200 MB
\--ambas obviamente para el arranque del sistema\-- y esto es lo interesante,
también una *partición del usuario* en **/home** donde se guardaran todos los datos
(música, documentos, descargas, etc), de modo tal que cuando se necesite
reinstalar el sistema no se pierdan. Esto es lo mismo que conviene hacer con
Windows, instalar una *partición del sistema* (Disco C) y armar otra para los
datos (Disco D).
