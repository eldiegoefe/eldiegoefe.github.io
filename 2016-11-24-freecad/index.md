# FreeCAD


Para proyectar diseños en madera los carpinteros de YouTube suelen usar
SketchUp, que es un software de Google que sólo funciona en Windows y Mac.
Busqué algún programa que pueda usar con el mismo fin pero en Linux, y encontré
FreeCAD. Estoy siguiendo un buen tutorial en castellano en [el canal de Juan
Gonzalez Gomez](https://www.youtube.com/user/obijuancube), aca pueden ver el
primer video de la serie:

{{< youtube 2_DbFzFV9D4 >}}

Algunos apuntes iniciales:

-   Luego de iniciar un nuevo proyecto seleccionar el *espacio de
    trabajo* Part.
-   Hay distintos *estilos de navegación* que se seleccionan con el menú
    contextual que se activa en cualquier región del espacio de trabajo
    activo. Por ejemplo tiene un modo *Blender* (resultará familiar a
    los usuarios de ese software de edición de video).
-   Se puede visualizar el origen y ejes de coordenadas desde el menú
    *View / Toggle Axis Cross*.
-   La creación de cubos, esferas y otras formas primitivas se produce
    mediante los iconos amarillos.
-   Cada elemento tiene un par de pestañas asociadas: en *View* se
    pueden cambiar, por ejemplo, los colores y tipos de visualización, y
    en *Data* las dimensiones y posición de los objetos.
-   Se puede hacer una selección individual haciendo click sobre cada
    objeto en el dibujo o sobre el listado de objetos del proyecto. Se
    pueden seleccionar conjuntos de objetos con los modificadores CTRL y
    Shift.
-   La posición de los objetos (y otras propiedades) se puede modificar
    tipeando el nuevo número en el display correspondiente o sino
    activando el display y moviendo la rueda del mouse.
-   SPC: muestra u oculta (transparenta) el objeto activo.
-   En los primeros videos de la serie que recomiendo al principio se ve
    cómo construir formas complejas a partir de uniones o restas de
    formas primitivas.
-   También se pueden clonar formas usando una simetría polar (alrededor
    de un eje) u ortogonal (como un arreglo matricial en una dimensión,
    en dos o en tres).

No estoy seguro de que FreeCAD sea un buen sustituto para SketchUp, pero
igual aprender a usarlo es bastante entretenido.

## Un ejemplo sencillo

Les muestro una vista lateral superior del *cono de tránsito* propuesto
como tarea del video 15 ([usando
conos](https://www.youtube.com/watch?v=eqh_KMsePPU)):

![vista lateral superior](https://c2.staticflickr.com/6/5788/31240860785_a73f203cd1_o.png){.align-center
width="50.0%"}

La construcción se logra uniendo un cono con un rectángulo al que se le
aplica un redondeado en sus bordes. Esta unión representa la pieza
completamente rellena. Luego se duplica el cono y se ajustan sus
dimensiones para que atraviese toda la pieza por dentro, y al hacer el
recorte quede el cono ya no maciso sino con el agujero que lo atraviesa.
El proceso es muy rápido.

![vista lateral inferior](https://c2.staticflickr.com/6/5781/31240860835_d7c2729849_o.png){.align-center
width="50.0%"}

