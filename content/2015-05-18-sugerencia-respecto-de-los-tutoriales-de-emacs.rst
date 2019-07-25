Sugerencia respecto de los tutoriales de Emacs
##############################################

:date: 2015-05-18 10:00
:category: tecnicismos
:tags: emacs
:author: El Diego Efe
:excerpt: Sugerencia respecto de los tutoriales de Emacs
:disqus_identifier: Sugerencia respecto de los tutoriales de Emacs

To read this entry in english: `click here`_

.. _click here: {filename}/2015-05-18-suggestion-about-emacs-tutorials.rst

Leo bastantes blogs sobre Emacs desde que empecé el viaje de aprender
a usarlo. Hay tutoriales buenísimos para principiantes y también
páginas destinadas a usuarios más avanzados. Sin embargo, en la
mayoría de los sitios se repite una costumbre que desestima una de las
ventajas que tiene el Todopoderoso Editor (su capacidad de
personalización): las instrucciones para hacer tal o cual cosa suelen
aparecer con sus atajos de teclado por defecto, como si fuese
invariable que abrir un archivo (visitarlo) se haga con C-x C-f, o
como si los únicos keybindings para ir a los extremos de la linea
donde se ubica el cursor sean C-a y C-e, o como si realizar búsquedas
incrementales requiera indefectiblemente teclear C-s. En mi caso, las
combinaciones de tecla para estas funciones, entre muchas otras, están
personalizadas, sin que muchas veces funcionen los atajos por defecto
(por ejemplo abro los archivos con C-o, muevo el cursor a los extremos
con M-h y S-M-h, y activo las "búsquedas incrementales" con C-f).

Mi sugerencia a toda la comunidad de educadores de Emacs es que en vez
de referirse a las combinaciones de tecla, en sus tutoriales y
comentarios coloquen siempre los nombres de las funcionen que sugieren
utilizar. Por ejemplo, en vez de escribir C-s deberían hablar de
isearch-forward, o en vez de C-a sería mejor indicar el comando
move-beginning-of-line. De esta manera, uno puede seguir las
instrucciones paso a paso utilizando execute-extended-command (que
generalmente se ejecuta con M-x, aunque en mi instalación eso sucede
con M-a).

Si uno necesita saber cuál es la combinación de teclas asociada a una
función (a la función que promueve el tutorial) puede ejecutar
describe-function para tener un resumen de la misma y ver sus
keybindings.
