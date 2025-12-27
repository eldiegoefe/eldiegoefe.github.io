---
title: Más sobre blogs con Pelican
date: 2015-04-10T10:00:00
categories: [blog]
tags: [blog, pelican]
author: Diego Efe
---

Hace algún tiempo escribí sobre el modo de [poner en marcha un blog usando
Pelican](%7Cfilename%7C/2014-04-22-setear-blog-con-pelican-y-github.rst). Con un
poco más de experiencia vuelvo a comentar algunas variaciones, como para más
adelante condensar los pasos en un artículo corregido y aumentado (o disminuido,
dado que la idea es simplificar).

Usar entornos virtuales de Python es muy sencillo, tanto que me
acostumbré (y hasta disfruto) de realizar instalaciones de diversos
programas usándolos. Entre ellos, Pelican. La ventaja es que queda un
entorno encapsulado que no se modifica con las actualizaciones del
sistema. Se puede tener, por ejemplo, un entorno con Python 3 mientras
en el sistema está instalada la versión 2.

## 1. Instalación del motor de los entornos virtuales

Para armar uno de estos entornos es necesario contar con
**python-virtualenv** en el sistema. En Arch y Manjaro:

``` console
$ sudo pacman -S python-virtualenv
```

Asegurarse de que también **python-pip** está instalado, porque se
necesita para el próximo paso:

``` console
$ sudo pacman -S python-pip
```

Manipular entornos virtuales se puede hacer con python-virtualenv sin
más, pero es más fácil aún con **virtualenvwrapper**, que puede
instalarse con pip (a nivel del sistema):

``` console
$ sudo pip install virtualenvwrapper
```

## 2. Creación de un entorno virtual

Para crear un entorno primero nos aseguramos de ejecutar
virtualenvwrapper:

``` console
$ source /usr/bin/virtualenvwrapper.sh
```

Alternativamente, si este script estuviese en el PATH hubiese bastado
con ejecutar:

``` console
$ virtualenvwrapper
```

Luego creamos el entorno virtual, con un intérprete de Python igual al
que se ejecuta por defecto en nuestro sistema:

``` console
$ mkvirtualenv nombredelentorno
```

Por defecto (si no se aclara otro directorio), los distintos entornos
que se vayan creando se almacenan en **\~/.virtualenvs/**. La [página de
referencia de
virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html)
es muy buena para consultar todas las opciones de los comandos
(mkvirtualenv, cdvirtualenv, etc).

Si, por ejemplo, queremos especificar una versión de Python en
particular, primero nos aseguramos de saber dónde se encuentra ésta:

``` console
$ whereis python3
/usr/bin/python3
```

La instalación de un nuevo entorno virtual con esta versión se ejecuta
así:

``` console
$ mkvirtualenv --python=/usr/bin/python3 nombredelentorno
```

Como resultado de la ejecución de **mkvirtualenv**, además de
instalarse, el entorno virtual se activa, con lo cual el prompt del
shell pasa a verse así:

``` console
(nombredelentorno)$
```

Al reiniciar el sistema, para activar el entorno hay que ejecutar
primero virtualenvwrapper y luego usar el comando **workon**:

``` console
$ source /usr/bin/virtualenvwrapper.sh
$ workon nombredelentorno
```

## 3. Instalación de Pelican y otros módulos

Los pasos finales son muy sencillos (ejecutarlos sin sudo para que la
instalación ocurra dentro del entorno virtual y no a nivel del sistema):

``` console
(nombredelentorno)$ pip install pelican
(nombredelentorno)$ pip install beautifulsoup4
(nombredelentorno)$ pip install pelican_youtube
(nombredelentorno)$ pip install ghp-import
```

## 4. Instalación de Plugins de Pelican

Algunos temas de Pelican requieren el uso de plugins que se instalan en
el directorio desde donde se ejecute la orden siguiente:

``` console
$ git clone --recursive https://github.com/getpelican/pelican-plugins
```

## 5. Desactivar el entorno virtual

Cuando no hay más por hacer dentro del entorno virtual, éste se
desactiva cerrando el terminal o ejecutando:

``` console
(nombredelentorno)$ deactivate
```
