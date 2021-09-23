# Comandante Emacs (dired-mode)


Estuve un rato largo (¡horas!) viendo cómo usar el modo \"dired\" que tiene
Emacs para el manejo de archivos, porque quiero usarlo al modo del viejo
Comandante Norton (y sus clones: Total Commander en Window\$, Krusader
especialmente para KDE, etc). Es decir: dos paneles que sirven de inicio y de
destino para poder copiar y mover archivos, crear directorios, navegarlos, etc.

{{< figure src="https://live.staticflickr.com/7526/15668751884_b2fa8f9d5b_c.jpg" title="Buffer mostrando un directorio con dired-mode" >}}

Lo primero que hice fue instalar un paquete que amplía las opciones
disponibles llamado dired+ (dired plus) y después instalé otra extensión
llamada dired-sort-menu. La información sobre la instalación de estos
paquetes da por supuesto que uno ya tiene experiencia en Emacs, y a
pesar de que yo lo uso hace casi un año y he instalado y desinstalado
muchas extensiones, estuve un rato para darme cuenta de algo que no
figura en [la página de
dired+](http://www.emacswiki.org/emacs/DiredPlus). En el archivo de
configuración de Emacs (init.el, custom.el o el que estemos utilizando)
es imprescindible agregar la orden siguiente:

``` cl
(require 'dired+)
```

Para correr el modo basta hacer **M-x dired** (yo creo que con esto se
carga ya con los agregados de dired+, que por ejemplo enriquece los
menúes de dired, así que viendo estos menúes uno puede darse cuenta si
está cargada la extensión o no). El buffer de dired que se abre muestra
los nombres de los archivos del directorio elegido (ver en la figura
siguiente), pero parece que por defecto se activa el ocultamiento de
toda otra información. Hay que ejecutar dired-hide-details-mode para que
se vea toda la info del archivo, incluyendo fecha, permisos, etc.

{{< figure src="https://farm8.staticflickr.com/7580/16290334112_66dd0af6b1_o.png" title="Buffer con dired+ suprimiendo detalles de los archivos" >}}

Por ahora no encuentro el modo de colorear distinto a las directorios y
a los archivos con distinta extensión (observación al 11/2020: en Doom
Emacs aparecen cosas con diversos colores, por ejemplo los permisos, las
fechas, los tamaños de los archivos). Intenté con el paquete
dired-rainbow y pude colorear distinto los archivos con diferentes
extensiones, pero no se cómo hacer con los directorios (porque no tienen
extensión), así que lo desinstalé. Pero copio debajo el código de prueba
que funcionó, para no perderlo:

``` cl
(require 'dired-rainbow)

(defconst my-dired-media-files-extensions
  '("mp3" "mp4" "MP3" "MP4" "avi" "mpg" "flv" "ogg")
  "Media files.")

(dired-rainbow-define html "#4e9a06" ("htm" "html" "xhtml"))
(dired-rainbow-define media "#ce5c00" my-dired-media-files-extensions)
```

Puse [una pregunta en Emacs
Exchange](http://emacs.stackexchange.com/questions/5765/how-to-view-files-ordered-by-extension-in-dired)
para ver el modo de ordenar los archivos por extensión (y poniendo
primero los directorios). Me respondieron al toque, y la solución estaba
en instalar un paquete llamado dired-sort-menu.el (o
dired-sort-menu+.el). Luego hay que agregar también en la configuración
el \"require\" correspondiente:

``` cl
(require 'dired-sort-menu+)
```

Al manipular archivos es muy práctico tener dos buffers abiertos como en
la figura siguiente, de modo que al copiar o mover se usan ambos
directorios como origen y destino, sin que haga falta teclear nada. En
este caso el ordenamiento es por nombre, así que se ven mezclados los
archivos (visibles y ocultos) con los directorios.

{{< figure src="https://farm8.staticflickr.com/7527/16105034929_742a1aeac2_b.jpg" title="Dos buffers coloridos con dired+." >}}

Edición del nombre de archivos y directorios

El buffer se puede volver editable para habilitar el cambio de nombre de
archivos y directorios, del mismo modo en que se edita un buffer normal
de texto. La función que vuelve editable el buffer es
dired-toggle-read-only que por defecto se ejecuta con C-x C-q y en Doom
Emacs directamente con \"i\" (insert mode). Al correr la función prestar
atención al minibuffer porque indica la manera de salir de este modo de
edición, confirmando los cambios (vanilla: C-c C-c; Doom: Z Z) o
cancelándolos (vanilla: C-c C-k; Doom: Z Q).

Las funciones más comunes y sus atajos de teclado (son case-sensitive)
están en la tabla siguiente, a modo de ejemplo, pero hay muchas más
opciones en los menúes de dired+, que son varios: Dir, Mark, Regexp,
Multiple, Single. En los menúes figuran los atajos, así que mirándolos
es una buena forma de aprender.

  ---------------------- -----------
  **Función**            **Atajo**

  Marcar archivo         m

  Desmarcar archivo      u

  Marcar por extensión   \*.

  Marcar directorios     \*/

  Desmarcar todos        U

  Invertir selección     t

  Dividir en 2 paneles   C-w v

  Ir al otro panel       C-w w

  Copiar                 C

  Mover/renombrar        R

  Full/simple view       ( ó S-8

  Entrar directorio      ENTER

  Directorio anterior    \-

  Crear directorio       \+

  Marcar para borrar     d

  Run acciones marcadas  x

  Buffer editable        C-x C-q

  Idem con Doom          i
  ---------------------- -----------

