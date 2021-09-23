# Instalacion de Linux


No es difícil encontrar la información para la instalación de Linux, pero hay distintas maneras y quiero dejar registrada la forma en que lo estoy haciendo actualmente. Los pasos que sigo son:

1.  Bajar el ISO (el archivo imagen) de la distribución que quiero
    instalar, en este caso es Linux Mint 17.
2.  Formatear en FAT32 el pendrive mediante el programa GParted.
3.  Con el programa UNETBOOTIN se pasa la imagen al pendrive (hay que
    elegir el archivo ISO como fuente).

Luego ya es cuestión de setear la PC para que arranque con el pendrive y
seguir las instrucciones que aparezcan en pantalla.

## Particiones

[En el sitio de
Fedora](http://docs.fedoraproject.org/en-US/Fedora/21/html/Installation_Guide/sect-installation-gui-manual-partitioning-recommended.html)
la recomendación es la siguiente:

-   **/boot** de 500 MB.
-   **/root** de 10 GB como mínimo, y 20 GB como estándar. Es la
    partición donde se instalarán todos los softwares. Yo suelo dejarlas
    en 30 GB.
-   **/home** de 10 GB como mínimo. Es la partición donde el usuario
    guarda sus documentos, fotos, música, películas\... Debería ser la
    partición más grande.
-   **swap** depende de la memoria y si se usa hibernación o no. Para un
    sistema de 8 GB está bien que sea de 8 a 12 GB.
-   BIOS Boot (1 MB) o **EFI System Partition** (200 MB). En mi caso voy
    a estar instalando sistemas más modernos, así que la idea es que
    sean EFI. El formato del volumen EFI debe ser FAT (así que lo elijo
    como FAT32).

## Post-instalación

Una cosa recomendable es buscar en la web algún artículo como éste: [20
things to do after installing Linux Mint 17 Qiana
Cinnamon](http://www.binarytides.com/better-linux-mint-17-cinnamon/),
que indica pasos a seguir luego de la instalación. Por ejemplo, la
recomendación de instalar los drivers del fabricante de la placa de
video (los pasos detallados están
[aca](http://www.binarytides.com/install-nvidia-drivers-linux-mint-16/))
permitió mejorar el score que da glmark2 de 599 a 1751. Hay que seguir
los pasos con atención, porque en este caso las instrucciones estaban
para placas NVidia y yo tengo una ATI Radeon HD 5570, así que los
drivers hay que buscarlos en la página que corresponda, lo cual no
estaba aclarado en la página mencionada.

