from django.conf.urls import patterns, include, url
from .views import PanelIndex

urlpatterns = patterns('',
    url(r'^$', PanelIndex.as_view(), name='panel_index'),
)
