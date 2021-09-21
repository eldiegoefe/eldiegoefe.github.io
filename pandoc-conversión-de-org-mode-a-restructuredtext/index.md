# Pandoc, conversión de org-mode a restructuredtext


Pandoc es un software para hacer conversión de archivos de texto entre distintos
lenguajes de markup. Me viene bien probarlo porque me gustaría escribir mis
entradas del blog desde org-mode (que uso con mucha frecuencia) y obtener el
mismo texto en versión restructuredText, que es el formato en el que escribo el
blog (con Pelican).

La instalación de Pandoc requirió un pequeño ajuste respecto de lo habitual en
Manjaro, ya que el programa no estaba disponible desde los repositorios que
vienen por defecto. Tuve que hacer los ajustes que se describen en [la wiki de
Arch](https://wiki.archlinux.org/index.php/ArchHaskell). Estos fueron los 5
pasos:

1.  Editar con permisos de administrador el archivo

``` console
/etc/pacman.conf
```

2.  Agregar esta entrada (en la parte donde se listan los repositorios):

``` console
[haskell-core]
Server = http://xsounds.org/~haskell/core/$arch
```

3.  Agregar claves para confiar en ese repositorio:

``` console
# sudo pacman-key -r 4209170B
# sudo pacman-key --lsign-key 4209170B
```

4.  Actualización de los paquetes

``` console
# sudo pacman -Syy
```

5.  Instalación propiamente dicha de pandoc (puede ser desde la
    aplicación gráfica Octopi).

