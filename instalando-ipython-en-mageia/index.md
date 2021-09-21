# Instalando IPython en Mageia

Para instalar IPython en Mageia, sin tener privilegios de root hay que cumplir con los siguientes pasos:

- Contar con privilegios de root para poder correr el instalador
- Hay que instalar PIP
- Con PIP instalar IPython
    
## Trabajar como root:

Conviene agregar el usuario a la lista de usuarios con privilegios para
ejecutar *sudo*. Las instrucciones están en [Configuring
sudo](https://wiki.mageia.org/en/Configuring_sudo) de Mageia.
Históricamente en UNIX este es el grupo Wheels.

Primero hay que crear el archivo */etc/sudoers.d/01wheel*

Después ejecutar lo siguiente en un terminal como root (es decir, luego
de hacer /usr/bin/su):

``` console
$ echo "%wheel ALL=(ALL)  ALL" > /etc/sudoers.d/01wheel
$ chmod 440 /etc/sudoers.d/01wheel
```

Agregar el usuario al grupo \"Wheel\". Para ello hay que editar el
usuario (desde Configure su computador / Administrar usuarios del
sistema). Click derecho para el menú contextual sobre el nombre del
usuario a agregar y *editar*. En la pestaña de grupos agregar un tick
sobre el grupo **wheel** y aceptar.

Desloguearse y volver a entrar (en caso que el usuario modificado sea el
usuario que hizo la edición).

**IMPORTANTE**: para mejorar la seguridad del sistema conviene usar sudo
o su siempre precedidos de la ruta real al comando (la explicación
completa verla en el link original), es decir:

``` console
$ /usr/bin/sudo *comando*
$ /usr/bin/su *comando*
```

## Instalación de PIP

Esto es muy fácil:

``` console
$ /usr/bin/sudo urpmi python-setuptools
$ /usr/bin/sudo easy_install pip
```

## Instalación de IPython

Igual de fácil:

``` console
$ /usr/bin/sudo pip install ipython
```

