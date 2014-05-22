from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

class PanelIndex(TemplateView):
    template_name = "panel/index.djhtml"