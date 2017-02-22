
:title: Flask desde Emacs
:date: 2016-11-17 10:00
:category: tecnicismos
:tags: emacs, flask, virtual-envs, git, magit
:author: El Diego Efe
:excerpt: Flask desde Emacs
:disqus_identifier: flask desde emacs
:status: draft

Flask es un microframework que permite armar servidores de páginas web mediante
Python. Mi intención es usarlo para armar un programa de analisis de datos
experimentales, al cual se pueda acceder desde cualquier máquina de una red, sin
tener que instalar nada en la máquina del usuario.

Sin embargo este artículo es sólo para tener una referencia sobre las
herramientas útiles de Emacs para facilitar el desarrollo, y no es realmente
sobre Flask.

Elección de un entorno virtual

Emacs puede acceder a los entornos virtuales instalados en el sistema. Para
gestionarlos (crearlos, agregar versiones de Python disponibles, destruirlos,
etc) uso pyenv y pyenv-virtualenv.

Para seleccionar un entorno virtual de los disponibles usamos M-x
pyenv-mode-set. Desde spacemacs el atajo es *SPC m v s* y como resultado muestra
un menú con los entornos que podemos elegir.
