#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Diego Fainstein'
SITENAME = u'Certezas Dudosas'
SITESUBTITLE = u'todo lo liquido se desvanece en el estomago'
SITEURL = 'http://eldiegoefe.github.io'
TIMEZONE = 'America/Argentina/Buenos_Aires'
DEFAULT_LANG = u'es'
# DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE_FORMAT = '%Y %B %d %a'
DATE_FORMATS = {
    'en': ('en_US','%Y, %B %d %a'),
    'jp': ('ja_JP','%Y-%m-%d(%a)'),
}
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
    # ('Archives', 'archives.html'),
          ('TecnoVortex', 'http://tecnovortex.com/'),
          ('GeekHack', 'http://geekhack.org/'),
          ('Prelude', 'http://batsov.com/prelude/'),
          ('Ergoemacs', 'http://ergoemacs.org/'),
          ('Seminario Gargarella', 'http://seminariogargarella.blogspot.com.ar/'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/eldiegoefe'),
          ('Github', 'http://github.com/eldiegoefe'),
          ('Facebook', 'http://www.facebook.com/eldiegoefe'),
          ('Flickr', 'http://www.flickr.com/photos/eldiegoefe/'),
          ('Instagram', 'http://instagram.com/eldiegoefe'),
          ('Google+', 'http://plus.google.com/+DiegoEfe'),
          ('Diaspora', 'http://www.joindiaspora.com/u/eldiegoefe'),
)

DEFAULT_PAGINATION = 20

# Seteos para modificar cuando pruebo el blog con un servidor en localhost
# Los posts con fecha futura se toman como drafts
# WITH_FUTURE_DATES = False
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# THEME = "/home/user/pelican-themes/theme-name"
# Mis agregados

THEME = "../pelican-elegant"

# THEME = "notmyidea"    # es un tema built-in
# THEME = "foundation-default-colours"
# CSS_FILE = "elegant.css"


# TAG_CLOUD_STEPS = 4
# TAG_CLOUD_MAX_ITEMS = 100


FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
DISQUS_SITENAME = "certezasdudosas"

# Instrucciones para la instalacion del plugin para videos de youtube
# en http://github.com/kura/pelican_youtube
PLUGIN_PATHS = ['../pelican-plugins']

LOAD_CONTENT_CACHE = False

# Direct_Templates lo requiere Elegant, esta habilitado mas abajo
# DIRECT_TEMPLATES = ('index', 'categories', 'archives')
TYPOGRIFY = True

TWITTER_USERNAME = 'eldiegoefe'

# ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
# ARTICLE_SAVE_AS = '/home/eldiegoefe/documentos/eldiegoefe.github.io/output/{date:%Y}/{date:%m}/{slug}.html'
# ARTICLE_EXCLUDES = ('pages',)
# PAGE_URL = 'pages/{slug}.html'


# Elegant requiere los siguientes seteos

PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'pelican_youtube']
# el plugin pelican_youtube lo tenia desde antes de Elegant

MARKDOWN = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# esto tambien es de Elegant...
# These are the optional configuration variables that you can define

RECENT_ARTICLES_COUNT = 30
COMMENTS_INTRO = u'No te vayas sin comentar algo del post, de las noticias del día, del clima, que se yo...'
SITE_LICENSE = u'Podes usar el contenido de este blog si pones un link hacia http://eldiegoefe.github.io/'
SITE_DESCRIPTION = u'Blog de Diego Fainstein'
EMAIL_SUBSCRIPTION_LABEL = u'Suscripción'
EMAIL_FIELD_PLACEHOLDER = u'¿dirección de e-mail?'
SUBSCRIBE_BUTTON_TITLE = u'Suscribirme'
# MAILCHIMP_FORM_ACTION = u'Esto es del mailchimp'

LANDING_PAGE_ABOUT = ({'title': 'Un hombre serio', 'details': '<p>Bioingeniero en la ficción, en la vida real defiende monstruos del ataque de todo tipo de superhéroes.</p>'})

# PROJECTS = [{
#     'name': 'Logpad + Duration',
#     'url': 'https://github.com/talha131/logpad-plus-duration#logpad--duration',
#     'description': 'Vim plugin to emulate Windows Notepad logging feature,'
#     ' and log duration of each entry'},
#     {'name': 'Elegant Theme for Pelican',
#     'url': 'http://oncrashreboot.com/pelican-elegant',
#     'description': 'A clean and distraction free theme, with search and a'
#     ' lot more unique features, using Jinja2 and Bootstrap'}]


# These are the optional article meta data variables that you can use

# subtitle
# summary
# disqus_identifier
# modified
# keywords

# info sobre sitemap. priorities y changefreqs tienen valores que usan
# los buscadores. mas info en:
# http://docs.getpelican.com/en/3.1.1/plugins.html#sitemap

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
