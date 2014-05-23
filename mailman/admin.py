from django.contrib import admin
from mailman.models import *

class ColumnAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }

admin.site.register(WebHandler)
admin.site.register(Recipient)
admin.site.register(Column, ColumnAdmin)
admin.site.register(ColumnData)