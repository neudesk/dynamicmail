# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'MailData'
        db.delete_table(u'mailman_maildata')

        # Adding model 'Column'
        db.create_table(u'mailman_column', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'mailman', ['Column'])

        # Adding model 'ColumnData'
        db.create_table(u'mailman_columndata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('web_handler', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mailman.WebHandler'])),
            ('column', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mailman.Column'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=350)),
        ))
        db.send_create_signal(u'mailman', ['ColumnData'])


    def backwards(self, orm):
        # Adding model 'MailData'
        db.create_table(u'mailman_maildata', (
            ('avg_adpos_tspyf', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('segment_contact_title', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('value_organictrafficday_tspyf', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('web_handler', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mailman.WebHandler'])),
            ('website_type', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('value_paidtrafficday_tspyf', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('tea_value', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('platform_shpcart', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('interaction_notes', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('avg_adpos_tispg', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('contact_url_twhxa', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('competitor4_tispg', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('email_twhxa', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('scrape_source', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('competitor5_tispg', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('organicclickday_tspyf', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('low_ppcbudget_tispg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('high_ppcbudget_tispg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('phone1_twhxa', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yahoo_ppckeywds_tispg', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('high_lastmonthclix_tispg', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('name_reg_twhxa', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('advertisers_tspyf', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('competitor2_tispg', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('competitor3_tispg', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('communication_notes', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('upper_adwordsppcdaily_tspyfl', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('rmt_value', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('low_lastmonthclix_tispg', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('contacted_yn', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('whois_url_twhxa', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('test_domain', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('paidclickday_tspyf', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('goog_ppckeywds_tispg', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('lower_adwordsppcdaily_tspyfl', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('competitor1_tispg', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('Phone2_twhxa', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'mailman', ['MailData'])

        # Deleting model 'Column'
        db.delete_table(u'mailman_column')

        # Deleting model 'ColumnData'
        db.delete_table(u'mailman_columndata')


    models = {
        u'mailman.column': {
            'Meta': {'object_name': 'Column'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
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