# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Column.slug'
        db.add_column(u'mailman_column', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=8, max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Column.slug'
        db.delete_column(u'mailman_column', 'slug')


    models = {
        u'mailman.column': {
            'Meta': {'object_name': 'Column'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'mailman.columndata': {
            'Meta': {'object_name': 'ColumnData'},
            'column': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mailman.Column']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'web_handler': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mailman.WebHandler']"})
        },
        u'mailman.recipient': {
            'Meta': {'object_name': 'Recipient'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'linkedin_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'web_handler': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mailman.WebHandler']"})
        },
        u'mailman.webhandler': {
            'Meta': {'object_name': 'WebHandler'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['mailman']