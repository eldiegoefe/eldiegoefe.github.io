:title: Mageia y Manjaro
:date: 2014-10-22 10:00
:category: tecnicismos
:tags: mageia, manjaro, particiones, terminal
:author: El Diego Efe
:excerpt: Mageia con problemas, instalación de Manjaro
:disqus_identifier: mageia y manjaro

Empezó a haber problemas para actualizar el sistema (`Mageia`_), que
mostraba un mensaje diciendo que había actualizaciones listas para
instalarse, pero no hacía nada al hacer click sobre *instalar*. Logré
que se produzca la instalación desde una consola con **sudo urpmi
--auto-update**.

.. _Mageia: https://www.mageia.org/es/

También dejó de funcionar el programa de configuración del sistema al
que se accede desde *herramientas/herramientas del sistema/configure su
computador*. Pero en algún momento volvió a andar. :)

Finalmente tuve problemas para instalar `Julia`_. No había manera de
que compile, y los errores no parecían lógicos. Aproveché para postear
`mi primer "Issue" en GitHub`_, en el repositorio de Julia. Estuvo
bueno porque me respondieron inmediatamente tratando de ayudarme, con
lo cual le perdí un poco el miedo a la experiencia de la interacción.

.. _Julia: http://julialang.org/
.. _mi primer "Issue" en GitHub: https://github.com/JuliaLang/julia/issues/8669

Pero el problema persistía y no quería seguir perdiendo tiempo
intentando soluciones que seguían fallando, con síntomas bastante
ilógicos, (y cuando la lógica parece no funcionar mi respuesta
inmediata es tratar de resetear todo). Sumado a eso, tenía previsto
instalar `Manjaro`_ desde que me entusiasmé con él en una máquina
virtual, y por si fuera poco el disco rígido me pedía una
reorganización a gritos, dado que tenía tres cuartas partes
inutilizadas por una distribución de particiones anómala, que
arrastraba desde la época en que tenía `Fedora`_.

.. _Fedora: http://fedoraproject.org/es/
.. _Manjaro: http://manjaro.org/

La instalación de Manjaro tuvo algunos inconvenientes porque no tengo
aún muy clara la cuestión del reemplazo de BIOS por UEFI. Ahora ya no
recuerdo tanto, pero el problema que tenía con el instalador gráfico
de Manjaro era que no me dejaba formatear y reparticionar a mi gusto
(no tenía la opción UEFI), lo cual sí pude hacer con el instalador
tipo terminal, que resultó ser bastante amigable. Lo más complicado al
particionar era que el tamaño de las particiones las pedía en
sectores, así que tenía que hacer "regla de tres" para obtener el
número de sectores correspondientes a los 50 Gb que quería, con lo que
terminaba tecleando un número de sectores con una cantidad importante
de dígitos.

Acá pueden ver la pantalla desde la cual escribo, con la nueva
instalación de Manjaro.

.. figure:: https://farm9.staticflickr.com/8584/16105314727_ae59b535dc_b.jpg
   :width: 100%
   :align: center
   :alt: pantalla con Manjaro
   :target: https://farm9.staticflickr.com/8584/16105314727_dbdb879673_o.png

   Pantalla con Manjaro

No abandoné la tarea de instalar con UEFI, a pesar de que me llevó
toda una tarde, porque con este nuevo sistema no hay limitación en el
número de particiones del disco. En cambio en el viejo y estándar BIOS
sólo se pueden hacer 4 primarias, lo cual complica las cosas al querer
tener varias distribuciones de Linux simultáneamente aptas para
bootear la computadora, que es lo que quiero hacer. Ahora llevo una
semana con Manjaro y viene todo perfecto, pero igual en algún momento
voy a continuar con el testeo de distribuciones, así que espero que lo
que haya hecho (dejar varias particiones vacías de 50 Gb) sirva para
esas posteriores instalaciones.

Finalmente, recomiendo que sean valientes y experimenten con
diferentes distribuciones de Linux, desde Fedora hasta acá todas han
tenido algún problema, pero quizás porque instalo diferentes paquetes
y pruebo cambios de configuración y eso lleva a que ocurran fallos. Un
usuario un poco más conservador que yo seguramente no va a tener
problemas con las distribuciones que les vengo comentando.

- `Guía de instalación de Manjaro con UEFI`_

  .. _Guía de instalación de Manjaro con UEFI: https://wiki.manjaro.org/index.php?title=UEFI_-_Install_Guide
