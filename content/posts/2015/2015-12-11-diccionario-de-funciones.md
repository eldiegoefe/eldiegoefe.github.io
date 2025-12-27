---
title: Diccionario de funciones
date: 2015-12-11T10:00:00
categories: [tecnicismos]
tags: [python, diccionarios, funciones]
author: Diego Efe
toc: false
---

Mientras escribo un programa para manipular imágenes de un microscopio, tuve que
ver cómo ejecutar una función distinta, de acuerdo a cierto parámetro. Más
concretamente, para procesar las imágenes en algunos casos se necesita un
kernel, que es una matriz llena de unos y ceros organizados de acuerdo a la
selección de dos parámetros: forma y tamaño. Por ejemplo, un \"disco\" de radio
3 se vería así:

    [[0 0 0 1 0 0 0]
     [0 1 1 1 1 1 0]
     [0 1 1 1 1 1 0]
     [1 1 1 1 1 1 1]
     [0 1 1 1 1 1 0]
     [0 1 1 1 1 1 0]
     [0 0 0 1 0 0 0]]

Y una matriz \"cuadrada\" de lado 3, así:

    [[1 1 1]
     [1 1 1]
     [1 1 1]]

Una forma de escribirlo sería usando un \"if\" para cada posibilidad,
pero si las variantes son muchas entonces queda poco elegante. Por
suerte encontré una alternativa, que se parece al \"case\" de otros
lenguajes, pero con mucho más *punch*:

``` python
tiposPosibles = {"cuadrado": square, "disco": disk}

def armarKernel(tipo="cuadrado", tam=3):
    kernel = tiposPosibles[tipo](tam)
```

En el ejemplo, tiposPosibles es un diccionario. Cuando tipo =
\"cuadrado\", y tam = 4, la linea equivale a: kernel = square(4).
¡Maravilloso!
