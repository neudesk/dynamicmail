import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/django/virtualenv/dynamicmail/local/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/var/www/dynamicmail')
sys.path.append('var/www/dynamicmail/dynamicmail')

os.environ['DJANGO_SETTINGS_MODULE'] = 'dynamicmail.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()