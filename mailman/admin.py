from django.contrib import admin
from mailman.models import *

admin.site.register(WebHandler)
admin.site.register(Recipient)
admin.site.register(MailData)