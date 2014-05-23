from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from .forms import PanelForm
from mailman.models import WebHandler

class PanelIndex(TemplateView):
    template_name = "panel/index.djhtml"
    form_class = PanelForm

    def get_context_data(self, **kwargs):
        context = super(PanelIndex, self).get_context_data( **kwargs)
        context['form'] = self.form_class
        return context