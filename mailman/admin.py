from django.contrib import admin
from mailman.models import *
from .formutils import ExtFileField
from django import forms
import csv, re

class ColumnAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',), }
    list_display = ('__str__', 'slug')

class ColumnDataAdmin(admin.ModelAdmin):
    list_display = ('web_handler', 'column_name', 'value', 'variable_name')

    def web_handler(self, instance):
        return instance.web_handler.url

    def column_name(self, instance):
        return instance.column.name

    def variable_name(self, instance):
        return instance.column.slug

class RecipientsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'contact_title', 'first_name', 'last_name', 'email', 'recipient_of')

    def recipient_of(self, instance):
        return instance.web_handler.url

class DataSourceForm(forms.ModelForm):
    file = ExtFileField(ext_whitelist=(".csv",))

    class Meta:
        model = DataSource

    def get_data(self, instance):
        filepath = instance.file
        return [row for row in csv.reader(filepath.read().splitlines())]

    def get_header(self, data):
        header = data[0]
        del header[0]
        return header

    def get_webhandler_header(self, header):
        return [header[i] for i in [0]]

    def get_recipients_header(self, header):
        return [header[i] for i in [2, 3, 4, 5, 6]]

    def get_column_data_header(self, header):
        columndata = set(header).difference(self.get_webhandler_header(header))
        return list(set(columndata).difference(self.get_recipients_header(header)))

    def get_data_rows(self, data):
        del data[0]
        return data

    def get_webhandler_column_value(self, row):
        del row[0]
        return [row[i] for i in [0]]

    def get_recipients_column_value(self, row):
        del row[0]
        return [row[i] for i in [2, 3, 4, 5, 6]]

    def del_item(self, row):
        del row
        return row

    def get_row_column_data_value(self, row):
        value = set(row).difference(self.get_recipients_column_value(row))
        return list(set(value).difference(self.get_webhandler_column_value(row)))

    def migrate_web_handler(self, wh):
        webhandler = WebHandler.objects.filter(url=wh)
        if not webhandler:
            webhandler = WebHandler.objects.create(url=wh)
            webhandler.save()
        else:
            webhandler = webhandler[0]
        return  webhandler

    def migrate_recipients(self, webhandler_instance, recipient_header, recipient_value):
        recipient_dic = {'web_handler': webhandler_instance}
        for idx, value in enumerate(recipient_header):
            recipient_dic[value] = recipient_value[idx]
        recipient = Recipient.objects.filter(email=recipient_dic['email'])
        if not recipient:
            recipient = Recipient.objects.create(email=recipient_dic['email'],
                                                 last_name=recipient_dic['last_name'],
                                                 first_name=recipient_dic['first_name'],
                                                 linkedin_link=recipient_dic['linkedin_link'],
                                                 contact_title=recipient_dic['recipient_dic'],
                                                 web_handler=recipient_dic['web_handler'])
            recipient.save()
        else:
            recipient = recipient[0]
        return recipient

    def migrate_column(self, column_header):
        column = Column.objects.filter(name=column_header)
        if not column:
            column = Column.objects.create(name=column_header, slug=re.sub(' ', '_', column_header))
            column.save()
        else:
            column = column[0]
        return column

    def migrate_columndata(self, webhandler_instance, column_header, column_value):
        columndata_dic = {'web_handler': webhandler_instance}
        for idx, value in enumerate(column_header):
            columndata_dic[value] = column_value[idx]
        for k, v in columndata_dic:
            columndata =  ColumnData.objects.filter(name=v)
            if not columndata:
                column = Column.objects.filter(name=columndata_dic[k])
                columndata = ColumnData.objects.create(name=column,
                                                       web_handler=columndata_dic['web_handler'],
                                                       value=columndata_dic[k])
                return columndata

    def migratecsv(self, instance):
        data = self.get_data(instance)
        column_data = self.get_data_rows(data)
        headers = self.get_header(data)
        webhandler_header = self.get_webhandler_header(headers)
        recipient_header = self.get_recipients_header(headers)
        column_header = self.get_column_data_header(headers)

        for idx, val in enumerate(webhandler_header):
            webhandler_instance = self.migrate_web_handler(val)
            recipient_value = column_data[idx]
            recipient = self.migrate_recipients(webhandler_instance,
                                                recipient_header,
                                                recipient_value)
            column_value = self.get_row_column_data_value(column_data[idx])
            self.migrate_columndata(self, webhandler_instance, column_header, column_value)

    def save(self, commit=True):
        instance = super(DataSourceForm, self).save()
        self.migratecsv(instance)
        return instance

class DataSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'file')
    form = DataSourceForm

admin.site.register(DataSource, DataSourceAdmin)
admin.site.register(WebHandler)
admin.site.register(Recipient, RecipientsAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(ColumnData, ColumnDataAdmin)