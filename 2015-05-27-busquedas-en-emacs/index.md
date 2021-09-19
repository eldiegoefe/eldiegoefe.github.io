# Búsquedas con isearch en Emacs


Es una tarea habitual al editar texto el buscar caracteres o palabras. Una de
las opciones que ofrece Emacs es la función de búsqueda incremental, que tiene
varias formas de inicio.
  
 | Comando                         | Por  defecto | Ergoemacs | Descripción                           |
 |---------------------------------|--------------|-----------|---------------------------------------|
 | isearch-forward                 | C-s          | C-f       | solicita los caracteres a buscar      |
 | isearch-forward-symbol-at-point | M-s .        | F8 .      | busca el símbolo bajo el cursor       |
 | isearch-forward-word            | M-s w        | F8 w      | busca palabras                        |
 | isearch-forward-symbol          | M-s \_       | F8 \_     | busca símbolos (símbolos según Emacs) |

Al ejecutar uno de estos comandos se entra dentro de un modo en el cual
se puede repetir la misma búsqueda o modificarla (en el minibuffer
aparece información relativa a este modo, por ejemplo tras ejecutar
*isearch-forward* aparece *I-search:* para que el usuario ingrese las
letras que desea buscar).

Se dispone de un gran número de opciones y atajos de teclado, válidos
mientras se mantiene este modo de búsqueda. Entre los más habituales:

-   RET (Enter): sale del modo de búsqueda, el cursor queda en la última
    locación encontrada
-   C-g: interrumpe el modo, el cursor vuelve a la posición inicial
-   C-f: repite la misma búsqueda hacia adelante
-   C-r: repite la misma búsqueda hacia atrás
-   M-s c: conmuta la sensibilidad a mayúsculas
-   M-s w: conmuta al modo de búsqueda de palabra completa

Hay muchas más opciones que se pueden consultar ejecutando *M-x
describe-function isearch-forward* o directamente *C-h f
isearch-forward*.

![](https://farm8.staticflickr.com/7748/18166889492_5daac19817_b.jpg)

