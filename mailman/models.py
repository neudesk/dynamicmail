import sendwithus
from django.db import models
from django.conf import settings
import csv

class DataSource(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=150)
    file = models.FileField(upload_to='csv')

    def __unicode__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     path = self.file

class WebHandler(models.Model):
    url = models.URLField(unique=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.url

class Recipient(models.Model):
    web_handler = models.ForeignKey(WebHandler, related_name='webhandler')
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    linkedin_link = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)
    contact_title = models.CharField(max_length=150, blank=True, null=True)

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