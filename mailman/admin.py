from django.contrib import admin
from mailman.models import *
from .formutils import ExtFileField
from django import forms
from django.conf import settings
import csv, re

class ColumnAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',), }
    list_display = ('__str__', 'slug')

class ColumnDataAdmin(admin.ModelAdmin):
    list_display = ('web_handler', 'column_name', 'value', 'variable_name')
    list_filter = ('web_handler',)

    def web_handler(self, instance):
        return instance.web_handler.url

    def column_name(self, instance):
        return instance.column.name

    def variable_name(self, instance):
        return instance.column.slug

class RecipientsAdmin(admin.ModelAdmin):
    list_filter = ('web_handler',)
    list_display = ('__str__', 'contact_title', 'first_name', 'last_name', 'email', 'linkedin_link', 'recipient_of')

    def recipient_of(self, instance):
        return instance.web_handler.url

class DataSourceForm(forms.ModelForm):
    file = ExtFileField(ext_whitelist=(".csv",))

    class Meta:
        model = DataSource

    def get_data(self, instance):
        filepath = instance.file
        return [row for row in csv.reader(filepath.read().splitlines())]

    def buildjson(self, data):
        header = data[0]
        del data[0]
        json = {}
        for idx, value in enumerate(header):
            json[value] = [d[idx] for d in data]
        return json

    def migrate_webhandler(self, json):
        data = json['website']
        idx = []
        for d in data:
            webhandler = WebHandler.objects.filter(url=d)
            if not webhandler:
                webhandler = WebHandler.objects.create(url=d)
            else:
                webhandler = webhandler[0]
            idx.append(webhandler)
        return idx

    def migrate_recipients(self, json, webhandler_objects):
        idx = 0
        for obj in webhandler_objects:
            first_name = json['first name'][idx]
            last_name = json['last name'][idx]
            email = json['email'][idx]
            linkedin_link = json['linkedin link'][idx]
            contact_title = json['contact title'][idx]
            recipient = Recipient.objects.filter(email=email)
            if not recipient:
                recipient = Recipient.objects.create(email=email,
                                                     last_name=last_name,
                                                     first_name=first_name,
                                                     linkedin_link=linkedin_link,
                                                     contact_title=contact_title,
                                                     web_handler=obj)
                recipient.save()
            idx += 1

    def migrate_column(self, json):
        excluded_items = ['first name', 'last name', 'contact title', 'linkedin link', 'email', 'key', 'website']
        column_obj = {}
        for k, v in json.items():
            if k not in excluded_items:
                column = Column.objects.filter(name=k)
                if not column:
                    column = Column.objects.create(name=k,
                                                   slug=re.sub(" ", "_", k))
                else:
                    column = column[0]
                column_obj[k] = column
        return column_obj

    def migrate_columndata(self, json, webhandler_objects, column_obj):
        excluded_items = ['first name', 'last name', 'contact title', 'linkedin link', 'email', 'key', 'website']
        for k, v in json.items():
            if k not in excluded_items:
                idx = 0
                for w in webhandler_objects:
                    columndata = ColumnData.objects.filter(web_handler=w,
                                                          column=column_obj[k])
                    if not columndata:
                        columndata = ColumnData.objects.create(web_handler=w,
                                                               column=column_obj[k],
                                                               value=v[idx])
                    else:
                        columndata = columndata[0]
                        columndata.value = v[idx]
                        columndata.save()
                    idx += 1

    def migratejson(self, instance):
        json = self.buildjson(self.get_data(instance))
        webhandler_objects = self.migrate_webhandler(json)
        self.migrate_recipients(json, webhandler_objects)
        column_obj = self.migrate_column(json)
        self.migrate_columndata(json, webhandler_objects, column_obj)



    # def save(self, commit=True):
    #     instance = super(DataSourceForm, self).save()
    #     self.migratecsv(instance)
    #     return instance

class DataSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'file')
    form = DataSourceForm

admin.site.register(DataSource, DataSourceAdmin)
admin.site.register(WebHandler)
admin.site.register(Recipient, RecipientsAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(ColumnData, ColumnDataAdmin)