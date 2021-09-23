# Python en Emacs y otros atajos


## Spacemacs

1.  Anaconda-mode: Emacs tiene muchas herramientas para facilitar la
    programación en Python. En Spacemacs se puede activar
    [anaconda-mode](https://github.com/proofit404/anaconda-mode), que habilita
    una serie de paquetes útiles. Por ejemplo \"eldoc\" que ofrece información
    en el modeline sobre la función que se está tipeando (muestra los nombres de
    sus argumentos). Cosas de Anaconda para usar:

    -   anaconda-mode-complete (C-M-i)
    -   anaconda-mode-find-definitions (SPC m g g): busca el origen del
        símbolo bajo el punto. Por ejemplo: si se trata de una función,
        abre el archivo donde está definida y ubica el punto sobre el
        encabezado de la misma.
    -   anaconda-mode-find-assignments
    -   anaconda-mode-find-references
    -   anaconda-mode-go-back
    -   anaconda-mode-show-doc

2.  Entornos virtuales: se puede activar un entorno virtual donde correr
    el programa que se está desarrollando con SPC m V (pyvenv-workon,
    pero en este caso no aparecen correctamente todas las opciones, al
    menos no veo los entornos que instalé con pyenv), o también con SPC
    m v s (pyenv-mode-set, en este caso sí se ven los entornos de
    pyenv).

3.  Shell con entorno virtual: para acceder a un shell con el mismo
    entorno virtual que se activó (en el punto anterior) hay que hacer
    SPC a s m (shell-pop-multiterm).

4.  Comentarios: para comentar el bloque de lineas seleccionadas se
    utiliza SPC c l (evilnc-comment-or-uncomment-lines). También se
    puede probar con SPC ; (evilnc-comment-operator).

5.  Para ejecutar programas que contienen el llamado a la función
    principal con un bloque del siguiente modo:

    ``` python
    if __name__ == '__main__':
    ```

    hay que pulsar C-u C-c C-c (y en Spacemacs: SPC u C-c C-c).
    Previamente hay que haber elegido el entorno virtual correcto (ver
    el punto 2). De este modo funcionan los programas incluso si tienen
    panel construido con PyQt. Más info en la pregunta que hice yo
    mismo: [How to execute a python program (with a GUI) from
    Emacs?](http://emacs.stackexchange.com/questions/13357/how-to-execute-a-python-program-with-a-gui-from-emacs).

## Yasnippets

1.  SPC i s (spacemacs/helm-yas). Si no están aún cargados, carga los
    snippets y ofrece un menú tipo helm para seleccionarlos. Luego
    quedan habilitados para usar el trigger (la abreviatura) seguido de
    TAB.

{{< figure src="https://c1.staticflickr.com/1/657/21855757933_5ff671a447_b.jpg" title="Yasnippets con Helm" >}}

## Tabulación

1.  C-x TAB (indent-rigidly). Selecciono las lineas, uso C-x TAB y luego
    las flechas hacia los lados para aumentar o disminuir la indentación
    manteniendo la disposición actual.
2.  También se puede tabular para respetar las necesidades del lenguaje,
    seleccionando una región y pulsando C-M-\\ (indent-region). Aún
    cuando no haya ninguna indentación previa en esta región, cada linea
    se acomoda al lugar que debe ir. Igual hay que chequear porque el
    comando no puede adivinar, y hay veces que un mismo bloque puede ir
    con distintas indentaciones correctas.

## Spacemacs

1.  Para insertar texto desde el modo \"normal\" (o \"comando\") se usa
    la letra p o P (la inserción es antes o después de la ubicación
    actual del cursor). Para pegar desde el modo \"insert\": C-y.
2.  Se comentan (y des-comentan) lineas seleccionándolas y presionando
    SPC c l (comment-or-uncomment-line).
3.  Se borra la ventana actual con SPC w d. Obviamente sólo es posible
    cuando hay más de una ventana abierta (recordar que las ventanas en
    Emacs son las subdivisiones de la pantalla ocupadas por un buffer).
4.  Para navegar directorios se usan las combinaciones C-j y C-l para
    moverse desde un directorio hacia otro que esté un nivel por encima
    o un nivel por debajo.

