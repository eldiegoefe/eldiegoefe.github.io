# Tutorial sobre control de versiones (parte 1)

-

En el sitio de [Software Carpentry](http://software-carpentry.org/) hay un buen
tutorial sobre el uso de sistemas de control de versiones. Estos apuntes son
prácticamente la traducción de esas instrucciones.

## Indice del Tutorial

- [Parte 1]({{< ref "2014-10-06-control-de-versiones-1.md" >}}). Cómo armar un repositorio local
- [Parte 2]({{< ref "2014-10-07-control-de-versiones-2.md" >}}). Cómo subir el repositorio local al remoto
- [Parte 3]({{< ref "2014-10-09-control-de-versiones-3.md" >}}). Cómo colaborar en un mismo repositorio remoto
- [Parte 4]({{< ref "2014-10-10-control-de-versiones-4.md" >}}). Cómo resolver conflictos

Para ver las versiones (en inglés) en las cuales se basa este tutorial, podés
visitar [la página de Software
Carpentry](http://software-carpentry.org/v5/novice/git/)

## Configuración

La primera vez que se usa Git en una máquina hay que configurar al menos el
nombre del usuario y su email. También puede elegirse el editor por defecto. Son
comandos que se ejecutan una sola vez. Por ejemplo:

``` powershell
$ git config --global user.name "Vlad Dracula"
$ git config --global user.email "vlad@tran.sylvan.ia"
$ git config --global color.ui "auto"
$ git config --global core.editor "emacs"
```

La tercer opcion es para que los mensajes con los cuales responde Git en el
terminal estén coloreados. La cláusula \"\--global\" indica que esta
configuración no se limita a un proyecto particular, sino que será utilizado en
todos los proyectos (repositorios) de esa computadora.

Para verificar el nombre de usuario se usa *git config user.name*.

## Inicialización

Se puede comenzar a trabajar con un proyecto usando el siguiente comando desde
el subdirectorio en el cual se alojarán los archivos del proyecto:

``` powershell
$ git init
```

De esta manera se crea un subdirectorio oculto (.git) donde se irá alojando todo
el historial de archivos, en todas sus versiones, a medida que se vayan
produciendo.

## Agregar un archivo al proyecto

Creamos un archivo de texto con cualquier editor (no necesariamente el elegido
en la configuración) y lo almacenamos en el directorio del proyecto. Por ejemplo
una canción de La Vela Puerca, en el archivo *va-a-escampar.txt*:

    Va a escampar

    Hoy asume lo que venga
    sea para bien, o todo mal.
    y aunque pierda lo que tenga
    se va a morder para aguantar

Si hacemos *\"git status\"* el sistema nos responde que reconoce la existencia
de un nuevo archivo en el proyecto, que todavía el sistema de control de
versiones no incorporó.

``` console
$ git status
# On branch master
#
# Initial commit
#
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#    va-a-escampar.txt
nothing added to commit but untracked files present (use "git add" to track)
```

Para agregar el archivo al proyecto se ejecuta:

``` console
$ git add va-a-escampar.txt
```

Y se puede pedir el nuevo informe de situación con:

``` console
$ git status
# On branch master
#
# Initial commit
#
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#
#    new file:   va-a-escampar.txt
#
```

## Comitear es un verbo muy extraño

Ahora Git ya sabe que debe ir registrando la evolución de *va-a-escampar.txt*,
pero todavía no ha grabado ninguna información sobre este archivo en su base de
datos (y si ya hubiese información de antes, aún no habría guardado los cambios
realizados desde el último *commit*). En inglés, grabar el estado actual de uno
o más archivos es hacer un **commit**. En castellano commit puede traducirse
como cometer, hacer, encomendar, perpetrar... Ninguna de las cuales sirve para
describir lo que sucede, así que hablaremos de **comitear**.

Para *comitear* el estado actual del archivo se ejecuta la orden *git commit -m
\"mensaje personal\"*:

``` console
$ git commit -m "Empezando a transcribir la letra de La Vela"
[master (root-commit) 38b86f5] Empezando a transcribir la letra de La Vela
1 file changed, 6 insertions(+)
create mode 100644 va-a-escampar.txt
```

Git guarda entonces un copia permanente de todos los archivos que están en la
base de datos (los que fueron agregados con **git add** dentro del directorio
oculto *.git*. Esta copia permanente es llamada una *revisión*, y su
identificador en el ejemplo fue 38b86f5.

De omitir el mensaje en el comando *git commit* (si no hubiese aparecido
-m \"mensaje\"), se hubiese abierto el editor configurado al principio,
para poder escribir el mensaje.

Volvemos a ver la situación actual del proyecto con **git status** y con **git
log** podemos ver el historial de cambios (en orden cronológico inverso), el
cual incluye el identificador completo de la revisión, el autor, la fecha y el
mensaje de Git al responder al commit:

``` console
$ git status
# On branch master
nothing to commit, working directory clean

$ git log
commit 38b86f5625453732e442c127f1d4678ec8550a12
Author: eldiegoefe <eldiegoefe@gmail.com>
Date:   Mon Oct 6 15:35:07 2014 -0300

   Empezando a transcribir la letra de La Vela
```

## Cambios (o agregados) en un archivo

> **¿Dónde se guardan los cambios?**
>
> En el directorio del proyecto sigue habiendo un solo archivo. Toda la
> información extra se almacena en el subdirectorio oculto *.git*, de
> modo que el sistema de archivos se ve limpio y se evita la posibilidad
> de borrar accidentalmente cosas (como versiones viejas del mismo
> archivo).

Si agregamos una segunda estrofa al archivo de texto, pasa a verse así:

    Va a escampar

    Hoy asume lo que venga
    sea para bien, o todo mal.
    y aunque pierda lo que tenga
    se va a morder para aguantar

    Hoy que claro ve las cosas
    que ayer no vio, ni va a exigir
    Sobre su pena se posa
    quiere entender para seguir

Al pedir el status del proyecto veremos:

``` console
$ git status
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#    modified:   va-a-escampar.txt
#
no changes added to commit (use "git add" and/or "git commit -a")
```

La última linea es la frase clave: \"no se agregaron cambios al
commit\". El archivo ha cambiado pero no le hemos dicho aún a Git que
queremos guardar esos cambios (lo haremos con *git add*).

## Comparación de versiones

Antes de agregar estos cambios podemos revisar nuestro trabajo usando
*git diff*, que nos muestra las diferencias entre el estado actual del
archivo y la última versión comiteada.

``` console
$ git diff
diff --git a/va-a-escampar.txt b/va-a-escampar.txt
index 97ab7b0..db818ec 100644
--- a/va-a-escampar.txt
+++ b/va-a-escampar.txt
@@ -4,3 +4,8 @@ Hoy asume lo que venga
 sea para bien, o todo mal.
 y aunque pierda lo que tenga
 se va a morder para aguantar
+
+Hoy que claro ve las cosas
+que ayer no vio, ni va a exigir
+Sobre su pena se posa
+quiere entender para seguir
```

La salida es críptica porque en realidad es una serie de comandos para
que un editor de textos pueda reconstruir un archivo a partir del otro.

1.  La primera linea muestra que Git produce una salida similar al
    comando Unix *diff* comparando la versión antigua y nueva del
    archivo.
2.  La segunda linea muestra la revisión exacta de cada archivo que está
    siendo comparado (97ab7b0 y db818ec, etiquetas únicas generadas por
    la computadora para esas revisiones).
3.  La linea restante muestra finalmente las lineas en las que aparecen
    las diferencias (marcando con \"+\" las lineas que se agregaron).

## Cómo comitear los cambios

Si hacemos un commit de los cambios:

``` console
$ git commit -m "Agregada la segunda estrofa"
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#    modified:   va-a-escampar.txt
#
no changes added to commit (use "git add" and/or "git commit -a")
```

**Ups. No se comitearon los cambios porque faltó agregarlos antes**.
Entonces, haremos:

``` console
$ git add va-a-escampar.txt
$ git commit -m "Agregada la segunda estrofa"
[master 6ae57e3] Agregada la segunda estrofa
1 file changed, 5 insertions(+)
```

Git insiste en que agreguemos los archivos al conjunto de los que
querramos comitear antes de realmente hacerlo, porque quizás no
querramos comitear todo junto. Por ejemplo, supongamos que estamos
agregando algunas citas a un documento. Podríamos querer agregarlas sin
comitear el trabajo que estamos haciendo en las conclusiones (que
todavía no terminamos). *NOTA PERSONAL: ¡no entiendo! ¿De qué me sirve
agregar los cambios si no los \"comiteo\"?*

RESPUESTA: Para permitirlo, Git tiene una zona de almacenamiento
especial donde hace un seguimiento de cosas que fueron agregadas al
último conjunto de cambios, pero que aún no fueron comiteadas. Con *git
add* se colocan las novedades en este area, y luego *git commit* las
copia al espacio de almacenamiento de largo plazo.

![git staging and commit areas](http://software-carpentry.org/v5/novice/git/img/git-staging-area.svg){.align-center
width="100.0%"}

Veamos cómo nuestros cambios a un archivo se mueven desde nuestro editor
hacia la *staging area* (zona de preparación o también area de ensayo) y
hacia el almacenamiento de largo plazo. Primero, agregamos otra estrofa:

    Llega la batalla
    y contra él estalla
    algún día va a escampar.
    y como sale de esta
    quiere la respuesta
    sabe que no es escapar.

Y analizamos las diferencias con *git diff*:

``` console
$ git diff
diff --git a/va-a-escampar.txt b/va-a-escampar.txt
index db818ec..0c33091 100644
--- a/va-a-escampar.txt
+++ b/va-a-escampar.txt
@@ -9,3 +9,10 @@ Hoy que claro ve las cosas
 que ayer no vio, ni va a exigir
 Sobre su pena se posa
 quiere entender para seguir
+
+Llega la batalla
+y contra él estalla
+algún día va a escampar.
+y como sale de esta
+quiere la respuesta
+sabe que no es escapar.
```

Git identifica las diferencias entre el archivo y la versión intermedia
(pero no comiteada), guardada en la *staging area* (la voy a llamar
*zona de preparación*). Si agregamos estos cambios al almacenamiento
intermedio, veremos lo siguiente:

``` console
$ git add va-a-escampar.txt
$ git diff
```

Ahora no hay ninguna salida, porque el archivo actualmente en edición es
igual al que guardamos en la *zona de preparación*.

Sin embargo, si hacemos:

``` console
$ git diff --staged
diff --git a/va-a-escampar.txt b/va-a-escampar.txt
index db818ec..0c33091 100644
--- a/va-a-escampar.txt
+++ b/va-a-escampar.txt
@@ -9,3 +9,10 @@ Hoy que claro ve las cosas
 que ayer no vio, ni va a exigir
 Sobre su pena se posa
 quiere entender para seguir
+
+Llega la batalla
+y contra él estalla
+algún día va a escampar.
+y como sale de esta
+quiere la respuesta
+sabe que no es escapar.
```

Ahora nos está mostrando las diferencias entre el último cambio
comiteado (en el almacenamiento de largo plazo) y lo que hay en la *zona
de preparación*. Guardemos estos cambios:

``` console
$ git commit -m "Tercera estrofa agregada"
[master 8f1eec1] Tercera estrofa agregada
 1 file changed, 7 insertions(+)
```

Vemos cómo quedó:

``` console
$ git status
# On branch master
nothing to commit, working directory clean
```

Y podemos examinar la historia de lo que fue sucediendo hasta ahora:

``` console
$ git log
commit 8f1eec1836a9ace8a2cbab7e2c3341efa5c3a537
Author: eldiegoefe <eldiegoefe@gmail.com>
Date:   Mon Oct 6 19:55:10 2014 -0300

    Tercera estrofa agregada

commit 6ae57e3d91a7a526a257df081d83a5b9be4e6d28
Author: eldiegoefe <eldiegoefe@gmail.com>
Date:   Mon Oct 6 16:54:40 2014 -0300

    Agregada la segunda estrofa

commit 38b86f5625453732e442c127f1d4678ec8550a12
Author: eldiegoefe <eldiegoefe@gmail.com>
Date:   Mon Oct 6 15:35:07 2014 -0300

    Empezando a transcribir la letra de La Vela
```

Resumiendo, cuando queremos hacer cambios en nuestro repositorio,
primero tenemos que agregar los cambios a la *zona de preparación* (con
*git add*), y luego *comitear* los cambios ensayados al repositorio (con
*git commit*).

![trabajando con git](http://software-carpentry.org/v5/novice/git/img/git-committing.svg){.align-center
width="100.0%"}

## Explorando el historial

Para ver lo que cambiamos, usamos *git diff* también, pero para
refiriéndonos a versiones viejas con la notación HEAD\~1, HEAD\~2, etc:

``` console
$ git diff HEAD~1 va-a-escampar.txt
diff --git a/va-a-escampar.txt b/va-a-escampar.txt
index db818ec..0c33091 100644
--- a/va-a-escampar.txt
+++ b/va-a-escampar.txt
@@ -9,3 +9,10 @@ Hoy que claro ve las cosas
 que ayer no vio, ni va a exigir
 Sobre su pena se posa
 quiere entender para seguir
+
+Llega la batalla
+y contra él estalla
+algún día va a escampar.
+y como sale de esta
+quiere la respuesta
+sabe que no es escapar.
```

``` console
$ git diff HEAD~2 va-a-escampar.txt
diff --git a/va-a-escampar.txt b/va-a-escampar.txt
index 97ab7b0..0c33091 100644
--- a/va-a-escampar.txt
+++ b/va-a-escampar.txt
@@ -4,3 +4,15 @@ Hoy asume lo que venga
 sea para bien, o todo mal.
 y aunque pierda lo que tenga
 se va a morder para aguantar
+
+Hoy que claro ve las cosas
+que ayer no vio, ni va a exigir
+Sobre su pena se posa
+quiere entender para seguir
+
+Llega la batalla
+y contra él estalla
+algún día va a escampar.
+y como sale de esta
+quiere la respuesta
+sabe que no es escapar.
```

De esta manera construimos una cadena de revisiones. El extremo más reciente de
la cadena es HEAD; podemos referirnos a revisiones previas usando la notación
\~, de manera que HEAD\~1 (se pronuncia \"head menos uno\") significa \"la
revisión previa\", mientras que HEAD\~123 vuelve 123 revisiones hacia atrás,
desde donde nos encontramos en la actualidad.

También nos podemos referir a las revisiones usando las cadenas largas de
dígitos y letras que Git muestra en los logs. Estos son IDs únicos para los
cambios, \"únicos\" significa realmente únicos: cada cambio a cualquier conjunto
de archivos en cualquier máquina tiene un identificador de 40 caracteres.
Nuestro primer commit nos dio el ID 38b86f5625453732e442c127f1d4678ec8550a12,
así que probemos esto:

``` console
$ git diff 38b86f5625453732e442c127f1d4678ec8550a12 va-a-escampar.txt
diff --git a/va-a-escampar.txt b/va-a-escampar.txt
index 97ab7b0..0c33091 100644
--- a/va-a-escampar.txt
+++ b/va-a-escampar.txt
@@ -4,3 +4,15 @@ Hoy asume lo que venga
 sea para bien, o todo mal.
 y aunque pierda lo que tenga
 se va a morder para aguantar
+
+Hoy que claro ve las cosas
+que ayer no vio, ni va a exigir
+Sobre su pena se posa
+quiere entender para seguir
+
+Llega la batalla
+y contra él estalla
+algún día va a escampar.
+y como sale de esta
+quiere la respuesta
+sabe que no es escapar.
```

Para no tipear cadenas de 40 números, Git permite usar los primeros de la
cadena, con el mismo resultado:

``` console
$ git diff 38b86f5 va-a-escampar.txt
```

## Recuperar versiones antiguas

De acuerdo: podemos grabar cambios a los archivos y ver qué hemos cambiado. Pero
¿cómo restauramos versiones viejas de las cosas? Supongamos que sobreescribimos
accidentalmente nuestro archivo va-a-escampar.txt, que pasa a contener sólo la
siguiente linea:

    no va a escampar nada

El comando *cat* muestra el contenido del archivo:

``` console
$ cat va-a-escampar.txt
no va a escampar nada
```

Con *git status* nos enteramos que el archivo ha cambiado, pero esos
cambios aún no pasaron a la *zona de preparación* (*staging area*).

``` console
$ git status
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#    modified:   va-a-escampar.txt
#
no changes added to commit (use "git add" and/or "git commit -a")
```

Podemos volver atrás, dejando las cosas como estaban antes, usando *git
checkout*:

``` console
$ git checkout HEAD va-a-escampar.txt
$ cat va-a-escampar.txt

Va a escampar

Hoy asume lo que venga
sea para bien, o todo mal.
y aunque pierda lo que tenga
se va a morder para aguantar

Hoy que claro ve las cosas
que ayer no vio, ni va a exigir
Sobre su pena se posa
quiere entender para seguir

Llega la batalla
y contra él estalla
algún día va a escampar.
y como sale de esta
quiere la respuesta
sabe que no es escapar.
```

Con *git checkout* se recupera una versión anterior de un archivo. En
este caso, le estamos pidiendo a Git que recupere la versión del archivo
guardada en HEAD, que fue la última revisión guardada. Si quisiéramos ir
más atrás podríamos usar un identificador de revisión:

``` console
$ git checkout 38b86f5 va-a-escampar.txt
```

Es importante recordar que debemos usar el número de revisión que identifica el
estado del repositorio antes del cambio que estamos tratando de revertir. Un
error común es usar el número de revisión del commit en el cual hicimos el
cambio del cual estamos tratando de deshacernos. En el ejemplo de abajo queremos
recobrar el estado inmediatamente anterior al commit más reciente (HEAD\~1), que
es la revisión 6ae57e3d9 (en la figura -realizada con otro ejemplo-corresponde a
la revision f22b25e):

![retornando a una revisión anterior de un archivo](http://software-carpentry.org/v5/novice/git/img/git-checkout.svg){.align-center
width="90.0%"}

El diagrama siguiento ilustra el modo en que puede verse la historia de un
archivo (moviéndose hacia atrás desde HEAD, la versión más recientemente
comiteada):

![historia de las revisiones de un archivo](http://software-carpentry.org/v5/novice/git/img/git-when-revisions-updated.svg){.align-center
width="90.0%"}

    Simplificando un caso común

    Si mirás cuidadosamente la salida de *git status*, vas a ver esta
    ayuda:

    (use "git checkout -- <file>..." to discard changes in working directory)

    Tal como afirma, *git checkout* sin un identificador de versión
    restaura los archivos al estado guardado en HEAD. El guión doble -- es
    necesario para separar los nombres de los archivos siendo recuperados
    del comando mismo: sin esos guiones, Git trataría de usar el nombre
    del archivo como identificador de la revisión a la cual se desea volver.

El hecho de que los archivos puedan recuperarse o revertirse uno por uno tiende
a cambiar el modo en que la gente organiza su trabajo. Si todo estuviese en un
solo gran archivo, entonces es dificil (si no imposible) deshacer los cambios a
la introducción sin también deshacer los cambios hechos a continuación a la
conclusión. Por otra parte, si la introducción y la conclusión estuviesen en
archivos separados, entonces sería más fácil moverse hacia atrás y hacia
adelante en el tiempo.

## Ignorando cosas

Vamos a ver qué hacer con los archivos del mismo directorio que no queremos
incluir en el sistema de control de versiones. Agregamos algunos archivos
vacíos: a.dat

``` console
$ mkdir results
$ touch a.dat b.dat c.dat results/a.out results/b.out
```

Y vemos qué dice Git:

``` console
$ git status
# On branch master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#    a.dat
#    b.dat
#    c.dat
#    results/
nothing added to commit but untracked files present (use "git add"
to track)
```

Colocar estos archivos bajo control de versiones sería un desperdicio de espacio
en disco. Peor aún, tenerlos listados nos distraería de los cambios que
realmente importan, de manera que debemos decirle a Git que los ignore, creando
un archivo en el directorio raiz del proyecto. Al archivo lo llamamos
*.gitignore*.

Dentro de *.gitignore* colocamos los patrones para ignorar archivos, en este
caso los archivos que terminen en *.dat* y los archivos que se encuentren en el
subdirectorio *results* (si cualquiera de estos archivos hubiese estado siendo
parte del control de versiones, Git continuará considerándolo a pesar de figurar
en *.gitignore*). Al listar el contenido de *.gitignore* deberíamos obtener
esto:

``` console
$ cat .gitignore
*.dat
results/
```

Si pedimos el status del proyecto, la salida se verá mucho más limpia
que antes:

``` console
$ git status
# On branch master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#    .gitignore
nothing added to commit but untracked files present (use "git add" to track)
```

La única cosa que Git advierte ahora es el archivo *.gitignore* recientemente
creado. Podríamos creer que no querríamos incorporarlo al control de versiones,
pero todos con quienes compartimos el repositorio probablemente querrían ignorar
las mismas cosas que estamos ignorando nosotros. Así que agregamos y comiteamos
este archivo (oculto, pues empieza con un punto):

``` console
$ git add .gitignore
$ git commit -m "Agregado del archivo de ignorancias"
$ git status
# On branch master
nothing to commit, working directory clean
```

Como un extra, al usar *.gitignore* evitamos agregar accidentalmente archivos
que no queremos al repositorio.

``` console
$ git add a.dat
The following paths are ignored by one of your .gitignore files:
a.dat
Use -f if you really want to add them.
fatal: no files added
```

Si queremos realmente pasar por alto los seteos de *.gitignore*, podemos usar
*git add -f* para forzar a Git a agregar algo. Siempre podemos ver la situación
de los archivos ignorados si quisiéramos:

``` console
$ git status --ignored

# On branch master
# Ignored files:
#  (use "git add -f <file>..." to include in what will be committed)
#
#        a.dat
#        b.dat
#        c.dat
#        results/

nothing to commit, working directory clean
```

## Claves

> Usar **git config** para configurar un usuario, dirección de email,
> editor y otras preferencias (todas estas cosas son válidas para una
> máquina)
>
> Con **git init** se inicializa un repositorio
>
> Con **git status** se muestra la situación de un repositorio
>
> Los archivos puedes almacenarse en el directorio de trabajo (que los
> usuarios ven), la *zona de preparación* o *staging area* (desde donde
> se realizará el próximo commit) y el repositorio local (donde las
> instantáneas son almacenadas permanentemente).
>
> Con **git add** se agregan archivos a la *zona de preparación*.
>
> Con **git commit** se crea una instantanea de la *zona de preparación*
> en el repositorio local.
>
> Siempre escribir un mensaje al comitear cambios (con **git commit -m
> \"mensaje\"**).
>
> Con **git diff** se muestran las diferencias entre versiones.
>
> Con **git checkout** se recuperan viejas versiones de un archivo.
>
> El archivo **.gitignore** indica a Git los archivos a ser ignorados
> por el sistema de control de versiones.

