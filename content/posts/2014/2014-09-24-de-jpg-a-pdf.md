---
title: De jpg a pdf
date: 2014-09-24T10:00:00
categories: [tecnicismos]
tags: [imagenes, pdf]
author: Diego Efe
toc: false
---

Encontré una muy sencilla aplicación para convertir archivos de imágenes. Si
bien tiene mucha potencia, porque puede hacer mucho más, yo la usé para
convertir imágenes en páginas de un archivo pdf.

Se necesita tener instalado un paquete llamado **imagemagick**. Para instalarlo
desde un terminal dependerá de la distribución, suele ser así:

``` bash
$ sudo urpmi imagemagick             # desde mageia
$ sudo apt-get install imagemagick   # desde ubuntu, mint, etc
$ sudo yum install imagemagick       # desde fedora
```

Luego, para usarlo, también desde un terminal y en el directorio donde
están guardadas las imágenes, se ejecuta **convert** (parece que no es
lo único que instala **imagemagick**):

``` bash
$ convert imagen.jpg archivo.pdf
```

Se pueden incluir varias imágenes en un mismo archivo:

``` bash
$ convert imagen1.jpg imagen2.jpg imagen3.jpg archivo.pdf
```

E incluso generalizar con asteriscos:

``` bash
$ convert imagen*.jpg archivo.pdf
```

Hay muchos ejemplos más en [Desde
Linux](http://blog.desdelinux.net/como-manipular-imagenes-desde-el-terminal/).
Y también más información haciendo **man convert** desde el terminal.
