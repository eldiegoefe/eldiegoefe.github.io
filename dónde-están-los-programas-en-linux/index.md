# Dónde están los programas en Linux


Los directorios típicos son los siguientes, aunque hay variaciones en las
distintas distribuciones de linux:

-   [/bin] ejecutables (Essential commands that everyone needs to use at any time)
-   [/usr] A complex hierarchy of additional programs and files.
-   [/usr/bin] normal user executables. The commands that aren't essential for
    users but are useful
-   [/sbin] (superuser core executables) The commands the system Administrator
    needs access to.
-   [/usr/sbin] (superuser executables). The commands that aren't essential for
    Administrators but are useful.
-   Library files: (semi-equivalent to windows dll\'s) [/lib], [/usr/lib], etc.
-   Configuration files: [/etc/]
-   [/run/media] es en donde se montan las unidades portátiles, como el rígido
    externo y el pendrive

También se le puede preguntar al sistema dónde está instalado un paquete:

``` console
$ whereis jekyll
jekyll: /home/diego/.rvm/gems/ruby-2.0.0-p353/bin/jekyll
```

