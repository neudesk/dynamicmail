from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView
from .forms import PanelForm
from mailman.models import WebHandler
from django.contrib import messages

class PanelIndex(FormView):
    template_name = "panel/index.djhtml"
    form_class = PanelForm
    success_url = '/panel/success'

    def form_valid(self, form):
        form.save()
        # try:
        #     form.save()
        # except Exception as e:
        #     messages.error(self.request, e)
        #     self.success_url = '/panel/'
        return super(PanelIndex, self).form_valid(form)

class Success(TemplateView):
    template_name = "panel/success.djhtml"