# Uso de MBED desde la linea de comandos (CLI)


Empecé a probar el uso de la plataforma MBED con la placa FRDM-K64F. Hasta ahora
usaba [la versión online del compilador](https://developer.mbed.org/) con una
FRDM-KL25Z, que es una (de las primeras en funcionar con MBED). El problema del
compilador online no es que haya que estar conectado a la web (lo vengo usando
desde hace mucho y nunca tuve problemas de acceso) sino sus limitadas
prestaciones como editor de texto. Por ejemplo, no encontré manera de comentar y
des-comentar múltiples lineas de código simultaneamente, algo que necesito hacer
con frecuencia. Por esto mismo prefiero el editor que uso para el resto de mis
actividades: Emacs, y esto lo puedo hacer con el nuevo compilador offline.

Las instrucciones para usar el compilador desde la linea de comandos (mbed-cli)
las extraje del video que está más abajo y de la documentación. Sin embargo lo
resumo en esta entrada para tener el paso-a-paso como referencia rápida. Por
esto mismo, hay mucha información que no está incluida en este post y que pueden
encontrar en la [documentación de
mbed-cli](https://docs.mbed.com/docs/mbed-os-handbook/en/5.1/dev_tools/cli/)
(como por ejemplo las instrucciones de instalación).

{{< youtube PI1Kq9RSN_Y >}}

## Inicializar un nuevo programa

Al inicializar un nuevo programa se crea un directorio con el nombre que
le asignamos. Este directorio aparece como hijo de nuestro directorio
actual, así que antes de ejecutar el comando hay que posicionarse en la
ubicación deseada.

### Para MBED OS 5

``` console
$ mbed new nombre-programa
$ cd nombre-programa
```

### Para MBED OS 2

``` console
$ mbed new nombre-programa --mbedlib
$ cd nombre-programa
```

## Mostrar las librerías instaladas

Al inicializarse un programa, como mínimo se importan las librerías de
MBED, ya sean las del OS 5 o del OS 2 (son diferentes entre sí). Para
verlas:

``` console
$ mbed ls -a
```

## Selección de placa y toolchain

Hay que conectar la placa MBED mediante su conector USB **OpenSDA** (el
que se usa para programarla) y ejecutar el siguiente comando, que nos
dará información que necesitaremos para seleccionar placa y toolchain:

``` console
$ mbed detect

[mbed] Detected K64F, port /dev/ttyACM0, mounted /media/diego/MBED
[mbed] Supported toolchains for K64F
+--------+-----------+-----------+-----------+-----------+-----------+
| Target | mbed OS 2 | mbed OS 5 |    ARM    |  GCC_ARM  |    IAR    |
+--------+-----------+-----------+-----------+-----------+-----------+
| K64F   | Supported | Supported | Supported | Supported | Supported |
+--------+-----------+-----------+-----------+-----------+-----------+
Supported targets: 1
Supported toolchains: 3
```

El sistema indica que encontró la K64F y cuáles son los *toolchains* que
disponemos para trabajar con ella. **Si conecto la placa KL25Z el
sistema no la detecta, parece que el sistema sólo es compatible con las
placas más nuevas**.

Para seleccionar la placa de destino donde correrá nuestro programa:

``` console
$ mbed target K64F
```

Para elegir el toolchain GCC_ARM usamos:

``` console
$ mbed toolchain GCC_ARM
```

Si pedimos el estado actual de la configuración veremos lo siguiente (si
la ejecución del comando *mbed new* se realizó desde
/home/diego/mis-proyectos):

``` console
$ mbed config --list

[mbed] Global config:
No global configuration is set

[mbed] Local config (/home/diego/mis-proyectos/nombre-programa):
TOOLCHAIN=GCC_ARM
TARGET=K64F
```

## Creación de programa

En el directorio raíz del proyecto es necesario crear un archivo llamado
*main.cpp* que contendrá el programa escrito en C++. Por ejemplo, este
programa enciende y apaga un LED de la placa (usando OS 2):

``` cpp
#include "mbed.h"

DigitalOut rojo(LED1);

void togglearLed(DigitalOut led)
{
    led = !led;
    wait(1);
} // togglearLed

int main() {
    while(1) {
        togglearLed(rojo);
        togglearLed(rojo);
    }
}
```

## Compilación y ejecución del programa

La compilación se realiza con el siguiente comando:

``` console
$ mbed compile
```

**Luego hay que copiar el archivo generado por el compilador en la placa
MBED**. Este archivo (cuyo nombre corresponde al utilizado durante la
inicialización del proyecto: \"nombre-programa\" y cuya extensión es
.bin) se encuentra dentro del directorio BUILD/K64F/GCC_ARM. Obviamente
este path corresponde a la placa y al toolchain elegidos en un paso
anterior. La placa MBED aparece como un disco en el navegador de
archivos. En Linux Mint 18 este disco está montado en /media/diego/MBED.

Luego hay que esperar que se produzca la transferencia del archivo .bin
hacia la placa MBED (parpadea un LED verde que está junto al conector
USB de la placa) y tras algunos segundos (siempre se abre un nuevo
navegador de archivos, como cuando conectamos un pendrive, en la
ubicación del MBED) podemos resetear la placa para que se inicie la
ejecución de nuestro programa. Si cargamos el programa que está copiado
en el paso anterior veremos parpadear el led rojo a una frecuencia de
0.5 Hz.

Si modificamos el programa en main.cpp hay que volver a compilarlo,
copiar el nombre-programa.bin hacia la placa MBED, esperar que se
complete la transferencia y resetearla. Este es el bucle que repetiremos
hasta lograr que nuestro programa funcione de la manera deseada.

## Resumen

``` console
$ mbed new nombre-programa (--mbedlib)
$ cd nombre-programa
$ mbed ls -a
$ mbed detect
$ mbed target K64F
$ mbed toolchain GCC_ARM
$ mbed config --list
$ mbed compile
```

Finalmente copiar el archivo .bin al MBED, esperar que finalice la
transferencia y resetear la placa.

