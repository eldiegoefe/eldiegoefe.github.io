---
title: Cómo simplificar la clasificación de fotos
date: 2015-01-15T10:00:00
categories: [blog]
tags: [fotografia, digikam, tutorial]
author: Diego Efe
draft: true
---

En un post anterior comentaba sobre la utilidad de clasificar fotos usando un
sistema de etiquetas, ordenadas en una estructura jerárquica. Por ejemplo:
*/lugares/paises/Argentina*, */lugares/paises/Uruguay*, */retratos/ancianos*,
*/retratos/actrices-porno*, */retratos/autoretratos/de-día*, etc). Así, para
etiquetar se hace un click en la categoría deseada (por ejemplo en \"de-día\"),
y todas las demás que la preceden (\"retratos\" y \"autorretratos\") también
servirán para identificar a la misma foto, para poder encontrarla cuando realice
una búsqueda con cualquiera de esos 3 criterios.

Ahora bien, hay al menos un detalle para simplificar la estructura que
encontré tras algunas pruebas. Había armado un esquema básico con el que
clasifiqué un conjunto de 4500 fotos de un viaje que duró 3 meses.
Llegué a unas 15 o 20 categorías básicas (y muchas subcategorías en
algunas de ellas). No se si elegí muy bien las etiquetas y las
subdivisiones, pero llegué a eso (algunas pueden verse en la figura
siguiente).

Si bien partí de un esquema mucho menor, encontraba fotos que no
entraban en las categorías existentes y requerían una clasificación
nueva, así que terminé con un árbol bastante frondoso en poco tiempo. La
cuestión es que hubo un momento en que me di cuenta de que tenía una
misma etiqueta alojada en distintas ramas: \"lugareshistóricos\",
\"museosherramientas\", \"fotografíaherramientas\" así que separé las
cosas y ahora cuando clasifico tengo que recordar que debo tildar las
dos palabras clave por separado (en vez de un solo click cuando me
tocaba ordenar la foto de una lente y elegía únicamente
\"fotografía\|herramientas\".

Con esta mecánica se evita un poco la repetición de algunas palabras
clave, a costa de ampliar las categorías básicas.

DigiKam provee un \"Gestor de Etiquetas\" para efectuar estas
manipulaciones. Tiene la ventaja de ser \"drag & drop\", de modo que uno
hace click sobre la etiqueta que quiere mover y la lleva al destino,
donde debe soltar el botón del ratón (si se mantiene apretado Shift al
soltar, la acción es mover la etiqueta, si uno no apreta esa tecla el
sistema pregunta si copiar, mover o cancelar). Al hacer esto hay que
tener cuidado con el siguiente inconveniente: una foto clasificada con
\"lugares\|históricos\" pueda perder la etiqueta \"lugares\" al mover
directamente la palabra \"históricos\" desde la categoría \"lugares\"
hacia \"adjetivos\". **Antes de hacer la modificación, es preciso
asegurarse de que todas las fotos que llevan la categoría
\"lugares\|históricos\" tengan también asignada la categoría \"lugares\"
por sí sola**. Esto es muy fácil de hacer con el panel de selección de
imágenes por categoría.

Si se les ocurren otros trucos para simplificar esta labor, les
agradeceré que me los comenten. ¡Saludos!

estrellas: todas las que no vale la pena volver a ver \--yo

:   etiqueto con 1 estrella las que voy a borrar, y luego de hacerlo
    reclasifico las que tienen 2 estrellas con mayor resolución, es
    decir que las peores de 2 estrellas pasan a tener una sola).
