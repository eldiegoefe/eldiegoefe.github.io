# Comunicacion USB con mbed

La comunicación mediante USB con microcontroladores me viene un escollo permanente. El protocolo en sí tiene una complejidad que dispuesto a dedicarle, sobre todo porque empecé a leer varias veces sobre el mismo y siempre me encuentro dando vueltas alrededor de detalles que parecen demasiado específicos y alejados de lo que yo necesito lograr. Decidí hacer la prueba con mbed, ya que tengo una placa kinetis frdm-kl25z de freescale, con la cual hay unos ejemplos de comunicación que parecen muy sencillos.

## Microcontrolador

Del lado del mbed el programa es el siguiente:

``` c++
#include "mbed.h"
#include "USBHID.h"

//We declare a USBHID device. Input out output reports have a length of 8 bytes
USBHID hid(8, 8);

//This report will contain data to be sent
HID_REPORT send_report;
HID_REPORT recv_report;

Serial pc(USBTX, USBRX);

int main(void) {
    send_report.length = 8;

    while (1) {
    //Fill the report
    for (int i = 0; i < send_report.length; i++) {
        send_report.data[i] = rand() & 0xff;
    }

    //Send the report
    hid.send(&send_report);

    //try to read a msg
    if(hid.readNB(&recv_report)) {
        pc.printf("recv: ");
        for(int i = 0; i < recv_report.length; i++) {
        pc.printf("%d ", recv_report.data[i]);
        }
        pc.printf("\r\n");
    }

    wait(0.1);
    }
```

En el [foro de
mbed](https://mbed.org/questions/1348/Whats-the-difference-between-read-and-re/)
preguntan cuál es la diferencia entre read y readNB, y también entre send y
sendNB:

> If there is data to read, read and read_nb do the same, they return that data.
> If not, readNB will return directly that there was no data to read, while read
> blocks until there is data.

> Send is pretty much the same, only then related to the output buffer. If the
> output buffer is empty, both will simply put the data in it and return. If it
> is full, non-blocking will tell there is no space, while blocking will wait
> until there is space.

## Computadora

Del lado de la computadora, el programa en python es:

``` python
#
#Simple example on how to send and receive data to the Mbed over USB (on Linux) using pyUSB 1.0
#
import os
import sys

import usb.core    # the main USB module
import usb.util    # utility functions

from time import sleep
import random

# handler called when a report is received
def rx_handler(data):
    print 'recv: ', data

def tx_handler(data):
    print 'env: ', data


def findHIDDevice(mbed_vendor_id, mbed_product_id):
    # Find device
    hid_device = usb.core.find(idVendor=mbed_vendor_id,idProduct=mbed_product_id)

    if not hid_device:
    print "No device connected"
    else:
    sys.stdout.write('mbed found\n')
    if hid_device.is_kernel_driver_active(0):
        try:
        hid_device.detach_kernel_driver(0)
        except usb.core.USBError as e:
        sys.exit("Could not detatch kernel driver: %s" % str(e))
    try:
        # set the active configuration. With no arguments, the first
        # configuration will be the active one
        hid_device.set_configuration()
        hid_device.reset()
    except usb.core.USBError as e:
        sys.exit("Could not set configuration: %s" % str(e))

    endpoint = hid_device[0][(0,0)][0]

    while True:
        data = [0x0] * 16

        #read the data
        bytes = hid_device.read(endpoint.bEndpointAddress, 8)
        rx_handler(bytes);

        for i in range(8):
        data[i] = bytes[i]
        data[i+8] = random.randint(0, 255)

        tx_handler(bytes)

        hid_device.write(1, data)    # 1 es el endpoint

if __name__ == '__main__':
    # The vendor ID and product ID used in the Mbed program
    mbed_vendor_id = 0x1234
    mbed_product_id = 0x0006

    # Search the Mbed, attach rx handler and send data
    findHIDDevice(mbed_vendor_id, mbed_product_id)
```

## En funcionamiento

En la imagen puede verse la pantalla de emacs donde se ve el envío y
recepción de datos.

![](https://farm9.staticflickr.com/8635/16105028699_317b3557d9_b.jpg)

## Problema resuelto

Hay un problema al ejecutar el programa de la computadora (lo cual hago
usando ipython, tanto en modo terminal como en modo notebook) que
dispara el siguiente error:

``` console
USBError: [Errno 13] Access denied (insufficient permissions)
```

Esto tiene que ver con los permisos para usar el USB. Una solución
rápida es ejecutar el script de python con permisos de root, para lo
cual alcanza con correr ipython anteponiendo sudo:

``` console
$ sudo ipython
```

Recuerdo haber seguido unas instrucciones para habilitar el usuario a
trabajar con el USB, pero no recuerdo dónde estaban y ahora no puedo
encontrarlas (aunque salen muchas páginas si uno busca este error).

