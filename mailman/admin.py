from django.contrib import admin
from mailman.models import *

class ColumnAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }

class ColumnDataAdmin(admin.ModelAdmin):
    list_display = ('web_handler', 'column_name', 'value', 'variable_name')

    def web_handler(self, instance):
        return instance.web_handler.url

    def column_name(self, instance):
        return instance.column.name

    def variable_name(self, instance):
        return instance.column.slug

class RecipientsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'first_name', 'last_name', 'email', 'recipient_of')

    def recipient_of(self, instance):
        return instance.web_handler.url

admin.site.register(WebHandler)
admin.site.register(Recipient, RecipientsAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(ColumnData, ColumnDataAdmin)