Generar pdf en español desde org-mode
#####################################

:date: 2014-08-06 10:00
:category: tecnicismos
:tags: emacs, org-mode, pdf
:author: El Diego Efe
:excerpt: Como generar pdf en español desde org-mode
:disqus_identifier: generar pdf desde org

Escribí un documento en org-mode (un modo mayor de emacs), porque
permite exportar en formato pdf y escribir todo en texto plano. Es
realmente una maravilla, se pueden escribir fórmulas en LaTeX, y
organizar la estructura del documento usando títulos precedidos de uno
o más asteriscos para indicar su nivel (si es un título principal, un
subtitulo, un subsubtítulo, etc.). Hasta genera automáticamente una
tabla de contenidos con todos estos títulos al hacer la exportación
del documento (keybinding: C-c C-e l o).

Pero tenía el problema de que la fecha y la tabla de contenidos,
aparecían escritas en inglés. Estuve buscando un rato largo el modo de
pasarlo a castellano, y finalmente lo encontré en la página de
Nurullah Akkaya, `Writing papers using org-mode`__

__ http://nakkaya.com/2010/09/07/writing-papers-using-org-mode/

En el encabezado hay que agregar

::

 #+LATEX_HEADER: \usepackage[spanish]{babel}

Sin embargo esto tiene un comportamiento medio raro, ya que además
requiere esta linea previa:

::

 #+LANGUAGE: es

Es extraño porque esta última linea es una directiva para generar html
y no pdf. Además me dio siempre el resultado en castellano aunque
probé también con *fr*, *pt*, *de*, ...; parecía que andaba siempre
igual, en español, pero al colocar *en* volvió a salir el texto en
inglés.
