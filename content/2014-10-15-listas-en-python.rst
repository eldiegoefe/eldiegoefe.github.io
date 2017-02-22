:title: Listas en Python
:date: 2014-10-15 10:00
:category: tecnicismos
:tags: python, listas
:author: El Diego Efe
:excerpt: Listas en Python
:disqus_identifier: listas en python

Apuntes del capítulo 10. Lists, de Think Python.

Traversing
==========

*To traverse* es el verbo que se refiere al acceso secuencial de los
elementos de una lista. La siguiente es una forma de "traversear" una
lista:

.. code-block:: python

   for cheese in cheeses:
          print cheese

Si se necesita modificar algún elemento de la lista es mejor hacer:

.. code-block:: python

   for i in range(len(numbers)):
          numbers[i] = numers[i] * 2

Agregar elementos a una lista
=============================

Se pueden agregar elementos individuales a una lista con *append*.

También se pueden agregar elementos con el operador *+*.

Ambas formas tienen diferencias:

.. code-block:: python

   t1 = [1, 3, 4]
   t2 = t1.append(10)
   print t1
   [1, 3, 4, 10]
   print t2
   None

El método *append* modifica la lista sobre la cual se aplica pero
tiene salida None.

El operador *+* sí tiene una salida:

.. code-block:: python

   t1 = [1, 3, 4]
   t2 = t1 + [10]
   print t1
   [1, 3, 4]
   print t2
   [1, 3, 4, 10]

Se puede agregar una lista (t2) a otra lista (t1) con *extend*:

.. code-block:: python

    t1 = [1, 3 , 4]
    t2 = [2, 2]
    t1.extend(t2)
    print t1
    [1, 3, 4, 2, 2]

Salidas de los métodos de lista
===============================

Las salidas de los métodos aplicados a listas son todos *void*, es
decir que no dan ningún valor de salida. Por ejemplo el método
**sort** ordena una lista, modifica esa lista (la muta) pero la salida
es None (aunque la lista efectivamente cambió).

Reduce Fat Fast or Map, Filter and Reduce
=========================================

**Reduce**: una operación que combina una secuencia de elementos en un
solo valor (por ejemplo: la suma de todos los elementos). Es un patrón
de procesamiento que *traversea* una secuencia y acumula los elementos
en un solo resultado.

**Map**: una operación que aplica una función a cada elemento de una lista
(por ejemplo: poner en mayúscula la inicial de las palabras que forman
una lista). El mapeo es una relación en la cual cada elemento de una
lista corresponde a un elemento en otra lista. Por ejemplo: una lista
es un mapeo de índices a elementos.

**Filter**: una operación que selecciona algunos elementos de una lista,
basándose en algún criterio (por ejemplo: las palabras de una lista cuyas
letras estén todas en mayúsculas). Es un patrón de procesamiento que
*traversea* una lista y selecciona los elementos que satisfacen algún
criterio especificado.

Las operaciones más comunes sobre una lista pueden ser expresadas como
una combinación de map, filter y reduce.

Borrar elementos de una lista
=============================

Hay distintos modos:

- **pop**: modifica la lista

.. code-block:: python

   t = [2, 4, 8]
   x = t.pop(1)
   print t
   [2, 8]
   print x
   4

- **del**: cuando no se necesita el elemento borrado

.. code-block:: python

   t = [2, 4, 8, 16]
   del t[1]
   print t
   [2, 8, 16]

Obs: pueden usarse slices. del t[1:3] ---> [2, 16]

- **remove**: cuando no se conoce el índice, pero sí el elemento a borrar

.. code-block:: python

   t = [2, 4, 8]
   t.remove(8)
   print t
   [2, 4]
