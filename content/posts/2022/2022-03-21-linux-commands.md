---
title: Comandos Linux
date: 2022-03-26T10:00:00
categories: [tecnicismos]
tags: [linux]
author: Diego Efe
disqus_identifier: Comandos Linux
featuredImagePreview:
draft: true
toc: false
---

# Comandos habituales en la linea de comandos de Linux

Los comandos que se listan son de BASH.

Aclaración: los puntos suspensivos indican que se pueden escribir varios nombres
de archivos o directorios.

- *pwd*. Print Working Directory. Muestra el directorio actual. 
- *ls -l directorios...*. Listar directorios. Incluir información completa.
- *ls -a directorios...*. Listar directorios. Incluir ocultos.
- *man comando*. Información de un comando: muestra su manual de uso.
- *cd*. Cambiar directorio.
- *cp arch1 arch2*. Copia el arch1 en el mismo directorio con el nombre arch2.
- *cp arch1 arch2 arch3 ... directorio*. Copiar varios archivos en el directorio
  destino.
- *mkdir directorios...*. Crear uno o más directorios.
- *mv arch1 arch2*. Renombra el arch1 en arch2.
- *mv arch1 arch2 arch3 ... directorio*. Mover archivos al directorio.
- *rm arch1 arch2 arch3 ...*. Remover archivos. 
- *ln archivo link*. Crea un hard link hacia archivo.
- *ln -s archivo link*. Crea un soft link hacia archivo. Es preferible a los
  hard-links. Conviene que la ruta definida sea relativa a la posición del
  symlink en vez de colocar el path completo, para que siga vigente aún cuando
  se muevan los archivos a otro directorio.
  
 Ayudas:
 
 - *type item* indica el tipo de archivo y brinda información sobre él.
 - *which cmnd* muestra el archivo ejecutable con su path.
 - *help cmnd* ofrece ayuda sobre un comando.
 - *man program* muestra el exhaustivo manual de un programa, mediante **less**.
 - *apropos palabra-clave* lista todos los comandos asociados a la palabra clave.
 - *info cmnd* muestra un manual alternativo del comando (propio de GNU) con un
   programa llamado **info**, usa hiperenlaces con el contenido organizado en
   distintos nodos.
 - *whatis cmnd* describe el comando en una linea.
 - *alias*.

| tabla | otro |
|:-----:|:----:|
| hola  | chau |
|       |      |

Zathura (VIM Based PDF Reader)

+: zoom +
-: zoom -
=: zoom 100%

Al estar haciendo zoom, se puede mover a derecha e izquierda con *h* y *l*
