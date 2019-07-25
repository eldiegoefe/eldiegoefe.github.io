Grabacion de screencasts para tutoriales de YouTube
###################################################

:date: 2014-09-23 10:00
:category: tecnicismos
:tags: youtube, video, tutorial
:author: El Diego Efe
:excerpt: Grabacion de screencasts para tutoriales de YouTube
:disqus_identifier: grabacion de screencasts

**Actualización (Feb-2017)**: es muy facil usar el programa `OBS Studio`_ para
grabar en la computadora tanto la pantalla como la webcam, micrófono, etc.
Funciona en Linux, Window$ y Mac.

.. _OBS Studio: https://obsproject.com

-----

Empecé a grabar tutoriales para usar IPython Notebook. Traté de
hacerlo con la aplicación recordMyDesktop, pero el modo de seleccionar
la parte de la pantalla a grabar resulta muy imprecisa, es
practicamente imposible determinar la región con precisión.

Luego encontré este buen tutorial: `Creating Screencasts in
Linux`_. Ahí hay dos datos importantes:

.. _`Creating Screencasts in Linux`: http://nienhueser.de/blog/?p=469

1. Conviene grabar una región cuyo razón de aspecto sea 16:9 (para que
   salga bien en un monitor wide). De la tabla de posibles tamaños
   aceptados por YouTube prefiero la de 1280x720.

2. Se pueden usar las opciones de ventana de KDE (a las cuales se
   accede con click derecho sobre el título de la ventana / Más
   acciones / Preferencias especiales de la ventana) para darle al
   navegador un tamaño de ventana (y un offset desde la esquina
   superior izquierda) igual al tamaño deseado para la grabación. De
   este modo se fuerza la ventana a un tamaño tal que ocupe todo el
   area de grabación, de modo de evitar incluir en el video cosas
   innecesarias.

Para la grabación empecé a usar la aplicación ffmpeg, en linea de
comando, tal como lo sugiere la página de Dennis Nienhüser que cité
más arriba.

Hice cambios en las opciones citadas por Dennis, para grabar también
el sonido agregué:

 -f alsa

 -ac 2: se usan 2 "audiochannels" (ac)

 -ab 128k: bitrate

 -acodec pcm_s16le: un codec de grabación de audio

 -i hw:1 - para seleccionar "input device"

Para saber cuál es la tarjeta de sonido se utiliza el comando *arecord
-l*, y dado que quiero grabar con la webcam USB uso hw:1 (porque es la
"card 1"). El resultado en mi PC es el siguiente:

.. code-block:: console

  **** List of CAPTURE Hardware Devices ****
  card 0: PCH [HDA Intel PCH], device 0: VT2020 Analog [VT2020 Analog]
    Subdevices: 1/1
    Subdevice #0: subdevice #0
  card 0: PCH [HDA Intel PCH], device 2: VT2020 Alt Analog [VT2020 Alt Analog]
    Subdevices: 1/1
    Subdevice #0: subdevice #0
  card 1: U0x46d0x825 [USB Device 0x46d:0x825], device 0: USB Audio [USB Audio]
    Subdevices: 1/1
    Subdevice #0: subdevice #0

Usé el programa `alsamixer`_ (ejecutado desde la línea de comando y
que funciona en modo texto) para seleccionar la placa de sonido,
aunque al final no se si tiene algo que ver el haber logrado grabar
video y sonido con lo hecho desde esta aplicación.

.. _`alsamixer`: https://trac.ffmpeg.org/wiki/Capture/ALSA

La orden que finalmente usé (va todo junto, es una sola linea):

.. code-block:: console

  ffmpeg -f alsa -ac 2 -ab 128k -acodec pcm_s16le -i hw:1 -f x11grab
  -show_region 1 -y -r 30 -s 1280x720 -i :0.0+0,0 -vcodec libx264
  screencast.avi

Tener cuidado con el nombre del archivo (en este ejemplo es
screencast.avi), porque sino se va cambiando entre grabaciones
sucesivas se va sobreescribiendo.

En la notebook con Linux Mint 17 tuve que instalar ffmpeg siguiendo
las instrucciones de `esta página`_.

.. _`esta página`:
   http://ask.fclose.com/1036/how-to-install-ffmpeg-on-linux-mint-17-qiana
