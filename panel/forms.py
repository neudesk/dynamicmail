from django import forms
from mailman.models import Recipient, WebHandler, get_swu_templates
import sendwithus
from django.conf import settings

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
    recipients = forms.CharField(max_length=450)

    def save(self):
        api = sendwithus.api(api_key=settings.SWU_API_KEY)
        template_id = self.cleaned_data['email_templates']
        for d in self.get_data(self.cleaned_data):
            res = api.send(
                            email_id=template_id,
                            recipient={'address': d['email']},
                            email_data=d
                          )
            if res.status_code != 200:
                raise Exception(res.text)
                break

    def get_data(self, form_data):
        data = []
        webhandler = WebHandler.objects.filter(id=form_data['web_handler'])[0]
        columndata = webhandler.columndata_set.all()
        recipients = form_data['recipients'].split(',')
        item = {}
        for d in columndata:
            item[d.column.slug] = d.value
        for r in recipients:
            recipient = Recipient.objects.filter(email=r)[0]
            recipient_data = {'first_name': recipient.first_name,
                              'last_name': recipient.last_name,
                              'email': recipient.email,
                              'linkedin_link': recipient.linkedin_link}
            recipient_data.update(item)
            data.append(recipient_data)
        return data

    def send_testmail(self, data):
        api = sendwithus.api(api_key=settings.SWU_API_KEY)
        r = api.send(
          email_id='tem_ed8qjPxQtAEqHwDWVzNwU4',
          recipient={'address': 'neumerance@live.com'},
          email_data=data
        )
        return r
