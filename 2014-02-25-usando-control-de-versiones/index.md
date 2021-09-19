# Usando control de versiones


(Editado: empecé a traducir un buen tutorial de Git y lo pueden ver en
[este nuevo post]({{< ref "/posts/2014/2014-10-06-control-de-versiones-1.md" >}})

El año pasado conocí algo que ya se había cruzado en mi camino y no me
había dado cuenta. Una necesidad lo requería: miles de versiones del
mismo archivo con el nombre evolucionando con rastros de racionalidad
pero en definitiva impidiendo saber si, tras dos o tres días de
ausencia, me encontraba trabajando sobre la última versión o si la que
decía \"*ultima final para imprimir final b*\" era realmente la que debía
utilizar. Tanto sea un documento de texto como un programa es
imprescindible tener algún método, y el método manual que utilizo desde
que tengo uso de memoria ya ven lo deficiente que es.

Por el lado ya no de la necesidad sino del efectivo uso del control de
versiones, encontré interesante la funcionalidad de las wikis, que van
almacenando todas las versiones previas y no tan solamente la última,
que es la que muestran; pudiéndose recuperar una versión más antigua e
incluso comparar la versión del texto actual con cualquier versión
previa.

Así fue como el año pasado me entusiasmé leyendo sobre **mercurial, git,
commits, branches, bitbuckets, githubs y palabrerío relacionado**. Advertí que
incluso está presente todo eso en software ampliamente diverso que yo había
usado en el pasado (como labview o lyx), pero no le había dado la menor bola.

Github es un sitio web que ofrece el sistema de control de versiones, un
servicio de alojamiento de archivos con la funcionalidad asociada de recuperar
versiones anteriores y todo lo relacionado con ello. Es ampliamente mencionado y
usado por los desarrolladores y comunidades de software libre (creo que es el
sitio elegido para cobijar las distintas versiones del kernel de linux). Es
sumamente interesante que estén a disposición de los navegantes todos los
códigos fuentes allí alojados, de manera tal que uno puede \"clonar\" todos esos
archivos (escritos en el idioma que sea) y trabajar con ellos en la computadora
personal propia. La idea es que cualquiera puede realizarle mejoras al programa
y pedir, mediante el propio sistema que ofrece el motor del sitio, la inclusión
de sus aportes al código fuente del programa.

Copio acá algunos apuntes mios del uso de GIT, no es un tutorial (ya hay muchos
en la web, como el de [Lars
Vogel](http://www.vogella.com/tutorials/Git/article.html), sino más bien un
ayuda-memoria para mi mismo, que estoy permanentemente buscando los comandos.
Espero poder recordarlos a medida que los use...

Un repositorio es un conjunto de archivos correspondientes a un mismo
proyecto, y con la misma palabra se designa al espacio donde estos se
alojan. En general un desarrollador conserva un repositorio local (un
directorio con todos los archivos en su propia computadora) y un
repositorio remoto (en un sitio como github, bitbucket, etc).

Un mismo repositorio puede tener una o varias ramas (branches). **Puede estar
habilitada una sola rama en cada momento**, la cual muestra el conjunto de
archivos y directorios contenidos en esa rama.

En el archivo [.gitignore] (que puede estar en cualquier subdirectorio del
repositorio) se listan los archivos que deben ignorarse. Por ejemplo [\*.pyc]
(los archivos de python compilados) o los [\*.exe] (lo que se controla con este
sistema son las versiones del código fuente en modo texto, no los archivos
binarios).

**.git** (es un directorio) contiene la historia completa del
repositorio. El contenido sólo lo manipula el motor del sistema y no el
usuario.

**.git/config** contiene la configuración local del repositorio

Los comandos más usados pueden estar entre los siguientes:

``` console
git init # Inicializamos el repositorio local Git
git add . # Agregamos todo (archivos y directorios) al repositorio
git commit -m "Initial commit" # Hacemos un commit al repositorio
git log # Muestra el log (un historial)
git add # Para agregar cosas al index stage (indice).
git a # Idéntico al anterior
git remote -v # Para ver a donde apunta el origin
git remote add origin git@github.com:usuario/repo.git # Para cambiar el origin
git remote rm origin # Para elimiar el origin
git push # Para enviar los cambios al repositorio
git pull # Para traer los cambios desde el repositorio
git branch # Para ver las distintas ramas existentes
git branch nombre-de-la-nueva-rama # Para crear una rama
git checkout nombre-de-la-otra-rama # Para cambiar a otra rama
git commit -a -m "Mensaje de commit" # Para comitear
git branch -d nombre-del-branch-a-borrar # Para borrar un branch
```

