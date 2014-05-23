from tastypie.resources import ModelResource
from tastypie import fields
from .models import *

class RecipientResource(ModelResource):
    class Meta:
        queryset = Recipient.objects.all()
        resource_name = 'recipient'
        include_resource_uri = True

class WebHandlerResource(ModelResource):
    recipients = fields.ToManyField('mailman.api.RecipientResource',
                                    'webhandler', full=True, null=True)
    class Meta:
        queryset = WebHandler.objects.all()
        resource_name = 'webhandler'
        include_resource_uri = True