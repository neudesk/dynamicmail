from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView
from .forms import PanelForm
from mailman.models import WebHandler
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

class PanelIndex(FormView):
    template_name = "panel/index.djhtml"
    form_class = PanelForm
    success_url = '/panel/success'

    def form_valid(self, form):
        try:
            form.save()
        except Exception as e:
            messages.error(self.request, e)
            self.success_url = '/panel/'
        return super(PanelIndex, self).form_valid(form)

    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_authenticated():
            return redirect('/')
        return super(PanelIndex, self).render_to_response(context, **response_kwargs)

class Success(TemplateView):
    template_name = "panel/success.djhtml"