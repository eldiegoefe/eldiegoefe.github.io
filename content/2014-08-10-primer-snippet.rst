:title: Primer snippet
:date: 2014-08-10 10:02
:category: tecnicismos
:tags: emacs, yasnippets
:author: El Diego Efe
:excerpt: Este es el primer snippet hecho para automatizar el
          encabezado de las paginas hechas en restructuredText
:disqus_identifier: primer snippet

Este es el primer snippet diseñado para automatizar el encabezado de
las paginas hechas en restructuredText, para facilitarme la escritura
de este blog. Hay mucha ayuda en la `página de Capitao Morte`_
(supongo que es su autor).

.. _página de Capitao Morte: http://capitaomorte.github.io/yasnippet/

.. code-block:: rest
   :linenos:

   # -*- mode: snippet; require-final-newline: nil -*-
   # name: encabezado
   # key: enc
   # expand-env: ((yas-indent-line 'fixed))
   # --

   :title: ${1:titulo}
   :date: ${2:2014}-{3:10}-{4:31} {5:10:00}
   :category: ${6:$$(yas-choose-value '("blog" "politica" "salud" "tecnicismos"))}
   :tags: $7
   :author: El Diego Efe
   :excerpt: $1

   $0

En la linea 14 la instrucción $0 se agregó porque en algún lado decía
que suele ponerse para indicar el lugar de salida cuando se termina de
ejecutar el snippet.

La linea 4 está para que la indentación aparezca correcta al
ejecutarse el snippet, ya que sin
esta linea aparecían unas tabulaciones erróneas.

**¿Dónde guardar el archivo?**

No conviene guardar el snippet nuevo en el directorio donde se
almacena automáticamente el paquete *yasnippets* porque al actualizar
este paquete se perderá nuestra creación.

Hay que verificar el valor de la variable donde se almacenan los
directorios para los snippets personalizados (mediante **M-x
customize-variable yas-snippet-dirs**). Al chequear veo que uno de los
directorios es *~/.emacs.d/snippets* pero cuando me fijo con el
navegador encuentro que aún no existe, así que lo creo (desde **M-x
dired**). Luego también creo un subdirectorio para mantener la lógica
de los nombres bajo
*~/.emacs.d/elpa/yasnippet-XXXXXXXX.XXXX/snippets*, donde a cada modo
mayor se le asigna un subdirectorio. Por lo tanto, para mi ultra
magnífico snippet de restructuredText, corresponde guardarlo así (sin
ninguna extensión):

.. code-block:: bash

 ~/.emacs.d/snippets/rst-mode/encabezado

**Otra cosa**: para poder colocar código con números
de línea en estas páginas (escritas con restructuredText) hay
que tener en cuenta lo siguiente:

 + debajo del **.. code-block::** se debe incluir la directiva
   **:linenos:**. No se si es un bug, pero esa directiva debe estar
   alineada con la palabra **code** para que funcione, y todo el
   bloque de código debe también respetar esta alineación. Para
   tabular un bloque de texto manteniendo las indentaciones que ya
   tiene se puede usar *M-x indent-rigidly*.

 + el nombre del lenguaje en **.. code-block::** parece que debe ir en
   minúsculas, para que sea reconocido y funcione el coloreado con
   pygments. En el caso de restructuredText la palabra clave que
   funcionó (por prueba y error) es rest. (Editado: luego encontré la
   página con los "lexers" válidos: `Available lexers`_, y vi que
   también eran válidos rst y restructuredtext).

.. _Available lexers: http://pygments.org/docs/lexers/
