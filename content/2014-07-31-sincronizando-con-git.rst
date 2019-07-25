Sincronizando con Git
#####################

:date: 2014-07-31 10:00
:category: tecnicismos
:tags: git, blog
:author: El Diego Efe
:excerpt: Un detalle sobre la sincronización de ramas con Git
:disqus_identifier: sincronizando con github

Estuve tratando de escribir este blog desde dos computadoras
distintas. Armé el sitio desde una de ellas (una PC de escritorio)
siguiendo las instrucciones que puse en otro post y después subí el
sitio a github con un pull. Quedan armadas tres ramas (branches) en
los repositorios:

    - source
    - master
    - gh-pages

Me cambié de máquina (a una laptop) e hice una copia de lo que había
subido clonando el supositorio, digo el repositorio remoto. Después me
puse a trabajar, armé nuevos post y corregí algunos otros. Hice el
agregado de los archivos al repositorio local y su correspondiente
*commit*. Finalmente un *"git push --all"* y con eso creo que se actualizó
el repositorio remoto.

El problema se me presentó al querer sincronizar los archivos en la PC
de escritorio, para volver a editar desde allí al blog pero sin perder
la edición que había hecho desde la otra máquina. Tenía entonces que
actualizar los archivos locales con los que estaban en el repositorio
remoto. Mi confusión surgió porque aparecía un mensaje (que ya no
recuerdo y no puedo recuperar) en donde git me decía que había algún
problema con elegir la rama, o algo así. Yo lo que había intentado,
intuitivamente, era un *"git pull --all"* y también un *"git pull"* y
*"git pull source"* pero en todos los casos algún error aparecía. La
solución fue ejecutar, estando en la rama *source* la siguiente
instrucción (sólo me había faltado agregar *origin* en mis intentos),
que hace un fetch y un merge con la rama *source* del repositorio
remoto (antes de ejecutarla, asegurarse de estar en la rama *source*
local):

.. code-block:: console

    $ git pull origin source

¡Felicidad!
