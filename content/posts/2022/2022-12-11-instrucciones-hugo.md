---
title: Instrucciones Hugo
date: 2022-12-11T10:00:00
categories: [tecnicismos]
tags: [blog]
author: Diego Efe
disqus_identifier: Instrucciones Hugo
featuredImagePreview: https://raw.githubusercontent.com/khusika/FeelIt/main/images/screenshot.png
toc: false
---

Estas son instrucciones para no olvidarme cómo actualizar este mismo
blog. Escribo las entradas y uso **Hugo** para correr un servidor local e
ir corrigiendo / agregando cosas. 

```terminal
$ hugo server
```

Una vez que tengo la versión final, hago una copia de todo el blog en
el repositorio "Certezas Dudosas" en mi cuenta de Bitbucket. Esto me
sirve de backup, para no perder nada.

Luego, para generar los archivos del blog hay que correr Hugo sin
modificadores: 

```terminal
$ hugo
```

El contenido generado se aloja en el directorio /public
(*/home/diegol/blog/certezas-dudosas/public*). 

En otro directorio tengo una copia del contenido de mi página en
Github (*/home/diegol/blog/eldiegoefe.github.io*). Sobre este directorio
copio y pego lo que había en /public. Capaz que quedan archivos basura
acumulándose, pero por ahora no necesito hacer limpieza.

Finalmente tengo que actualizar el repositorio de Github y subirlo:

```terminal
$ git status
$ git add . 
$ git commit -m "agregada tal cosa..."
$ git push --all
```

¡Listo! Ya tengo subido el blog.

--- 

El tema que uso para darle formato al blog se llama **FeelIt**. Lo tengo
que clonar en un directorio dentro de certezas-dudosas
(*blog/certezas-dudosas/themes/FeelIt*), de esta manera:

```terminal
$ git clone https://github.com/khusika/FeelIt.git themes/FeelIt
```
