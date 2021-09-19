# Escritorio cómodo y atajos de teclado


Me cuesta encontrar un modo cómodo de trabajar con Emacs y otros programas en
KDE. Como creo que voy encontrando cosas que me resultan funcionales, las resumo
aca.

Sirve trabajar con 4 workspaces (areas de trabajo) en KDE. En el espacio
1 tengo el navegador, en el 2 tengo Emacs y en el 4 tengo un terminal.
Cambio de espacio con C-7 (espacio 1), C-8 (espacio 2), C-9 (espacio 3)
y C-0 (espacio 4). Para mover la ventana de un programa a un espacio de
trabajo lo hago con M-7, M-8, M-9 y M-0 (los fans de emacs saben que M
es Meta, y que eso significa en un teclado convencional la tecla Alt).

Para elegir estos atajos de teclado hay que ir a Preferencias del
Sistema / Accesos rápidos y gestos / Accesos rápidos de teclado globales
y elegir en \"Componente de KDE\" la opción \"KWIN\", allí es fácil
darse cuenta cómo continuar.

De paso, hay una opción en KDE para que cada espacio de trabajo sea
independiente de los otros, así que pueden tener widgets y fondos de
pantalla diferentes, lo que ayuda a diferenciarlos.

## Emacs

En Emacs uso estas cosas que están buenísimas:

Intercambié la funcionalidad de las letras U y X (estoy en Dvorak) con
estas lineas en el archivo de configuración de emacs:

``` cl
(keyboard-translate ?\C-x ?\C-u)
(keyboard-translate ?\C-u ?\C-x)
```

Cambié el keybinding para ir a la linea anterior a C-t, de manera que
queda junto a C-n, que es para ir a la linea siguiente:

``` cl
(global-set-key (kbd "C-t") 'previous-line)
```

Uso C-a y C-e para ir al principio y final de cada linea.

Uso C-l para que se centre la ventana alrededor del cursor (muy util
cuando estamos cerca del borde inferior de la pantalla).

Borro palabras hacia atrás con M-del. Tengo que revisar por qué no anda
C-x del (que es backward-kill-sentence). Da el mensaje \"C-x deletechar
is undefined\". Se ve que es un problema con la tecla *del*.

Uso el acorde **jj** que ejecuta *ace-jump-word-mode* que permite
navegar hacia la letra inicial de una palabra de un modo muy veloz (y
entretenido). Tendría que acostumbrarme a usar también estos:

> -   jk: Jump to a character(ace-jump-char-mode)
> -   jl: Jump to the beginning of a line(ace-jump-line-mode)
> -   JJ: Jump back to previous
>     buffer(prelude-switch-to-previous-buffer)
> -   xx: Executed extended command(execute-extended-command)
> -   yy: Browse the kill ring(browse-kill-ring)

Para navegar entre los cambios uso el acorde **uu** que muestra el
historial como un arbol (*undo-tree-visualize*).

Para saltar de una ventana a otra uso el habitual C-x o (en realidad
hago C-u o gracias al truco del intercambio entre la x y la u que
mencioné antes), pero ejecuta *ace-window* que funciona semejante a los
*ace-jumps*. Lo mismo se logra con C-TAB.

Para intercambiar ventanas activas sirve C-c s. Es una función de
Prelude y sólo funciona si hay 2 ventanas en pantalla.

Para aumentar la indentación de una región o bloque uso C-x TAB.

Para borrar un rectángulo, por ejemplo la indentación de un bloque,
pongo la marca y el punto en los extremos de la región y luego C-x r k.

Uso **lgrep** para buscar archivos por contenido. Es interactivo, va
preguntando la fórmula de búsqueda, el tipo de archivo y el directorio.
Projectile tiene también un buscador de contenido dentro de los archivos
de un proyecto, lo tengo que probar: C-c p g

Recién instalo el paquete workgroups2 que gestiona las sesiones,
incluyendo la posición de las ventanas. Lo descubrí gracias a [una
pregunta que hice en
emacs.stackexchange](http://emacs.stackexchange.com/questions/822/how-to-setup-default-windows-at-startup).

Para ejecutar algún cambio de configuración (en .emacs o en custom.el)
puedo marcar la región que contiene el cambio y hacer M-x eval-region.

Prelude tiene C-x m para iniciar *eshell*. Sin embargo no puedo ejecutar
el environment para el blog (. bin/activate desde el directorio ENV).

Finalmente, para repetir el último comando se usa C-x z (y luego si
desea repetirse nuevamente, basta con apretar la z sola).

