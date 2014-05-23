import sendwithus
from django.db import models
from django.conf import settings

class WebHandler(models.Model):
    url = models.URLField(unique=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.url

class Recipient(models.Model):
    web_handler = models.ForeignKey(WebHandler, related_name='webhandler')
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    linkedin_link = models.URLField(blank=True, null=True)
    email = models.EmailField()

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Column(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

class ColumnData(models.Model):
    web_handler = models.ForeignKey(WebHandler)
    column = models.ForeignKey(Column)
    value = models.TextField(max_length=350)

    def __unicode__(self):
        return self.value

    class Meta:
        verbose_name_plural = "Column Data"

def get_swu_templates():
    key = settings.SWU_API_KEY
    api = sendwithus.api(api_key=key)
    resp = api.emails()
    return resp.json()