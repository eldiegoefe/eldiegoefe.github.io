# Instalacion de PyQt


Este es un post-ayudamemoria para la instalación de PyQt en un entorno virtual.
Tengo la impresión de que lo escribí ya en el blog pero no lo encuentro ni con
los buscadores más buscados (ag, ack, pt):

1.  Activar el virtualenv, asumiendo que están instalados pyenv y
    pyenv-virtualenvs (también tendría que agregar el tutorial para
    usarlos, pero es demasiado para el propósito del día de hoy, aunque
    \"hoy\" no tiene sentido para un texto perdido en la web).
    Supongamos que el entorno se llama \"lab\":

    ``` terminal
    $ pyenv activate lab
    ```

2.  Crear un directorio para descargar las fuentes de PyQt y SIP, por
    ejemplo dentro del /home/\$user:

    ``` terminal
    $ mkdir build
    $ cd build
    ```

3.  Bajar las últimas versiones de PyQt y SIP de Sourceforge (luego de
    hacer la búsqueda de PyQt ver en la pestaña \"files\", ahí aparecen
    tanto PyQt como SIP). Estos son los enlaces para ir directamente
    (bajar los archivos .tar.gz para X11):
    [PyQt4](http://sourceforge.net/projects/pyqt/files/PyQt4/) y
    [SIP](http://sourceforge.net/projects/pyqt/files/sip/).

4.  Descomprimir los tar (el nombre del archivo depende de la versión
    vigente):

    ``` terminal
    $ tar zxvf PyQt-x11-gpl-4.11.3.tar.gz
    $ tar zxvf sip-4.16.6.tar.gz
    ```

5.  Puede ser necesario instalar algunas dependencias. Para Python 2.7:

    ``` terminal
    $ sudo apt-get install python2.7-dev libxext-dev python-qt4 qt4-dev-tools libqt4-dev build-essential
    ```

    Para Python3:

    ``` terminal
    $ sudo apt-get install python3-dev libxext-dev python-qt4 qt4-dev-tools
    libqt4-dev build-essential
    ```

6.  Compilar SIP y verificar que no haya errores (sobre todo en el make
    install, si aparecen errores puede ser que requiera ejecutar como
    administrador: sudo make install):

    ``` terminal
    $ cd sip-4.16.6
    $ python configure.py
    $ make
    $ [sudo] make install
    ```

    Si aparecen errores porque no se tienen permisos de escritura,
    ejecutar la última orden incluyendo el *sudo* porque parece que la
    instalación si bien se realiza desde el entorno virtual, termina
    escribiendo en /usr/include/python2.7 (que en mi instalación
    pertenece a *root*).

7.  Ir al directorio donde se descomprimió PyQt y ejecutar las mismas
    órdenes:

    ``` terminal
    $ python configure.py
    $ make
    $ [sudo] make install
    ```

    Podría haber un error en el primer comando, relacionado con la falta
    de una instalación de Qt (o con una instalación fallida). Por eso no
    hay que saltearse el paso 5.

8.  Listo, correr Python y verificar que el módulo se importa sin
    errores:

    ``` python
    import PyQt4
    ```

9\. *Old comment*: \"Pffff, no funciona ahora\... Después de tanto
detalle la cosa no anda, que garrón (anduvo y después dejó de andar,
tiene demasiados problemas esto).\"

*New comment*: Anduvo todo bien, lo que pasa es que probaba con \"import
pyqt4\" todo en minúscula y entonces daba error. ¡Cuidado entonces con
las instrucciones porque son case-sensitive!

10. Nota a mi mismo: instalar también pyqtgraph, pyusb (con PIP).

