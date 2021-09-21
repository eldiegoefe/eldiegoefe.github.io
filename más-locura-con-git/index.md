# Más locura con Git


Hay un lindo tutorial interactivo para aprender a usar Git [este
Carpentry](https://github.com/swcarpentry/site), recomendado desde el GitHub de
[Software Carpentry](https://github.com/swcarpentry/site). Me gustó también el
video [Git for ages 4 and up](https://www.youtube.com/watch?v=1ffBJ4sVUb4) (no
entendí nada la presentación del expositor, pero el resto sí).

Al sitio interactivo llegué desde
[Astropy](http://astropy.readthedocs.org/en/latest/), en particular de la página
[How to make a code
contribution](http://astropy.readthedocs.org/en/latest/development/workflow/development_workflow.html),
que parece que vale la pena leer, porque explica el workflow que utilizan, cosa
que no había encontrado hasta ahora (que te expliquen cómo es la secuencia de
acciones de un trabajo, su lógica, los trucos, puede ahorrar muchos problemas
asociados con la inexperiencia).

El tutorial interactivo va mostrando *hints*, de los cuales quiero
acordame:

> -   **add all**: You can also type *git add -A .* where the dot stands
>     for the current directory, so everything in and beneath it is
>     added. The *-A* ensures even file deletions are included.
> -   **git reset**: You can use *git reset \<filename>* to remove a
>     file or files from the staging area.
> -   **More useful logs**: Use git log \--summary to see more
>     information for each commit. You can see where new files were
>     added for the first time or where files were deleted. It\'s a good
>     overview of what\'s going on in the project.
> -   **Branching**. Branches are what naturally happens when you want
>     to work on multiple features at the same time. You wouldn\'t want
>     to end up with a master branch which has Feature A half done and
>     Feature B half done. Rather you\'d separate the code base into two
>     \"snapshots\" (branches) and work on and commit to them
>     separately. As soon as one was ready, you might merge this branch
>     back into the master branch and push it to the remote server.

Tengo dudas con esto: si luego de hacer un pull desde un repositorio
remoto, hay cambios respecto de lo que tenía en el repositorio local,
¿qué me dice Git si hago *git status*?

Más material:

> -   [Version control for fun and
>     profit](http://nbviewer.ipython.org/github/fperez/reprosw/blob/master/Version%20Control.ipynb)
> -   [Revision control
>     software](http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-7-Revision-Control-Software.ipynb)
> -   [Git for Scientists](http://nyuccl.org/pages/GitTutorial/)

Cosas interesantes del artículo de Fernando Perez:

-   Se pueden generar alias para ejecutar comandos largos con nombres
    cortos. Por ejemplo *git config \--global alias.slog \"log
    \--oneline \--topo-order \--graph\"* hace que luego funcione *git
    slog*.

Hay un [video de Jessica
Kerr](https://www.youtube.com/watch?v=Dv8I_kfrFWw) en el cual hace
algunos buenos comentarios:

-   Recomienda tener un gestor gráfico para ver el arbol de un
    repositorio, y usarlo antes de comitear para anticipar cómo debería
    verse el arbol, y entonces luego de comitear verificar en el grico
    que lo realizado coincide con lo que queríamos hacer. Quizás esto lo
    pueda hacer
-   origin/master es un puntero (como HEAD) que apunta hacia donde
    estaba el HEAD en origin la última vez que lo visitamos.
-   No conviene usar *pull* porque es un *fetch* + *merge*. Hacerlo esto
    último por separado brinda mayor control, permite ver cuál es el
    merge que hacemos.
-   El *push* hace lo mismo que el *pull* pero en dirección opuesta
    (desde nuestro repo hacia el remoto). Como tiene que hacer un merge,
    sólo lo permitirá si puede hacer un *fast-forward* en el remoto,
    esto es decir: si no hubo otro usuario que hiciera cambios en el
    remoto desde la última vez que sincronizamos nuestro repo local con
    el remoto. Por eso, si hubiese habido algún cambio en el remoto,
    deberá hacerse un pull (o un fetch+merge) antes del push.

