from django import forms
from mailman.models import WebHandler, get_swu_templates

class PanelForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PanelForm, self).__init__(*args, **kwargs)
        wh_choices = [('', 'Please select website url.')]
        wh_choices.extend([(wh.id, str(wh)) for wh in WebHandler.objects.filter(is_active=True)])
        et_choices = [('', 'Please select email template')]
        et_choices.extend([(t['id'], str('%s template' % t['name'])) for t in get_swu_templates()])
        self.fields['web_handler'].choices = wh_choices
        self.fields['email_templates'].choices = et_choices
    web_handler = forms.ChoiceField(choices=(),
                                    widget=forms.Select(attrs={'class':'form-control input-lg'}),
                                    required=True)
    email_templates = forms.ChoiceField(choices=(),
                                        widget=forms.Select(attrs={'class':'form-control input-lg'}),
                                        required=True)