---
title: Crear colecciones y albumes en digiKam
date: 2015-01-15T10:00:00
categories: [blog]
tags: [fotografia, digikam, tutorial]
author: Diego Efe
featuredImagePreview: https://farm9.staticflickr.com/8607/16286745132_f1665fa0b7_h.jpg
toc: false
---

Crear albumes en digiKam tiene un inconveniente que un usuario que intenta
emplearlo descubre rápidamente. Es un detalle que no está bien documentado en
los tutoriales que encontré en la web. El problema es el siguiente: sólo van a
poder crear álbumes dentro del único álbum existente, el cual aparece tras el
procedimiento de configuración básica, cuando digiKam se ejecuta por primera
vez. Probablemente este álbum se llame \"/home/nombreusuario/Imágenes\", como en
la figura siguiente.

**Imagen 1**: al iniciar el uso de digiKam hay probablemente una sola colección
(y un mensaje de bienvenida muy informativo pero medio fiero, con fondo azul).

{{< figure src="https://farm9.staticflickr.com/8569/15667544713_c7b33ac69f_h.jpg" title="Imagen 1" width=75% >}}

Para crear un álbum las instrucciones son sencillas: hay que ir al menú
*Album* y elegir *Nuevo (Ctrl+N)\...*, o también click con el botón
derecho sobre el álbum dentro del cual queremos crearlo. **El problema
radica en que sólo nos está permitido crear nuevos álbumes dentro del
único ya existente**. Si queremos crear uno que descienda directamente
de \"Álbumes\", con la misma jerarquía que el que aparece por defecto
(\"/home/nombreusuario/Imágenes\"), vamos a descubrir que la mencionada
opción (*Nuevo*) en el menú se puede ver pero aparece en gris, no se
puede elegir, tampoco funciona el atajo de teclado (Ctrl+N) y si
tratamos con el ratón vemos que la opción tampoco está disponible en el
menú contextual (sólo aparece una opción \--Álbum\--que en realidad es
el título de este menú contextual):

**Imagen 2**: Un detalle ampliado de la ventana anterior. No se encuentra la
opción, en el menú contextual, de agregar un nuevo álbum. Al hacer click derecho
sobre Álbumes aparece el menú contextual de la figura, que sólo posee un título
(Álbumes). ¡Qué difícil es explicar las cosas si todo se llama igual!

{{< figure src="https://farm9.staticflickr.com/8683/16101480319_efb201162b_o.png" title="Imagen 2" >}}

En digiKam hay una diferencia de nomenclatura entre **Colecciones** y
**Álbumes**, que no se explícita (a la colección a veces la nombran como
\"álbum raíz\" o \"root album\", y en las opciones aparece también
traducido al castellano como **Temas**), y que ahora les comento. Las
colecciones son los recipientes donde se almacenan los álbumes; se
corresponden físicamente con los directorios principales dentro de los
cuales se ubicarán las fotos en subálbumes. El programa no nos deja
crear álbumes dependientes de \"Albumes\" porque antes debemos crear las
\"Colecciones\". Ya tenemos creada una colección sin habernos dado
cuenta y es la que corresponde a /home/nombreusuario/Imágenes, pero si
tenemos fotos con las cuales queremos trabajar, y no deseamos moverlas
físicamente a este directorio (copiarlas o moverlas dentro de este
directorio, da igual), entonces debemos crear una colección por cada
carpeta donde tengamos nuestros archivos de imágenes (por ejemplo en el
directorio /home/nombreusuario/fotografias o en un subdirectorio de un
disco externo). Esto no es necesario cuando las fotos se encuentran en
subdirectorios dentro de la colección existente. Vale aclarar que
digiKam refleja el contenido de las colecciones y subálbumes como un
navegador de archivos, y actualiza el contenido de los mismos
inmediatamente si con un programa externo copiamos o movemos fotos desde
y hacia los directorios de la colección.

Para crear las colecciones los pasos son muy sencillos. Hay que
dirigirse al menú \"Settings/Configure digiKam\...\" y allí, en el panel
de la izquierda, seleccionar el segundo icono desde arriba: \"Temas\"
(en inglés es \"Collections\").

**Imagen 3: Una sola colección existe inicialmente, la que se creó
(inadvertidamente) cuando atravesamos la configuración inicial de digiKam,
durante su primera corrida.**

{{< figure src="https://farm8.staticflickr.com/7469/15664846264_ac27f442ea_b.jpg" title="Imagen 3" >}}

Obviamente hay que presionar el botón \"Añadir colección\". Por
colecciones locales se refiere a aquellas que estén dentro del
directorio personal del usuario (por ejemplo \~/fotografias). Las
colecciones en medios extraibles serán para elegir colecciones en discos
externos, pendrives, DVDs, etc. Las colecciones en redes compartidas
sólo tendrán sentido en computadoras que se encuentren conectadas a una
red local. Aquí les muestro cómo queda este menú de configuración una
vez creada la colección /home/fotografo/fotografias (que se sintetiza
como \~/fotografias):

**Imagen 4: Configuración luego de haber añadido una colección (o \"álbum
raíz\").**

{{< figure src="https://farm9.staticflickr.com/8595/16099911410_27dcbd2dea_b.jpg" title="Imagen 4" >}}

Volvemos a la pantalla principal de digiKam y vemos que apareció la
nueva colección (fotografias) y al hacer click derecho con el mouse
vemos el menú contextual, ahora completo con la opción de crear nuevos
álbumes (dependientes de esta colección).

**Imagen 5: Colección agregada y menú contextual.**

{{< figure src="https://farm8.staticflickr.com/7568/16101500609_2a2ede17e6_o.png" title="Imagen 5" >}}

A continuación les muestro otra pantalla con algunos álbumes de muestra.

**Imagen 6: Álbumes y fotografías de ejemplo. Si abren el administrador de
archivos (que depende de la distribución de linux y el escritorio que
usen, en KDE suele ser dolphin) verán una estructura idéntica de
directorios: cada álbum es una carpeta
\"física\".**

{{< figure src="https://farm9.staticflickr.com/8607/16286745132_f1665fa0b7_h.jpg" title="Imagen 6" >}}

## Cambio de idioma de digiKam

*Un último tip*: se pueden elegir los idiomas en que se presenta digiKam
en el menú de ayuda (Ayuda/Cambiar el idioma de la aplicación\...). Es
una opción útil, por ejemplo, para seguir un tutorial de la web que no
está en español.
