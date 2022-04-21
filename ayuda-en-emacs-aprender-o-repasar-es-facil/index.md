# Ayuda en Emacs - Aprender o Repasar es Facil


Indagar sobre las múltiples funciones de Emacs es una tarea
inevitable. Ya sea para explorar y descubrir comandos útiles, o tras
un tiempo alejados del editor durante el que nuestros músculos olvidan
hasta los atajos de teclado más cotidianos.

Por suerte Emacs cuenta con mucha documentación incorporada y si
aprendemos a preguntarle, nos responderá todas nuestras dudas sin
necesidad de salir a buscar respuestas en la web. 

Un problema de la información disponible online es que está centrada
por lo general en los atajos de teclado que vienen por defecto en
Emacs (o en los paquetes de terceros que instalemos), y entonces se
vuelven inaplicables las sentencias del tipo "*para salir de Emacs se
usa C-x C-c*". Yo promuevo el uso del nombre de las funciones para dar
ayuda, pero en cualquier caso, es mejor preguntarle a nuestra versión
local de Emacs todo lo que necesitemos saber, puesto que conoce
nuestros atajos de teclado al dedillo.

A continuación se listan algunas opciones para obtener ayuda.

## Info

Contamos con un conjunto de manuales muy detallados escritos en
TeXinfo (el formato de documentación oficial de GNU, que usa un mismo
archivo fuente para producir distintos formatos de salida como HTML,
Info, PDF, XML, etc.).

Mediante la función **info** accedemos a un índice con todos
los manuales *TeXinfo* instalados en nuestro sistema, incluido el
propio manual de Emacs pero también los de muchos paquetes
extras. Están construidos como *hipertexto*, navegable con las teclas
citadas debajo.

| Atajo   | Función                                  | Descripción                                          |
|---------|------------------------------------------|------------------------------------------------------|
| C-h i   | info                                     | Abre el manual info                                  |
| C-h 4 i | info-other-window                        | Idem, pero en otra ventana                           |
| [ and ] | Info-forward-node / Info-backward-node   | Ir al nodo siguiente / previo                        |
| l and r | Info-history-back / Info-history-forward | Navegar historial hacia atrás o adelante             |
| n and p | Info-next / Info-prev                    | Ir al nodo siguiente / previo (misma jerarquía)      |
| u       | Info-up                                  | Sube un nivel a un nodo superior                     |
| SPC     | Info-scroll-up                           | Scroll de una pantalla                               |
| TAB     | Info-next-reference                      | Cicla entre enlaces (hiperlinks) de la página        |
| RET     | Info-follow-nearest-node                 | Abre el enlace activo                                |
| m       | Info-menu                                | Pregunta por un item del menú (si hay uno) y lo abre |
| q       | quit-window                              | Cierra la ventana con el navegador de info           |

Info admite el uso de bookmarks (más sobre esto en otro posteo...). 

## Apropos

Es un comando que responde preguntas como "¿cuáles son los comandos
para trabajar con archivos?". La manera de hacerlo es usar un patrón
de búsqueda que puede ser una palabra, una lista de palabras o una
expresión regular. Es útil cuando no estamos seguros de lo que estamos
buscando. Permite buscar variables y comandos, y tiene soporte para
realizar las búsquedas con expresiones regulares.

| Atajo | Función               | Descripción                                                          |
|-------|-----------------------|----------------------------------------------------------------------|
| C-h a | apropos-command       | Muestra todos los comandos que coinciden con el criterio de búsqueda |
|       | apropos               | Muestra todo: funciones y variables                                  |

Por ejemplo, nos sirve para buscar funciones relacionadas con archivos
(buscaríamos: *file*) o rectángulos (*rectangle*). El resultado se
muestra en un buffer: las funciones que incluyen *file* o *rectangle*
en el nombre, su atajo de teclado y una breve descripción. Se puede
navegar hasta el nombre de los comandos o variables listados y con RET
abrir un nuevo buffer con más información.

Cuando se especifica más de una palabra como patrón de búsqueda, para
que haya coincidencia debe haber dos o más de esas palabras en el
nombre. Por ejemplo si buscamos sobre operaciones sobre copiar o
cortar oraciones podríamos buscar así: C-h a sentence kill yank insert.

Para mayor flexibilidad se pueden usar expresiones regulares. En
general, son expresiones de búsqueda que contienen los siguientes
caracteres: ^$*+?.\[. Funciones que terminen con "guión y región":
*-region$*, o con "guión y rectángulo": *-rectangle$*. 

Hay varias funciones más en la familia de *apropos*. Las podemos
buscar con *C-h a apropos*.

## Describe

Disponemos de ayuda para todas las funciones, a la cual accedemos
mediante el nombre de la función o con su atajo de teclado. También
tenemos una descripción de los modos activos en el buffer, con el que
podemos ver un listado de las funciones disponibles y sus atajos de
teclado. Finalmente, si conocemos un prefijo está disponible una ayuda
que indica todas las funciones que comparten ese inicio de atajo de
teclado.

| Atajo       | Función              | Descripción                                                                                                      |
|-------------|----------------------|------------------------------------------------------------------------------------------------------------------|
| C-h f       | describe-function    | Muestra documentación de la función en un nuevo buffer, a partir del nombre de la función                        |
| C-h k       | describe-key         | Idem anterior, pero a partir del atajo de teclado                                                                |
| C-h c       | describe-key-briefly | Muestra una linea con el nombre de la función asociada al atajo, en el minibuffer                                |
| C-h m       | describe-mode        | Muestra un buffer con la información del modo mayor y sus atajos, junto con una descripción de los modos menores |
| C-h b       | describe-bindings    | Muestra un buffer con una lista de todas los atajos y sus definiciones                                           |
| Prefijo C-h |                      | Muestra un buffer con una lista de todas las posibles funciones que se pueden ejecutar completando el prefijo    |







