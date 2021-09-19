# Instrucciones para armar un blog geek


En mi caso, alcanzar un estado zen requiere atravesar travesías barrocas.
Mientras miraba cosas de IPython llegué a [Pythonic
Perambulations](http://jakevdp.github.io/). Me gustó el contenido (muestra cómo
armar ventanas de browsers con matplotlib interactivo), me gustó el diseño y me
llamó la atención el dominio **github.io**.

Blogs como el de [Jake Vanderplas](http://jakevdp.github.io) se arman
con un motor llamado Jekyll.

(*editado: Jake migró su sitio a Pelican, que está escrito en Python. Armé un
post para explicar cómo instalarlo y usarlo en conjunción con las páginas
personales de GitHub, ver [Blog con Pelican y Github]({{< ref
"/posts/2014/2014-04-22-setear-blog-con-pelican-y-github" >}} "Blog"). **Por ende
este post queda desactualizado, además de haber quedado incompleto o quizás con
errores**).

Jekyll está escrito en Ruby, que permite desentendernos de los sistemas de
publicación de contenidos (como Wordpress, con el que armé sitios como
[Policiclos](http://policiclos.com.ar) y a los cuales terminé perdiendo acceso
por culpa de un hacker indonesio que me cambió la página de acceso al panel de
control del blog por un texto burlón en un ingles todo despatarrado, por lo cual
el sitio está sin actualizar desde hace un par de años (igual ahora en el año
2014 el servicio de nombres en Argentina empieza a ser pago, con lo cual hubiese
sido bastante posible que este -y otros blogs- fuesen dados de baja). Con Jekyll
la idea es que uno escribe texto plano (no hace falta escribir en html), se
desentiende de la tarea de actualizar con cierta frecuencia el manejador de
contenidos (actualizar wordpress), crea sitios estáticos que se cargan muy
rápido (y pueden lucir muy lindos) y obtiene más flexibilidad que las propuestas
de blogging populares: [Blogger](http://www.blogger.com),
[Wordpress](http://www.wordpress.com), [Tumblr](http://www.tumblr.com), etc.

Pero nunca nada es tan fácil como dicen por ahí. Quizás con las instrucciones
siguientes puedan replicar una versión corta de lo que ha sido mi experiencia.
Se ahorrarían así varias horas de intentos fallidos:

Toda la información está en [la web de Jekyll](http://jekyllrb.com) (sin
embargo, continúo con la síntesis de lo que yo hice). Hay un gran tutorial
escrito por Andrew Munsell (revisando esto en 2021 veo que lo convirtió en un
curso pago): [Jekyll by
example](https://www.andrewmunsell.com/course/learning-jekyll-by-example/).

## Instalación de Software Requerido

Para instalar Jekyll se necesita Ruby y RubyGems. Bajé los últimos paquetes de
ambos, los descomprimí y compilé pero, seguramente por mi falta de experiencia
en Linux, la cosa no marchaba. Terminé instalando RVM: [Ruby Version
Manager](https://rvm.io). Para usarlo abren un terminal de Linux y piden una
lista de todos los interpretes de Ruby que RVM es capaz de instalar en su
sistema.

``` console
$ rvm list known
```

A mi me dio un listado que incluía (pero no se limitaba) a:

``` console
# MRI Rubies
[ruby-]1.8.6[-p420]
[ruby-]1.8.7[-p374]
[ruby-]1.9.1[-p431]
[ruby-]1.9.2[-p320]
[ruby-]1.9.3[-p484]
[ruby-]2.0.0-p195
[ruby-]2.0.0[-p353]
[ruby-]2.1.0
[ruby-]2.1-head
ruby-head
```

Elegí instalar la versión 2.1.0 con la siguiente instrucción:

``` console
$ rvm install 2.1.0
```

Para ver que versión de Ruby tienen efectivamente instalada teclean:

``` console
$ ruby -v
```

## Instalación de Jekyll

Ahora sí van a poder instalar Jekyll:

``` console
$ gem install jekyll
```

## Generación del nuevo blog

El sitio se inicializa generándose los primeros archivos imprescindibles:

``` console
$ jekyll new el-nombre-de-mi-blog
```

Después hay que hacer un build:

``` console
$ jekyll build
```

## Blog local

Se puede acceder a la versión local del sitio web (para corroborar que todo se
vea tal como se desea, antes de subirlo al hosting):

``` console
$ jekyll serve --watch
```

La dirección para ver el sitio generado será <http://localhost:4000> o sino
también <http://0.0.0.0:4000>. El agregado de **\--watch** permite que si se
realizan cambios en los archivos, éstos se puedan ver inmediatamente recargando
la página del navegador.

## Subiendo el sitio a un hosting

Para actualizar el sitio en el hosting sólo hará falta subir al mismo el
contenido de la carpeta **\_site**.

## The End

La ventaja de Jekyll es que finalmente se termina escribiendo en texto plano
(con la ayuda de [Markdown](http://daringfireball.net/projects/markdown/) se
generan páginas estáticas (que funcionan muy rápido) y se logra inmunidad frente
a los ataques de hackers de Indonesia.

