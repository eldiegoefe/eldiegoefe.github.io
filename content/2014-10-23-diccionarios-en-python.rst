:title: Diccionarios en Python
:date: 2014-10-23 10:00
:category: tecnicismos
:tags: python, diccionarios
:author: El Diego Efe
:excerpt: Diccionarios en Python
:status: draft
:disqus_identifier: diccionarios en python

VERIFICAR TODO ESTO; LO FUI CAMBIANDO SIN PROBARLO, Y DE MEMORIA.
El operador **in** funciona con las listas. Las "keys" (los índices no
numéricos del diccionario) son listas en Python 2.7 y son de un tipo
especial en Python 3.3, por lo que en este último caso hay que
convertir las keys en una lista, antes de aplicar el operador
mencionado. Para ver si un elemento está entre los valores del
diccionario antes hay que usar *values*:

.. code-block:: python

   eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
   vals = eng2sp.values()
   'one' in eng2sp
   True
   'uno' in eng2sp
   False
   'uno' in vals
   True
