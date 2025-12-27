---
title: Lineas en Emacs - Visual line mode - Auto fill mode
date: 2023-10-30T10:00:00
categories: [tecnicismos]
tags: [emacs]
author: Diego Efe
featuredImagePreview: https://live.staticflickr.com/65535/53337827938_3ab3a4e359_b.jpg
toc: false
---

En Emacs las lineas de texto pueden ser:

- *visibles*: las que terminan en cada linea o renglón
- *lógicas*: las que terminan con un Enter. Una linea lógica puede ocupar muchas lineas visibles, y esto hace que algunos comandos de Emacs funcionen de manera distinta en ambos tipos de linea.

Por defecto las lineas son *lógicas* y al escribir uno puede llegar al final de la linea y continuar escribiendo. Aparecen caracteres "raros" sobre los bordes (para indicar que la linea se continúa). Hay un ajuste de linea o "line-wrap", de manera que el renglón inicial y el renglón que continúa constituyen una sola linea de texto (una línea *lógica*).

La última palabra puede quedar dividida, con los primeros caracteres
sobre el final de la linea, y los últimos caracteres al principio de
la linea de abajo. Al cambiar el tamaño del buffer donde se muestra la
linea, el lugar donde se produce el line-wrap cambia, pero la linea
sigue teniendo siempre la misma extensión original.

Comparado con el modo de linea *visible* hay comandos que funcionan
distinto: 

+ en lineas *visibles*: C-a (move-beginning-of-line: ir al inicio de
  la linea), C-e (move-end-of-line: ir al final de la linea) funcionan
  en las lineas tal como las vemos (no tiene en cuenta las líneas
  *lógicas*).
- en lineas *lógicas*: C-a y C-e van al inicio y final absoluto de la
  linea, con lo cual no permite ir al inicio y final de las lineas
  *visibles*. Se complica navegar el texto.
  
auto-fill-mode
------------------

En este modo, al llegar a una posición prefijada en el renglón, se produce un fin de linea automáticamente (sin tener que apretar Enter). Así, cada linea lógica corresponde a una linea visible.

Se activa/desactiva con auto-fill-mode. Es un modo menor, que al
activarse se indica con *Fill* en la "mode-line" (la linea de estado). Puede activarse globalmente desde el init.el:

```cl
(setq-default auto-fill-function 'do-auto-fill)
```

La desventaja es que si por algún motivo se achica el tamaño del
buffer y la linea ya no entra en un renglón visible, se producirá un
"line-wrap", debiéndose realizar un auto-fill manual para corregir la
situación. También es problemático si se necesita copiar un texto a
otro editor, cada linea será considerada un párrafo.

En este modo son útiles los comandos:

- fill-paragraph (M-q): ajusta el bloque de texto seleccionado al
  ancho correcto (inserta los fines de linea donde corresponde para
  que el texto se vea bien).
- unfill-region (C-M-q): combina todas las lineas visibles
  seleccionadas en un solo párrafo. 

Este último hay que definirlo en el archivo de configuración *init.el*
de Emacs:

```cl
;; unfill-paragraph es una función para deshacer fill-paragraph
;; https://www.emacswiki.org/emacs/UnfillParagraph
;;; Stefan Monnier <foo at acm.org>. It is the opposite of fill-paragraph
(defun unfill-paragraph (&optional region)
  "Takes a multi-line paragraph and makes it into a single line of text."
  (interactive (progn (barf-if-buffer-read-only) '(t)))
  (let ((fill-column (point-max))
        ;; This would override `fill-column' if it's an integer.
        (emacs-lisp-docstring-fill-column t))
    (fill-paragraph nil region)))

;; unfill-region está inspirada en unfill-paragraph
(defun unfill-region (beg end)
  "Unfill the region, joining text paragraphs into a single
    logical line.  This is useful, e.g., for use with
    `visual-line-mode'."
  (interactive "*r")
  (let ((fill-column (point-max)))
    (fill-region beg end)))

;; Handy key definition
(define-key global-map "\C-\M-Q" 'unfill-region)
```

visual-line-mode
--------------------

Es un modo que permite que los comandos como C-a y C-e actúen sobre las lineas visibles en vez de las lineas lógicas. Al activarse se eliminan los caracteres "raros" que señalan la continuidad de la linea *lógica*.

Se activa/desactiva con visual-line-mode en cada buffer, o globalmente en todos los buffers con global-visual-line-mode. Es un modo menor, que al activarse se indica con *Wrap* en la "mode-line" (la linea de estado). Se puede agregar al *init.el* para que se active globalmente:

```cl
(global-visual-line-mode)
```

Este modo evita el inconveniente de que las palabras queden truncadas, con la parte inicial sobre el final del renglón y el resto sobre la parte inicial del renglón siguiente. El ajuste de linea se realiza respetando las palabras completas.

Puede instalarse (y activarse) el paquete *[visual-fill-column](https://github.com/joostkremers/visual-fill-column)* para fijar un ancho de linea distinto al ancho del buffer (más parecido a auto-fill-mode). En *init.el* habrá que agregar:

```cl
(add-hook 'visual-line-mode-hook #'visual-fill-column-mode)
```

Puede intalarse (y activarse) el paquete *[adaptive-wrap](https://elpa.gnu.org/packages/adaptive-wrap.html)* para mejorar la presentación visual de las listas (para que las lineas queden alineadas con la sangría de su primer renglón). 

Tampoco muestra ningún caracter raro en los bordes para indicar que la linea continua en la siguiente linea *visible*. Esto se puede cambiar con la variable visual-line-mode-fringe-indicators.

Una alternativa de visualización que puede ser útil a veces es truncar las lineas (y que no se vea lo que excede al ancho del buffer). Esto se logra con M-x toggle-truncate-lines.

![Modos en acción](https://live.staticflickr.com/65535/53337827938_77f4ba4ffe_k.jpg ) 

