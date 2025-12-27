---
title: Tutorial sobre control de versiones (parte 4)
date: 2014-10-10T11:00:00
categories: [tecnicismos]
tags: [git, control de versiones, tutorial]
author: Diego Efe
series: ["control-de-versiones"]
featuredImagePreview: https://live.staticflickr.com/65535/51500798922_23d474dc72.jpg
---

Para ver las versiones (en inglés) en las cuales se basa este tutorial, podés
visitar [la página de Software
Carpentry](http://software-carpentry.org/v5/novice/git/)

## Cuándo aparecen los conflictos

El sistema de control de versiones permite que la gente trabaje en paralelo
editando sus programas en código fuente. En realidad, se puede usar para
cualquier tipo de archivo con texto plano (me parece fantástico para informes,
relatos, blogs como este, etc).

Trabajar en paralelo implica que en algún momento dos personas se van a pisar y
van a modificar una misma porción de texto. Esto podría pasarle incluso a una
sola persona: si trabajamos un mismo fragmento en la computadora de escritorio
en casa, en una notebook y también en una PC en el laburo, podríamos haber hecho
diferentes cambios en cada copia. El control de versiones nos ayuda a manipular
esos conflictos dándonos herramientas para resolver esos cambios superpuestos.

## Un conflicto impostado

Para ver cómo se resuelven estos conflictos vamos a subir al repositorio *emacs*
que posee *eldiegoefe* el archivo *manifiesto.txt* con el siguiente texto:

    Un fantasma recorre Europa: el fantasma del comunismo. Todas las
    fuerzas de la vieja Europa se han unido en santa cruzada para acosar a
    ese fantasma: el Papa y el zar, Metternich y Guizot, los radicales
    franceses y los polizontes alemanes.

A continuación vamos a hacer que los dos usuarios con los que trabajamos en la
[parte 3]({{< ref "/posts/2014/2014-10-09-control-de-versiones-3.md" >}})
(*eldiegoefe* y *bioingenierodiegol*) realicen cambios de este archivo en sus
repositorios locales.

El usuario *bioingenierodiegol* agrega una linea a su versión local de
*manifiesto.txt*:

    Un fantasma recorre Europa: el fantasma del comunismo. Todas las
    fuerzas de la vieja Europa se han unido en santa cruzada para acosar a
    ese fantasma: el Papa y el zar, Metternich y Guizot, los radicales
    franceses y los polizontes alemanes. Marx se la come.

Mientras tanto el usuario *eldiegoefe* agrega otra oración, un poco
menos revisionista:

    Un fantasma recorre Europa: el fantasma del comunismo. Todas las
    fuerzas de la vieja Europa se han unido en santa cruzada para acosar a
    ese fantasma: el Papa y el zar, Metternich y Guizot, los radicales
    franceses y los polizontes alemanes. Marx es re-grosso, vieja.

Por cosas de la vida, *bioingenierodiegol* hace su secuencia **1. git
add manifiesto.txt**, **2. git commit -m \"Agregue linea \'Marx se la
come\'\"** y **3. git push origin master** de modo que cuando termina de
hacerlo, en el repositorio remoto (en Github) el archivo
*manifiesto.txt* habla de la gastronómica vida sexual de Marx.

## Experimentando la frustración del militante

El respetuoso militante *eldiegoefe* también modifica su copia local de
*manifiesto.txt*, hace su *git add* y su *git commit* pero veamos qué
sucede cuando intenta el *git push*:

``` console
[eldiegoefe]$ git push origin master
To https://github.com/eldiegoefe/emacs.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/eldiegoefe/emacs.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

El sistema nos da un error, pero también nos dice el motivo por el cual
fue rechazado el *push*: el remoto contiene trabajo que no poseemos
localmente. Esto es frecuentemente causado por otro usuario actualizando
el repositorio en Github en el tiempo que transcurre entre el momento
que hicimos la última sincronización con el repositorio remoto y el
tiempo en el que intentamos el *git push*. En su mensaje, como el
sistema sabe de esta posibilidad, sugiere primero integrar los cambios
del remoto con un *git pull* antes de volver a intentar nuestro *git
push*.

## Comenzando a solucionar la cuestión

Es decir que Git detecta que los cambios hechos en una copia se
superponen con los hechos en la otra copia, y nos impide pisar o
sobreescribir el trabajo. Vamos entonces a hacer el *git pull* desde
Github y fundir esos cambios remotos en nuestra copia local.

``` console
[eldiegoefe]$ git pull origin master
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 2), reused 3 (delta 2)
Unpacking objects: 100% (3/3), done.
From https://github.com/eldiegoefe/emacs
 * branch            master     -> FETCH_HEAD
   142c683..efe8a9a  master     -> origin/master
Auto-merging manifiesto.txt
CONFLICT (content): Merge conflict in manifiesto.txt
Automatic merge failed; fix conflicts and then commit the result.
```

Ahora Git nos avisa que hay un conflicto y marca el archivo donde éste
se produce (*manifiesto.txt*). Veamos ahora el contenido de este archivo
con cualquier editor:

    Un fantasma recorre Europa: el fantasma del comunismo. Todas las
    <<<<<<< HEAD
    fuerzas de la vieja Europa se han unido en santa cruzada para acosar a
    ese fantasma: el Papa y el zar, Metternich y Guizot, los radicales
    franceses y los polizontes alemanes. Marx es re-grosso, vieja.
    =======
    fuerzas de la vieja Europa se han unido en santa cruzada para
    acosar a ese fantasma: el Papa y el zar, Metternich y Guizot, los
    radicales franceses y los polizontes alemanes. Marx se la come.
    >>>>>>> efe8a9a434f1a2609a16660f7d78c82fadad7d7c

Vemos que Git ha modificado el archivo local colocando marcas para
separar las dos versiones. Veo que ambas versiones no solamente difieren
en la oración que habla de Marx, sino también en el contenido de las
últimas tres lineas (no empiezan y terminan con las mismas palabras).
¡No es facil engañar a Git!

Las marcas son **\<\<\<\<\<\<\< HEAD**, el separador **=======** (que
divide los cambios conflictivos en las dos versiones) y **\>\>\>\>\>\>\>
efe8a9a434f1a2609a16660f7d78c82fadad7d7c**. Lo que está junto al
**HEAD** es el contenido local, mientras lo que está tras el separador
(antes del identificador de la revisión que acabamos de bajar) es el
contenido agregado remotamente.

## Solución en proceso

Nos corresponde editar este archivo para remover las marcas y
reconciliar los cambios. Podemos hacer lo que nos plazca: mantener los
cambios que hicimos en el repositorio local, mantener los cambios hechos
en el repositorio remoto, escribir algo nuevo que reemplace a ambos, o
eliminar completamente ambos cambios. Hagamos una mezcla:

    Un fantasma recorre Europa: el fantasma del comunismo. Todas las
    fuerzas de la vieja Europa se han unido en santa cruzada para
    acosar a ese fantasma: el Papa y el zar, Metternich y Guizot, los
    radicales franceses y los polizontes alemanes. Marx es re-grosso,
    pero Engels es más grosso todavía.

Ahora *eldiegoefe* pide enterarse de cómo está la situación:

``` console
[eldiegoefe]$ git status
# On branch master
# You have unmerged paths.
#   (fix conflicts and run "git commit")
#
# Unmerged paths:
#   (use "git add <file>..." to mark resolution)
#
#       both modified:      manifiesto.txt
#
no changes added to commit (use "git add" and/or "git commit -a")
```

Tenemos que agregar los cambios y comitearlos antes de volver a intentar
el push:

``` console
[eldiegoefe]$ git add manifiesto.txt

[eldiegoefe]$ git status
# On branch master
# All conflicts fixed but you are still merging.
#   (use "git commit" to conclude merge)
#
# Changes to be committed:
#
#       modified:   manifiesto.txt

[eldiegoefe]$ git commit -m "Conflicto arreglado en manifiesto.txt"
[master 4f17908] Conflicto arreglado en manifiesto.txt

[eldiegoefe]$ git status
# On branch master
nothing to commit, working directory clean
```

## Listo el pollo

Ahora sí intentamos el push:

``` console
[eldiegoefe]$ git push origin master
Counting objects: 10, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 665 bytes | 0 bytes/s, done.
Total 6 (delta 4), reused 0 (delta 0)
To https://github.com/eldiegoefe/emacs.git
   efe8a9a..4f17908  master -> master
```

Esta vez pudimos subir todo exitosamente. Ahora vamos a ver qué le pasa
al otro usuario *bioingenierodiegol* cuando quiere actualizar su repo
local:

``` console
[bioingenierodiegol] $ git pull origin master
remote: Counting objects: 6, done.
remote: Compressing objects: 100% (2/2), done.
Unpacking objects: 100% (6/6), done.
remote: Total 6 (delta 4), reused 6 (delta 4)
From https://github.com/eldiegoefe/emacs
 * branch            master     -> FETCH_HEAD
   efe8a9a..4f17908  master     -> origin/master
Updating efe8a9a..4f17908
Fast-forward
 manifiesto.txt | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
```

Sin problemas se ha cerrado el círculo, ambos usuarios tienen el mismo
contenido en el archivo que había generado el conflicto:

    Un fantasma recorre Europa: el fantasma del comunismo. Todas las
    fuerzas de la vieja Europa se han unido en santa cruzada para
    acosar a ese fantasma: el Papa y el zar, Metternich y Guizot, los
    radicales franceses y los polizontes alemanes. Marx es re-grosso,
    pero Engels es más grosso todavía.

El usuario *bioingenierodiegol* no tuvo necesidad de hacer la fusión
(merge) porque Git sabe que algún otro ya lo hizo.

Los usuarios tienden a dividir sus programas y textos en múltiples
archivos (en vez de meter todo en un mismo archivo enorme) porque esto
facilita lo que acabamos de ver: habilidad del sistema de control de
versiones para fusionar cambios conflictivos.

Hay también otro beneficio: siempre que hay conflictos repetidos en un
archivo en particular, el sistema de control de versiones está
esencialmente tratando de decirle a sus usuarios que deberían clarificar
quién es el responsable de cada cosa, o encontrar un modo de dividir el
trabajo de modo diferente.

## Claves

> Los conflictos ocurren cuando dos o más personas cambian el mismo
> archivo al mismo tiempo.
>
> El sistema de control de versiones no permite que la gente
> sobreescriba ciegamente los cambios realizados por otras personas. En
> cambio, resalta los conflictos para que los puedan resolver.
