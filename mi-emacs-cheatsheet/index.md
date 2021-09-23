# Mi Emacs Cheatsheet



| función                  | keybind | doom    |
|--------------------------+---------+---------|
| doom/open-private-config |         | SPC f P |
| describe-function        | C-h f   | SPC h f |
| describe-key             | C-h k   | SPC h k |
| describe-bindings        |         | SPC h b |

| Saltos                           |   |       |                                              |
|----------------------------------+---+-------+----------------------------------------------|
| evil-avy-goto-char-1             |   | g s s | hay que ingresar luego 2 caracteres seguidos |
| goto-last-change                 |   | g ;   | lleva el punto hacia el último cambio        |
| evilem-motion-find-char          |   | g s f | busca un caracter hacia adelante del punto   |
| evilem-motion-find-char-backward |   | g s F | busca un caracter hacia atrás del punto      |


| Comentarios                       |         |     |                              |
|-----------------------------------+---------+-----+------------------------------|
| comment-line                      | C-x C-; |     |                              |
| evilnc-comment-or-uncomment-lines | C-x C-; |     |                              |
| evilnc-comment-operator           |         | g c | comenta y descomenta bloques |
|                                   |         |     |                              |

| Macros                    |         |                                 |
|---------------------------+---------+---------------------------------|
| kmacro-start-macro        | C-x (   | Inicia la grabación             |
| kmacro-end-macro          | C-x )   | Finaliza la grabación           |
| kmacro-end-and-call-macro | C-x e   | Ejecuta la última macro grabada |



| Dired |         |                            |
|-------+---------+----------------------------|
|       | C-x C-q | Editar buffer de Dired     |
|       | C-c C-c | Finalizar edición y grabar |

yasnippets

| Yasnippets             |           |                                            |
|------------------------+-----------+--------------------------------------------|
| yas-visit-snippet-file | C-c & C-v | Muestra los snippets del modo mayor activo |
| yas-new-snippet        | C-c & C-n | Crea un nuevo snippet                      |
|                        |           |                                            |
|                        |           |                                            |

encc

