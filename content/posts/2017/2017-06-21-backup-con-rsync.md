---
title: Backup con RSync
date: 2017-06-21T10:00:00
categories: [tecnicismos]
tags: [rsync, backup, linux]
author: Diego Efe
disqus_identifier: Backup con RSync
featuredImagePreview: https://live.staticflickr.com/65535/51493029653_c6de021d3a.jpg
toc: false
---

RSync es un programa que permite copiar archivos, pero a diferencia de un
copiado común, compara los archivos de origen y destino y sólo realiza la
transferencia de la diferencia entre ambos: si son iguales no transfiere nada,
si es un archivo de texto y se agregó sólo un caracter, RSync envía unicamente
ese caracter y reconstruye el archivo en el destino para que ambas copias sean
exactamente iguales. De este modo el procedimiento es más eficiente, en
particular si se copian archivos grandes. La copia se puede realizar entre
cualquier directorio de origen y destino, ya sea que se encuentren en un mismo
disco rígido, en diferentes discos en una misma computadora o también entre una
máquina local y una remota (o viceversa).

Poder copiar de este modo es óptimo para realizar backups de nuestros
datos. Como se pueden copiar directorios recursivamente entonces es muy
facil, por ejemplo, mantener una copia actualizada de una colección de
fotos, que generalmente tiene muchos subdirectorios para almacenar
imágenes ordenadas por fecha o por temática. Es RSync el que compara el
contenido de cada subdirectorio, y por ejemplo si le cambiamos el
contraste a una foto, lo detecta y actualiza en la copia de destino. Nos
ahorra tener que identificar cuál es el archivo que procesamos, y todo
con una sola linea de comandos, que ya veremos\...

Primero tenemos que saber la ubicación de los archivos que queremos
copiar y el camino hacia el lugar donde haremos la copia. Para esta
tarea podemos usar el comando df, que muestra el espacio libre en cada
sistema de archivos que se encuentra montado en el sistema y también
informa el punto de montaje. El modificador *-h* (la forma corta de
*\--human-readable*) ofrece el resultado en potencias de 1024.

``` console
$ df -h

S.ficheros     Tamaño Usados  Disp Uso% Montado en
udev             3,9G      0  3,9G   0% /dev
tmpfs            784M   9,7M  775M   2% /run
/dev/sda4         49G    23G   24G  50% /
tmpfs            3,9G   237M  3,6G   7% /dev/shm
tmpfs            5,0M   4,0K  5,0M   1% /run/lock
tmpfs            3,9G      0  3,9G   0% /sys/fs/cgroup
/dev/sda2        1,3G   500M  705M  42% /boot
/dev/sda5        853G   402G  408G  50% /home
cgmfs            100K      0  100K   0% /run/cgmanager/fs
tmpfs            784M    16K  784M   1% /run/user/1001
/dev/sdc1        932G   912G   21G  98% /media/diego/biblioteca
```

En el ejemplo pueden ver mi directorio de origen (que son archivos
ubicados en /home) y el destino será algún subdirectorio en el disco
rígido externo, que se encuentra montado en /media/diego/biblioteca (me
está quedando poco espacio\...).

También se puede utilizar el comando *lsblk* para obtener información
sobre los discos montados:

``` terminal
$ lsblk

NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda      8:0    0 931,5G  0 disk 
├─sda1   8:1    0    20M  0 part 
├─sda2   8:2    0   1,3G  0 part /boot
├─sda3   8:3    0  15,3G  0 part [SWAP]
├─sda4   8:4    0    49G  0 part /
└─sda5   8:5    0 865,9G  0 part /home
sdb      8:16   0 119,2G  0 disk 
├─sdb1   8:17   0   100M  0 part 
├─sdb2   8:18   0 118,7G  0 part 
└─sdb3   8:19   0   450M  0 part 
sdc      8:32   0 931,5G  0 disk 
└─sdc1   8:33   0 931,5G  0 part /media/diego/biblioteca
sdd      8:48   0 931,5G  0 disk 
```

Generalmente el comando RSync se ejecuta con estos modificadores:

``` terminal
$ rsync -avh --progress --delete /desde /hacia
```

Donde:

-   **a**: archive, es un modificador que se usa generalmente. Es una
    abreviatura para no tener que poner todos estos otros modificadores
    -rlptgoD. Sirve para asegurar que en la transferencia se preserven
    los symbolic links, dispositivos, atributos, permisos, ownerships,
    etc.
-   **v**: verbose
-   **h**: human readable.
-   **progress**: muestra el progreso de la transferencia.
-   **delete**: borra los archivos en destino que no están en el origen.
-   **/desde**: directorio de origen
-   **/hacia**: directorio de destino

Leyendo el manual de RSync encontramos dos modos distintos de copiar un
directorio hacia un destino, siendo la diferencia el uso de un *trailing
slash* (el símbolo /):

``` terminal
rsync -av /origen/foo /destino
rsync -av /origen/foo/ /destino/foo
```

En el primer caso se copia el directorio foo dentro del directorio
destino dest. En cambio con el trailing slash indicamos que lo que se
copia es el contenido del directorio foo, y entonces para mantener la
estructura en el destino, debemos copiarlo dentro de un directorio foo
(no directamente en dest).

Para copiar todas mis fotos, lo que tengo que hacer es crear (por única
vez) un directorio para tal efecto en el disco externo:

``` terminal
$ mkdir /media/diego/biblioteca/mantener-backup/fotos-diego
```

Para efectuar la copia de las fotos que tengo ubicadas dentro de
/home/diego/fotos, el comando será:

``` terminal
$ rsync -avh --progress --delete ~/fotos/ /media/diego/biblioteca/mantener-backup/fotos-diego
```

Otro ejemplo es la copia que hago de mi colección de libros organizados
con Calibre:

``` terminal
$ rsync -avh --progress --delete ~/calibre/ /media/diego/biblioteca/espejo-del-rigido/calibre
```

De un rígido externo a otro (porque hay que hacer backup del backup de
vez en cuando):

``` terminal
$ rsync -avh --progress --delete /media/diego/biblioteca/mantener-backup/ /media/diego/backup/mantener-backup
$ rsync -avh --progress --delete /media/diego/biblioteca/fotos-videos/ /media/diego/backup/fotos-videos
```

La primera vez que se ejecute rsync, cuando el destino está vacío,
consumirá más tiempo porque debe copiar todos los archivos. Sin embargo,
en ejecuciones posteriores se compararán los directorios de origen y
destino, y sólo se copiará aquello que haya cambiado (o se borrarán
aquellos archivos en el directorio de destino que se hayan eliminado del
directorio de origen). Este modo de hacer backup me cambió la vida.

------------------------------------------------------------------------

A continuación, un ejemplo modificado de
[StackExchange](https://superuser.com/questions/576687/how-to-print-files-that-would-have-been-changed-using-rsync):
sirve para verificar con un \"dry-run\" cuáles serán los cambios que se
realizarán, sin que se materialicen. Para efectuar realmente los cambios
hay que borrar \"\--dry-run\" y ejecutar de nuevo la orden.

El \"delete-after\" realiza el borrado de los archivos en el destino
(aquellos que no están en el origen) recién después de que se haya
completado la copia. El directorio de origen y el del final están
probados para un caso particular en mi instalación de Manjaro
(18/11/2020), así que cada uno tendrá que modificarlo de acuerdo a sus
ubicaciones.

``` terminal
$ rsync -avhi --dry-run --progress --delete-after ~/Calibre/
/run/media/diego/biblioteca/espejo-del-rigido/calibre/general/ | egrep -v
"sending incremental file list" | egrep -v "^\
```
