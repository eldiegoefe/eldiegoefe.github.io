# Panel frontal del software


Una vez más me encuentro ante el desafío de armar un panel para un programa de
análisis de datos, hecho en Python. Lo ideal sería trabajar con lineas de
comandos y no tener que estar lidiando con menúes, botones y areas de
graficación, pero sería impractico para los usuarios a quienes está destinado el
programa. Así que nuevamente tengo que rastrear cómo se arma una pantalla con
todas estas cosas.

Como ya usé con anterioridad Qt, PyQt y PyQtGraph voy a continuar
eligiéndolos, aunque se que existen opciones. Con Qt Designer armo el
panel frontal con los elementos básicos: un espacio para ingresar texto
(más adelante será un selector de archivos) y dos gráficas que
contendrán histogramas. Esto último es lo más arduo, porque siempre me
olvido del procedimiento (y por eso armo este artículo, que tiene mucho
extraido de [How to use
PyQtGraph](http://www.pyqtgraph.org/documentation/how_to_use.html)).

1.  Crear un widget QGraphicsView ("Graphics View" en la categoría
    "Display Widgets").
2.  Click derecho sobre el QGraphicsView. Seleccionar "Promote To\...".
3.  En "Promoted class name" teclear el nombre de la clase a utilizar
    (por lo general es "PlotWidget", pero también podría ser
    "GraphicsLayoutWidget", etc).
4.  En "Header file" escribir "pyqtgraph" (sin ninguna extensión).
5.  Click en "Add" y luego click en "Promote".

Al grabar desde Qt Designer tendremos un archivo con extensión \".ui\".
Para convertirlo y poder usarlo en Python es preciso utilizar el
conversor llamado pyuic4:

pyuic4 -x panel.ui -o panel.py

Si no lo tenían instalado y están en un descendiente de Debian o Ubuntu:

sudo apt-get install pyqt4-dev-tools

A continuación se puede ver un ejemplo de un programa en Python que
utiliza el panel que fuimos creado. La clase creada al armar el panel se
llama, por defecto, Ui_MainWindow. En el ejemplo la llamé
Ui_VentanaPrincipal. El panel del ejemplo tiene un boton, una etiqueta y
un PlotWidget.

``` python
from PyQt4 import QtCore, QtGui
from panel import Ui_VentanaPrincipal

import numpy as np

class Window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)
        self.ui.pushButton_actualizar.clicked.connect(self.borrarEtiqueta)

    def borrarEtiqueta(self):
        self.ui.lbl_etiqueta.setText("")

    def escribirEtiqueta(self, texto):
        self.ui.lbl_etiqueta.setText(texto)

    def setearLimitesPlot(self, x1, x2, y1, y2):
        p = self.ui.miCuadricula
        p.setRange(xRange=[x1, x2], yRange=[y1, y2])

    def graficar(self, data):
        p = self.ui.miCuadricula
        p.plot(data)


if __name__ == '__main__':

    import sys

    ## initializing Qt (only once per application)
    app = QtGui.QApplication(sys.argv)

    ## inicializa un objeto (window) que contendra todos los widgets, y lo muestra 
    window = Window()
    window.show()

    window.setearLimitesPlot(0, 25, 0, 1)

    datos = np.random.normal(size=25)
    window.graficar(datos)

    window.ui.lbl_etiqueta.setText("hola")

    ## se puede referenciar al plot desde aqui, de este modo:
    ## p = window.ui.miCuadricula
    ## p.setRange(xRange=[-500, 500], yRange=[-500, 500])

    window.escribirEtiqueta("Etiqueta modificada")

    ## Start the Qt event loop: app.exec()
    sys.exit(app.exec_())
```

