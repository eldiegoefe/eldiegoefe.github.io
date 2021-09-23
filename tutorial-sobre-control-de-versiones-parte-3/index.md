# Tutorial sobre control de versiones (parte 3)


## Indice del Tutorial

- [Parte 1]({{< ref "2014-10-06-control-de-versiones-1.md" >}}). Cómo armar un repositorio local
- [Parte 2]({{< ref "2014-10-07-control-de-versiones-2.md" >}}). Cómo subir el repositorio local al remoto
- [Parte 3]({{< ref "2014-10-09-control-de-versiones-3.md" >}}). Cómo colaborar en un mismo repositorio remoto
- [Parte 4]({{< ref "2014-10-10-control-de-versiones-4.md" >}}). Cómo resolver conflictos

Para ver las versiones (en inglés) en las cuales se basa este tutorial,
podés visitar [la página de Software
Carpentry](http://software-carpentry.org/v5/novice/git/)

## Probando el cooperativismo

Vamos a practicar cómo se realiza una colaboración a través de un
repositorio en Github. Para ello nada mejor que colaborar con uno mismo.
Lo que hago es trabajar con dos cuentas en Github, corriendo un usuario
en mi PC de escritorio y el otro dentro de una máquina virtual dentro de
la misma PC (aunque también lo podría hacer desde una notebook, o desde
otra sesión de esta misma computadora, pero decir que uno corre una
máquina virtual con Linux suena mucho más *god-level*). No voy a
detenerme a explicar nada sobre las máquinas virtuales porque además de
ser demasiado sencillo también es off-topic, y no quiero offtopiquearme.
¡Cómprense un amiguito y chau!

Vamos a seguir haciendo las pruebas usando el repositorio **emacs** con
el que estaba nerdeando/tinkereando/boludeando (ahhhh, la flexibilidad
del lenguaje) en la parte 2. Voy a darle permiso de acceso
([no-carnal](#no-carnal)) a un tercero (*bioingenieroDiegol*, mi otra
cuenta). Con este propósito me dirijo a la página del repositorio en
Github, y selecciono Settings/Collaborators. Una vez allí agrego a
*bioingenieroDiegol*.

## Clonación

Luego me cambio a la PC virtual y allí ya vestido como
*bioingenieroDiegol* voy a clonar el repositorio en esa virtuosa
computadora:

``` console
[bioingenierodiegol]$ git clone https://github.com/eldiegoefe/emacs.git
[bioingenierodiegol]$ cd emacs
[bioingenierodiegol]$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working directory clean
```

Ahora tengo los mismos archivos en la compu de *bioingenieroDiegol* que
en el repositorio de Github. Además sucede algo muy curioso, **sin**
haber hecho *git remote add origin
https://github.com/eldiegoefe/emacs.git* vamos a tener:

``` console
[bioingenierodiegol]$ git remote -v
origin  https://github.com/eldiegoefe/emacs.git (fetch)
origin  https://github.com/eldiegoefe/emacs.git (push)
```

Vemos que la url y el alias estaban en el repositorio. Es por convención
que se usa el nombre de *origin* como alias. Cuando más adelante quiera
hacer el *git push* voy a usar directamente *git push origin master* y
va a funcionar.

## Cambios hechos por el colaborador

A continuación hago algunos cambios en los archivos locales de
*bioingenieroDiegol* (para esta prueba puedo agregar un archivo nuevo o
modificar los existentes) y luego voy a tratar de subirlos al repo
remoto (que sigue siendo propiedad de *eldiegoefe*). Para esta última
tarea es que hube agregado (¡caramba!) a *bioingenieroDiegol* a la lista
de colaboradores (porque para la clonación no necesitaba permisos).

``` console
[bioingenierodiegol]$ touch archivo-vacio.txt
[bioingenierodiegol]$ git add archivo-vacio.txt
[bioingenierodiegol]$ git commit -m "Agrego archivo-vacio.txt"
[bioingenierodiegol]$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
nothing to commit, working directory clean
```

Git es muy comunicativo y nos dice lo que sucede y cómo tenemos que
continuar. Nuestra rama *master* local está adelantada respecto de la
rama *master* que se encuentra en origin (origin/master) por 1 commit
(el que acabamos de realizar).

## El colaborador sube sus cambios a Github

Tenemos que hacer un push para llevar los cambios locales de
*bioingenieroDiegol* al remoto. No hay nada que comitear (ni nada que
festejar, aún). Vamos a hacerle caso a Git, vean lo que sucede tras un
*git push origin master* hecho por *bioingenieroDiegol* (no se confundan
con el prompt de esa consola, que es *manjaro-efe%*):

{{< figure src="https://farm9.staticflickr.com/8671/15668755234_04cf679b86_o.png" title="Consola mostrando git push desde bioingenieroDiegol" >}}

Ningún error, todo bien (vean que tuve que responder con el username y
password del colaborador *bioingenieroDiegol*, bah, el password no se
ve\...).

## El dueño original del repositorio actualiza su repo local

Finalmente el dueño original del repositorio (yo, *eldiegoefe*) quiere
actualizar su repositorio local con los cambios hechos por todos los
contribuyentes (en este caso sólo *bioingenieroDiegol*). Para ello hace
un pull desde el remoto:

``` console
[eldiegoefe]$ git pull origin master
remote: Counting objects: 2, done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 2 (delta 1), reused 2 (delta 1)
Unpacking objects: 100% (2/2), done.
From https://github.com/eldiegoefe/emacs
 * branch            master     -> FETCH_HEAD
   2c817b6..f94cdfa  master     -> origin/master
Updating 2c817b6..f94cdfa
Fast-forward
 archivo-vacio.txt | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 archivo-vacio.txt
```

El sistema le indica que se actualizó, que un archivo cambió
(*insertions* y *deletions* son cambios en el interior de los archivos,
como no hubo ningun cambio entonces quedan en cero). El método por el
cual se hizo la fusión (merge) entre el remoto y el local fue
*Fast-forward* y no hubo ningún conflicto. ¡Fiesta!

## Claves

> Un repositorio local Git puede estar conectado a uno o más
> repositorios remotos.
>
> Se puede usar el protocolo HTTPS para conectarse al repositorio remoto
> (hasta que uno aprenda a lidiar con el protocolo SSH, que es más
> seguro).
>
> Con **git push** se copian los cambios del repositorio local hacia el
> remoto
>
> Con **git pull** se copian los cambios desde el repositorio remoto
> hacia el repositorio local.
>
> Con **git clone** se copia un repositorio remoto para crear un
> repositorio local con un *remote* automáticamente llamado *origin*.

::: {#no-carnal}
¡basta de hacer chistes malos!
:::

