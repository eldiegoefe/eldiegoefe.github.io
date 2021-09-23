# Apuntes sobre matplotlib


Estos son algunos apuntes extraidos principalmente del [tutorial de Artist](http://matplotlib.org/users/artists.html).

### Matplotlib

Matplotlib is the whole package

### **pylab**

-   a module in matplotlib
-   installed alongside matplotlib
-   preferred for interactive calculations and plotting

### **matplotlib.pyplot**

-   a module in matplotlib provides the state machine interface to the
    underlying plotting library in matplotlib
-   combines the pyplot functionality (for plotting) with numpy
    functionality in a single namespace
-   figures and axes are implicitly and automatically created to achieve
    the desired plot
-   preferred for scripting

## Artist

Artist has three layers:

1.  matplotlib.backend_bases.FigureCanvas: area onto which the figure is
    drawn
2.  matplotlib.backend_bases.Renderer: object which knows how to draw on
    the FigureCanvas
3.  matplotlib.artist.Artist: object that knows how to use a renderer to
    paint onto the canvas (el usuario típico usa esto el 95% del tiempo)

1 and 2 handle all the details of talking to user interface toolkits
(Qt4)

3 handles all the high level constructs like representing and laying out
the figure, text and lines

### Artist types

-   primitive: standard graphical objects we want to paint onto our
    canvas (Line2D, Rectangle, Text, AxesImages, etc)
-   containers: places to put the primitives (Axis, Axes, Figure)

### Standard use

Create a Figure instance use the Figure to create one or more Axes or
Subplot instances use the **Axes** (plotting area into which most of the
objects go) instance **helper methods** (plot(), text(), hist(), etc) to
create the **primitives** (Line2D, Text, Rectangle).

**Helper methods**

> will take your data (numpy arrays, strings) and create primitive
> Artists instances as needed (Line2D, etc), add them to the relevant
> containers and draw them when requested

**Subplots**

> a special case of an Axes that lives in a regular rows by columns grid
> of subplots instances.

**Axes**

> if you want to create an Axes at an arbitrary location, simply use the
> add_axes() method which takes a list of \[left, bottom, width,
> height\] values in 0-1 relative coordinates.

   
{{< figure src="https://farm8.staticflickr.com/7562/15668742154_5fa9d2804e_b.jpg" title="Apuntes horrorosos" width=50% >}}
   

Había hecho este dibujito cuando estaba viendo este tema, para aplicarlo
a un programa para linealizar termistores, pero veo que en el dibujo la
jerarquía de Figure y Canvas aparecen distinto en los dos gráficos, no
se si es un error\...

