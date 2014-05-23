from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', PanelIndex.as_view(), name='panel_index'),
    url(r'^success/$', Success.as_view(), name='panel_success'),
)
