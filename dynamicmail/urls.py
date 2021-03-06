from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from tastypie.api import Api
from mailman.api import *

v1_api = Api(api_name='v1')
v1_api.register(WebHandlerResource())
v1_api.register(RecipientResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dynamicmail.views.home', name='home'),
    # url(r'^dynamicmail/', include('dynamicmail.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^panel/', include('panel.urls')),
    (r'^api/', include(v1_api.urls)),
    url(r'^$', 'auth.views.login_user', name='login_user'),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
       'document_root': settings.STATIC_ROOT,
    }),
)
