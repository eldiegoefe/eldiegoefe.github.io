---
title: Movimientos Originales en Emacs
date: 2022-03-27T10:00:00
categories: [tecnicismos]
tags: [emacs]
author: Diego Efe
disqus_identifier: Movimientos Originales en Emacs
featuredImagePreview: https://live.staticflickr.com/65535/51965503911_211bea59a8_o.png
toc: false
---

Estoy volviendo a probar Emacs con los atajos de teclado originales, tras años de usar evil-mode y la edición modal propia de VIM (que está buenísima). Lo hago para independizarme de los *kits* como *Doom Emacs* y *Spacemacs* y así retomar el control total sobre la configuración y de paso retomar el estudio de LISP. Esto es un resumen de los atajos de teclado que deseo recordar.

# Movimientos sobre la linea

| Tecla | Comando                | Comentario                                                   |
|:-----:|:----------------------:|:------------------------------------------------------------:|
| C-a   | move-beginning-of-line | Mueve al inicio de la linea                                  |
| C-e   | move-end-of-line       | Mueve al final de la linea                                   |
| M-m   | back-to-indentation    | Mueve al primer caracter de la linea luego de la indentación |

# Movimientos de distancias cortas: caracteres y lineas

| Tecla | Comando       | Comentario                       |
|:-----:|:-------------:|:--------------------------------:|
| C-f   | forward-char  | Mueve un caracter hacia adelante |
| C-b   | backward-char | Mueve un caracter hacia atrás    |
| C-n   | next-line     | Mueve hacia la siguiente linea   |
| C-p   | previous-line | Mueve hacia la linea previa      |

# Movimientos entre palabras

| Tecla | Comando       | Comentario                       |
|:-----:|:-------------:|:--------------------------------:|
| M-f   | forward-word  | Mueve una palabra hacia adelante |
| M-b   | backward-word | Mueve una palabra hacia atrás    |

Me parece preferible usar los que aparecen abajo como "Movimiento entre bloques" porque saltan entre palabras igual que estos, y no hace falta estar pensando en si el prefijo es Alt o Ctrl. 

# Movimientos entre oraciones y párrafos

Hay que tener en cuenta que la definición de lo que es una oración o párrafo. En general, las oraciones se considera que terminan en punto y dos espacios. Pero esto puede ser diferente entre diversos modos. No es lo mismo que el buffer sea de markdown que de código Python.

| Tecla | Comando            | Comentario                       |
|:-----:|:------------------:|:--------------------------------:|
| M-}   | forward-paragraph  | Mueve hacia el siguiente párrafo |
| M-{   | backward-paragraph | Mueve hacia el párrafo anterior  |
| M-e   | forward-sentence   | Mueve hacia la siguiente oración |
| M-a   | backward-sentence  | Mueve hacia la oración previa    |

# Movimiento entre bloques (comillas, paréntesis, corchetes, etc)

También conocidos como movimientos entre s-expressions o sencillamente sexp (deberían llamarse expresiones balanceadas, tienen un inicio y un final marcados por estos caracteres especiales: ", ', ( ), [ ], {}, etc. Son especialmente útiles para editar código.

| Tecla | Comando          | Comentario                         |
|:-----:|:----------------:|:----------------------------------:|
| C-M-b | backward-sexp    | Mover hacia la expresión anterior  |
| C-M-f | forward-sexp     | Mover hacia la expresión siguiente |
| C-M-d | down-list        | Mueve dentro de la sexp, al inicio |
| C-M-u | backward-up-list | Mueve dentro de la sexp, al final  |


# Salto al inicio o final del buffer

| Tecla | Comando             | Comentario                  |
|:-----:|:-------------------:|:---------------------------:|
| M-<   | beginning-of-buffer | Saltar al inicio del buffer |
| M->   | end-of-buffer       | Saltar al final del buffer  |

Dejan la marca en la posición desde la cual se origina el salto, por lo cual es fácil volver con C-u C-SPC.
   
# Salto a una posición específica

Para saltar hacia un lugar a media distancia, dentro del buffer visible, lo más eficiente es buscar la palabra hacia la cual queremos ir o hacia alguna palabra aledaña si la deseada aparece demasiadas veces.

| Tecla | Comando                 | Comentario                 |
|:-----:|:-----------------------:|:--------------------------:|
| C-s   | isearch                 | Busca hacia adelante       |
| C-r   | isearch-backward        | Busca hacia atrás          |
| C-M-s | isearch-forward-regexp  | Hacia adelante, con regexp |
| C-M-r | isearch-backward-regexp | Hacia atrás, con regexp    |
| M-s w | isearch-forward-word    | Búqueda "fuzzy"            |


Una vez iniciada la búsqueda, son válidos los siguientes atajos.

| Tecla | Comando                   | Comentario                                        |
|:-----:|:-------------------------:|:-------------------------------------------------:|
| C-w   | isearch-yank-word-or-char | Agrega la palabra bajo el punto                   |
| M-y   | isearch-yank-pop          | Yank del kill-ring                                |
| M-c   | isearch-toggle-case-fold  | Alterna sensibilidad a mayúsculas/minúsculas      |
| M-p   | isearch-ring-retreat      | Hacia atrás en la lista de búsquedas (anteriores) |
| M-n   | isearch-ring-advance      | Hacia adelante en la lista de búsquedas           |

El comando básico es isearch pero puede estar reemplazado por otros como swiper (si está instalado ivy).

# Movimientos mayúsculos: página arriba y abajo

| Tecla   | Comando                  | Comentario                             |
|:-------:|:------------------------:|:--------------------------------------:|
| M-v     | scroll-down-command      | Mueve una página hacia arriba          |
| C-v     | scroll-up-command        | Mueve una página hacia abajo           |
| C-M-v   | scroll-other-window      | Página hacia abajo en la otra ventana  |
| S-C-M-v | scroll-other-window-down | Página hacia arriba en la otra ventana |

La "otra ventana" es el otro buffer que haya abierto, debajo o al lado del buffer activo. 

# Uso de Bookmarks

Se pueden guardar posiciones del cursor y volver luego a ellas. Ampliaré en otra entrada del blog. Por ahora:

| Tecla     | Comando           | Comentario                       |
|:---------:|:-----------------:|:--------------------------------:|
| C-x r SPC | point-to-register | Fija el bookmark                 |
| C-x r j   | jump-to-register  | Salta a la posición del bookmark |

# Posicionamiento del texto en la ventana

| Tecla | Comando                        | Comentario                                                                      |
|:-----:|:------------------------------:|:-------------------------------------------------------------------------------:|
| C-l   | recenter-top-bottom            | Mueve la linea del punto(*) a la parte superior, media o inferior de la ventana |
| M-r   | move-to-window-line-top-bottom | Ubica el punto en la linea superior, media o final de la ventana                |

(*) Punto y cursor son sinónimos.	

Repetición de los comandos: se puede invocar la repetición del comando que se desea ejecutar, utilizando el prefijo C-u.  Por defecto, esto implica repetir cuatro veces el mismo comando. Por ejemplo C-u C-f mueve el cursor cuatro posiciones hacia adelante.  Si se especifica un número entonces se estará fijando el número de repeticiones. Por ejemplo C-u 10 C-n mueve el cursor diez lineas hacia abajo. 

{{< figure src="https://live.staticflickr.com/65535/51964494207_4d53ecefba_o.png" title="M-x Butterfly" >}}

















