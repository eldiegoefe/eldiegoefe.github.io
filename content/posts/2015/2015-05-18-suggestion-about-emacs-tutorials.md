---
title: Suggestion about Emacs tutorials
date: 2015-05-18T10:00:00
categories: [tecnicismos]
tags: [emacs]
author: Diego Efe
toc: false
---

Para leer este texto en español: [click
aca](https://eldiegoefe.github.io/sugerencia-respecto-de-los-tutoriales-de-emacs.html)

I read many Emacs blogs since I started the trip of learning it. There are great
beginner\'s tutorials and also webpages for more advanced users. However,
there\'s a habit I find repeatedly on the majority of sites which goes against
one of the Almighty Editor advantages: instructions usually refer to default
keybindings, like it was invariant that you visit files only with C-x C-f, or
like the only admited shortcuts to the beginning and ending of the current line
where C-a and C-e, or if the incremental search inevitable required to type C-s.
In my case, keybindings for all these functions and many others are
personalized, and the default ones are disabled (I visit files with C-o, move
the point to the beginning or end of the line with M-h and S-M-h, and activate
incremental searches with C-f).

My advice to all the Emacs educator\'s community is to refer and cite
the suggested function names in tutorials and comments, instead of using
their default keybindings. For example, you should talk about
isearch-forward instead of writing C-s; it is better to write the whole
move-beginning-of-line function name instead of only refering to C-a.
This way, it is possible to follow step by step instructions using
execute-extended-command (generally executed with M-x, although in my
setup that happens with M-a).

Then, if you need to know the keybinding to a function, just execute
describe-function to get its abstract and see its keybindings.
