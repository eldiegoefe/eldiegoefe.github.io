# Bienvenidos a Scheme


Nuevamente un vórtice del espacio-tiempo perturbó el campo magnético terrestre y
esta vez no solamente escaparon de prisión los más peligrosos rufianes de Ciudad
Gótica, sino que en vez de retomar el estudio de Clojure, el dialecto de Lisp
que me cautivó en 2014, viajé hasta otro universo computacional y ahora estoy a
toda máquina leyendo sobre Scheme, que es otro dialecto del lenguaje diseñado
para simular la inteligencia humana, creado por John McCarthy en la década del
50.

{{< figure src="https://c1.staticflickr.com/5/4541/38650993086_6356f41de4_o.jpg" title="John McCarthy haciéndose el lindo" >}}

Salvo que seas un hongo, o que hayas sido fascinado por la retórica
kirchnerista y/o la capacidad de gestión del macrismo con la
consiguiente pérdida correlativa de capacidades cognitivas, aprender
sobre programación en Lisp te provoca una masiva liberación de
norepinefrina y serotonina, un insoportable deseo de visitar Las Toninas
y de comer pan dulce con muchas pasas de uva como el que venden en la
granjita de al lado de casa.

Scheme es un dialecto muy utilizado en ámbitos educativos. Se que es más
pequeño y sencillo que Common Lisp, y no se qué diferencias tiene con
Clojure y Racket y otros herederos del LISt Processor (de ahí el nombre
del lenguaje McCartista). El tema es que los cursos introductorios de
\"Computer Science\" en las universidades más prestigiosas del mundo
(Berkeley, MIT, La Matanza, Stanford, etc) lo utilizan o lo utilizaban
hasta hace muy poco. De hecho, justamente llegué a Scheme buscando
bibliografía para estudiar programación y Lisp. Me encontré en la web
varios libros y cursos recomendados:

-   el curso CS 61A dictado en Berkeley por Brian Harvey.
-   el libro \"[Structure and Interpretation of Computer
    Programs](https://mitpress.mit.edu/sicp/full-text/book/book.html)\"
    (comunmente llamado SICP) de Harold Abelson, Gerald Jay Sussman y
    Julie Sussman. GJ Sussman fue uno de los dos diseñadores originales
    de Scheme, junto a su discípulo Guy L. Steele Jr (que diseñó y
    documentó también otros lenguajes). Mientras ellos elaboran nuevos
    lenguajes uno apenas puede lidiar con el ordenamiento de las
    estanterías del lavadero.
-   el libro \"Scheme and the Art of Programming\" de George Springer y
    Daniel Friedman
-   el libro \"[Simply
    Scheme](https://people.eecs.berkeley.edu/~bh/ss-toc2.html)\" de
    Brian Harvey y Matthew Wright. Debajo pueden ver la tapa de la
    primera edición.
-   la serie de libros \"The Little Schemer\", \"The Reasoned Schemer\",
    \"The Seasoned Schemer\" de Daniel Friedman, Matthias Felleisen,
    William Byrd y Oleg Kiselyov.

Las clases del
[2008](https://archive.org/details/ucberkeley-webcast-PL6879A8466C44A5D5)
y
[2011](http://www.infocobuild.com/education/audio-video-courses/computer-science/cs61a-spring2011-berkeley.html)
del CS 61A dictadas por [Brian
Harvey](https://people.eecs.berkeley.edu/~bh/) pueden verse online
(hagan click en los años
[2008](https://archive.org/details/ucberkeley-webcast-PL6879A8466C44A5D5)
y
[2011](http://www.infocobuild.com/education/audio-video-courses/computer-science/cs61a-spring2011-berkeley.html)
para llegar). Sus clases son muy claras y entretenidas. Tanto en estas
clases como en la bibliografía el énfasis está puesto en estudiar /
encontrar / desarrollar / identificar los conceptos con los cuales
generar abstracciones para resolver problemas con la computadora, más
que en enseñar la sintaxis de un lenguaje de programación. También está
disponible online [el curso CS 61A actual](https://cs61a.org) (cuyo
lenguaje principal es Python 3) con acceso a todo el material con el que
cuentan los alumnos (generoso, abrumador, envidiable, es impresionante
el interés por enseñar que tienen esos equipos de profesores y
auxiliares). Acá pueden ver la primera clase del 2008 (desde YouTube).

{{< youtube xWZb9U92rgo >}}

También está online el curso completo \"Structure and Interpretation of
Computer Science\" basado en el libro homónimo, con [las clases de 1986
en
video](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video-lectures/)
(la primera edición del libro es de 1985, y la segunda de 1996, esta
última es la que está online y aparece en un link más arriba). Hay que
acostumbrarse al hecho de que sean grabaciones viejas de menor calidad a
los tutoriales en 1080p de YouTube que se ven actualmente, pero el
contenido lo merece.

Se me hizo un lío hasta descubrir por dónde empezar, con tanto material
extraordinario. El SICP es el libro clásico que todo el mundo recomienda
en los foros, pero no es sencillo. Por suerte descubrí que el libro de
Harvey-Wright se propone como precuela (lo dicen en el prólogo) y es
recomendable leerlo antes, como preparación para el de Abelson-Sussman.

{{< figure src="https://c1.staticflickr.com/5/4563/38677380062_73929181b2_o.jpg" title="Portada de Simply Scheme" >}}

También está buenísimo \"The Little Schemer\" que lo tenía guardado
desde hace mucho. Apenas voy por la mitad, pero ya mismo puedo
recomendarlo porque me parece muy apropiado para entender, por ejemplo,
la recursividad y cómo usarla, algo central en LISP. El texto está
organizado con la estructura de [enseñanza
programada](https://es.wikipedia.org/wiki/Enseñanza_programada). En esta
modalidad (que conocí en una serie de libros que tenía mi hermano,
\"[Curso Programado de
Cálculo](https://www.amazon.com/Curso-programado-cálculo-Sucesiones-infinitas/dp/8429150552)\"
de Editorial Reverté, que usé en la secundaria cuando quise prepararme
para la universidad) la información se presenta secuencialmente en
pequeños párrafos que contienen problemas o frases para resolver y
completar. En la misma hoja están las soluciones a los problemas y las
palabras faltantes. El lector trata de responder y completar los
espacios en blanco mientras tapa las respuestas, de manera que cuando
termina puede comparar sus resultados con las soluciones correctas. Será
conductista pero es muy entretenido, la presentación va avanzando en
pasos muy pequeños y al menos a mi me genera un estímulo muy agradable
ir descubriendo la coincidencia o cercanía de las respuestas propias a
las indicadas por el autor. Estaría bueno que haya más libros con esta
modalidad.

{{< figure src="https://c1.staticflickr.com/5/4531/38677094272_d56db10a21_b.jpg" title="Una página del libro de enseñanza programada" width=75% >}}

Por suerte todos estos libros están disponibles gratuitamente o se
consiguen con algún torrent, porque por un lado no están disponibles en
Argentina, y sus precios (en
[BookDepository](https://www.bookdepository.com), que no cobra el costo
de envío, Amazon no los envía a nuestro país) son altísimos. SICP cuesta
casi 1000 ARS, Simply Scheme más de 1300 ARS, The Little Schemer casi
700 ARS, etc.

En un próximo post voy a explicar cómo uso Scheme desde el shell o desde
Emacs para probar los pequeños programas que los libros tienen de
ejemplo o los que surgen de los problemas que proponen.

