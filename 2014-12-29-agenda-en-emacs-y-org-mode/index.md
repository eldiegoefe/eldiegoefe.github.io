# Agenda en Emacs y OrgMode


## Configuracion

En el archivo de configuracion de Emacs hay que incluir varios elementos
para poder usar la agenda adecuadamente.

Se pueden seleccionar individualmente los archivos que forman parte de
la agenda:

``` cl
(setq org-agenda-files (list "~/mis-archivos-org/apuntes-varios.org"
                             "~/mis-archivos-org/acomodar.org"))
```

O sino utilizar un directorio completo:

``` cl
(setq org-agenda-files '("~/mis-archivos-org"))
```

Se puede utilizar un archivo en particular para ir anotando al vuelo las
ideas que se nos ocurren. Este archivo lo podremos abrir con
*org-capture* (C-c c). Esto nos permite volcar lo que tenemos en la
cabeza y dejar para después su clasificación, de manera de no perder la
idea e interrumpir nuestro flujo de trabajo lo menos posible. La nota se
cierra con C-c C-c y se vuelve al mismo buffer donde estabamos al
iniciar la captura.

``` cl
(setq org-default-notes-file "~/mis-archivos-org/inbox.org")
```

Para abrir el inbox.org desde cualquier buffer se puede asignar un
atajo:

``` cl
;; asigna "C-c o" para abrir mi inbox.org sin tener que buscarlo
(global-set-key (kbd "C-c o")
                (lambda () (interactive) (find-file "~/org/inbox.org")))
```

Estos son otros comandos de configuración de org-mode que tengo
seteados. Salvo el primero, el resto puede entenderse por inspección:

``` cl
(setq org-agenda-include-diary t)
(setq org-deadline-warning-days 7)

;; Palabras clave para los TODO
(setq org-todo-keywords
      '((sequence "TODO(t)" "NEXT(n)" "ESPERANDO(w@)" "HIBERNANDO(h@)"
                  "|" "CANCELADO(c@)" "COMPLETADO(f@)")))

;; Colores de los TODO
(setq org-todo-keyword-faces
      '(("TODO" . (:foreground "deep sky blue" :background "dim gray" :weight bold))
        ("NEXT" . (:foreground "tomato" :background "dim gray" :weight bold))
        ;; ("ACCIONFUTURA" . "salmon")
        ;; ("AVANCEPARCIAL" . "medium spring green")
        ("ESPERANDO" . (:foreground "orange" :background "dim gray" :weight bold))
        ("HIBERNANDO" . (:foreground "salmon" :background "dim gray" :weight bold))
        ("CANCELADO" . "yellow")
        ("COMPLETADO" . "green")))

 ;; Tags
(setq org-tag-persistent-alist
      '(("@casa" . ?1)
        ("@laburo" . ?2)
        ("tiempolibre" . ?3)
        ("compras" . ?6)
        ("nota" . ?7)
        ("creat" . ?8)
        ("prj" . ?9)
        ("someday" . ?0)))

;; Colores de los tags
(setq org-tag-faces
      '(("@casa" . (:foreground "firebrick" :weight bold :inherit s-variable-pitch))
        ("@laburo" . "light sea green")
        ("tiempolibre" . "deep sky blue")
        ("compras" . "spring green")
        ("oblig" . "light coral")
        ("creat" . "olive drab")
        ("prj" . "cornflower blue")
        ("someday" . "orchid")))
```

Estas son las plantillas correspondientes a los distintos tipos de notas
configuradas para guardarse en archivos como inbox.org, diario-personal,
etc. Cada nota puede tener una estructura particular, en algunos casos
importa colocar una fecha, una etiqueta, un deadline, etc:

``` cl
;; Capture templates for: TODO tasks, Notes, appointments, phone calls,
;; meetings, and org-protocol
(setq org-capture-templates
      (quote (("a" "tarea" entry (file "~/mis-archivos-org/inbox.org")
               "* TODO %^{Brief Description} %^g\n\n%?\n\nAgregado: %T")
              ("t" "todo" entry (file "~/mis-archivos-org/inbox.org")
               "* TODO %?\n%U\n%a\n" :clock-in t :clock-resume t)
              ("n" "nota" entry (file "~/mis-archivos-org/inbox.org")
               "* %? :NOTE:\nAgregado: %T\n\n")
              ("j" "journal" entry (file+datetree "~/mis-archivos-org/diario-personal.org")
               "* %?\n%T\n" :clock-in t :clock-resume t)
              ("l" "laboratorio" entry (file+datetree "~/mis-archivos-org/laboratorio-diario.org")
               "* %?\n%t\n")
              ("e" "ejercicios" entry (file+datetree "~/mis-archivos-org/cosas-saludables.org")
               "* %?\n%T\n")
              ("r" "respond" entry (file "~/mis-archivos-org/inbox.org")
               "* NEXT Respond to %:from on %:subject\nSCHEDULED: %t\n%U\n%a\n" :clock-in t :clock-resume t :immediate-finish t)
              ;; b: modificado de http://members.optusnet.com.au/~charles57/GTD/gtd_workflow.html
              ("w" "org-protocol" entry (file "~/mis-archivos-org/inbox.org")
               "* TODO Review %c\n%U\n" :immediate-finish t)
              ("m" "Meeting" entry (file "~/mis-archivos-org/inbox.org")
               "* MEETING with %? :MEETING:\n%U" :clock-in t :clock-resume t)
              ("p" "Phone call" entry (file "~/mis-archivos-org/inbox.org")
               "* PHONE %? :PHONE:\n%U" :clock-in t :clock-resume t)
              ("h" "Habit" entry (file "~/mis-archivos-org/inbox.org")
```

Finalmente, para acceder a la agenda hay que invocar el comando
*org-agenda* o configurar una combinación de teclas para su ejecución,
habitualmente se usa C-c a:

``` cl
(global-set-key "\C-ca" 'org-agenda)
```

Allí aparece un menú con las distintas opciones de visualización. A
continuación se describen las opciones (es un resumen de la sección
[Built in agenda
views](http://orgmode.org/manual/Built_002din-agenda-views.html#Built_002din-agenda-views).

### Vista 1

org-agenda-list (C-c a a): muestra la vista de agenda para el número de
días fijado por la variable org-agenda-span (que puede contener un
número o uno de los valores siguientes: day, week, month, year). Por
defecto esta variable está elegida en \"week\" (mostrará una semana). Si
se invoca el comando con un prefijo numérico se incluyen esa cantidad de
días. Por ejemplo con C-u 3 0 C-c a a se mostrará una agenda para los
siguientes 30 días. Para agendas semanales, se empieza por defecto en el
lunes previo.

### Vista 2

org-todo-list (C-c a t): es la lista global de \"TODO\"s, muestra en un
solo lugar todos los items marcados como pendientes (TODO).

org-todo-list (C-c a T): es una variación que pregunta por una keyword y
lista entonces todos los items marcados con esa keyword (por ejemplo:
CANCELADO o COMPLETADO, etc). Se pueden incluir varias keywords usando
el caracter \"\|\" (que es un OR).

Para acortar la lista de TODOs hay dos modos:

1.  sacar de la lista aquellos TODOs que estén marcados como schedule y
    deadline, para lo cual hay que configurar las variables
    org-agenda-todo-ignore-scheduled, org-agenda-todo-ignore-deadlines,
    org-agenda-todo-ignore-timestamp y/o
    org-agenda-todo-ignore-with-date.
2.  los items TODO pueden tener subniveles con las distintas subtareas.
    En estos casos puede ser suficiente listar sólo los niveles de mayor
    importancia y omitir los subniveles. Para ello hay que configurar
    las variable org-agenda-todo-list-sublevels.

### Vista 3

org-tags-view (C-c a m): muestra una lista de acuerdo a etiquetas (tags)
o propiedades, que se seleccionan de una lista.

org-tags-view (C-c a M): es parecido, pero además requiere que la
etiqueta sea un TODO (y que este TODO no haya sido COMPLETADO).

Hay muchos detalles sobre la construcción de criterios de búsqueda más
complejos en [este link del
manual](http://orgmode.org/manual/Matching-tags-and-properties.html#Matching-tags-and-properties).

### Vista 4

org-timeline (C-c a L): resume todos los items marcados con fecha,
principalmente usado para dar un panorama de los eventos de un proyecto.

Si se usa un prefijo (C-u) se muestran todos los TODOs sin completar que
también estén listados debajo del mismo día.

### Vista 5

org-search-view (C-c a s): es una herramienta para búsqueda de texto,
particularmente útil para encontrar notas. Admite búsquedas literales y
usando \"regexp\". Ver detalles de búsqueda [en el
manual](http://orgmode.org/manual/Search-view.html#Search-view).

### Vista 6

org-agenda-list-stuck-projects (C-c a #): al seguir un sistema como GTD
(de David Allen), hay que revisar regularmente que todos los proyectos
se muevan. Un proyecto estancado es uno que no tiene definidas las
\"próximas acciones\", de modo que nunca aparecería en la lista de TODOs
que produce org-mode.

Para personalizar el modo de identificar y encontrar proyectos
estancados se utiliza C-c a !. Por defecto supone que todos los
proyectos son headlines de nivel 2, y que no están estancados si tiene
al menos una entrada marcada con alguna de las tres keywords: TODO,
NEXT, NEXTACTION.

Ver más detalles sobre esta configuración en [stuck
projects](http://orgmode.org/manual/Stuck-projects.html#Stuck-projects).

