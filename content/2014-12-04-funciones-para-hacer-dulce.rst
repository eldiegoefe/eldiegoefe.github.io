:title: Funciones para hacer dulce
:date: 2014-12-04 12:00
:category: tecnicismos
:tags: clojure, lisp, programacion
:author: El Diego Efe
:excerpt: Funciones para hacer dulce
:status: draft
:disqus_identifier: funciones para hacer dulce

El ejemplo del capítulo `Functional Programming`_ (del libro `Clojure
for the Brave and True`_ me hizo analizar con detenimiento muchas
funciones para poder entender un poco su funcionamiento. Esta es una
serie de anotaciones para recordar mi temblorosa exploración.

1. Lista de funciones usadas:

- apply
- assoc-in
- clojure.string/join
- clojure.string/lower-case
- comp
- cons
- count
- count
- dec
- filter
- first
- get
- get-in
- get-input
- if-let
- if-not
- inc
- input
- int
- last
- lazy-seq
- map
- max-pos
- not-empty
- nth
- or
- partial
- println
- range
- re-seq
- reduce
- some
- str
- take
- take-while

2. `assoc-in`_: arma o agrega valores a un mapa anidado. Puede usarse
   de distintas maneras para modificar o agregar elementos de un mapa
   o vector con mapas.

.. code-block:: clj

   (assoc-in map [llaves] valor)

   ; parte de un mapa vacío: {}
   (assoc-in {} [:a :b :c] 1)
   {:a {:b {:c 1}}}

   ; definimos un vector con 2 maps
   (def usuarios [{:nombre "Ricardo" :telefono 326-3322}  {:nombre "Juana" :telefono 327-4343}])
   [{:telefono 3263322, :nombre Ricardo} {:telefono 3274343, :nombre Juana}]

   ; agrega un dato al elemento 0 del vector. recordar que usuarios es
   ; inmutable, asi que si despues pretendemos usarlo, seguira teniendo
   ; los valores originales, sin este agregado.
   (assoc-in usuarios [0 :email] "ricardo@mail.com")
   [{:email "ricardo@mail.com", :telefono 3263322, :nombre "Ricardo"}
   {:telefono 3274343, :nombre "Juana"}]

3. Para ver el contenido de una variable en el repl se puede poner
   directamente el nombre de esta variable, sin los paréntesis.

.. _assoc-in: http://clojuredocs.org/clojure.core/assoc-in
.. _Clojure for the Brave and True: http://www.braveclojure.com/
.. _Functional Programming: http://www.braveclojure.com/functional-programming/#4__Peg_Thing_
