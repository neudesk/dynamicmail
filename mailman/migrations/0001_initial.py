# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WebHandler'
        db.create_table(u'mailman_webhandler', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(unique=True, max_length=200)),
            ('mail_data', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mailman.MailData'])),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'mailman', ['WebHandler'])

        # Adding model 'Recipient'
        db.create_table(u'mailman_recipient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('linkedin_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'mailman', ['Recipient'])

        # Adding model 'MailData'
        db.create_table(u'mailman_maildata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contacted_yn', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('interaction_notes', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('website_type', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('segment_contact_title', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('platform_shpcart', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('lower_adwordsppcdaily_tspyfl', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('upper_adwordsppcdaily_tspyfl', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('avg_adpos_tspyf', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('advertisers_tspyf', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('value_organictrafficday_tspyf', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('value_paidtrafficday_tspyf', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('paidclickday_tspyf', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('organicclickday_tspyf', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('tea_value', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('rmt_value', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('name_reg_twhxa', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('whois_url_twhxa', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('contact_url_twhxa', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('phone1_twhxa', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('Phone2_twhxa', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('email_twhxa', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('communication_notes', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('scrape_source', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('test_domain', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('low_ppcbudget_tispg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('high_ppcbudget_tispg', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('low_lastmonthclix_tispg', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('high_lastmonthclix_tispg', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('avg_adpos_tispg', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('goog_ppckeywds_tispg', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('yahoo_ppckeywds_tispg', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('competitor1_tispg', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('competitor2_tispg', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('competitor3_tispg', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('competitor4_tispg', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('competitor5_tispg', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal(u'mailman', ['MailData'])


    def backwards(self, orm):
        # Deleting model 'WebHandler'
        db.delete_table(u'mailman_webhandler')

        # Deleting model 'Recipient'
        db.delete_table(u'mailman_recipient')

        # Deleting model 'MailData'
        db.delete_table(u'mailman_maildata')


    models = {
        u'mailman.maildata': {
            'Meta': {'object_name': 'MailData'},
            'Phone2_twhxa': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'advertisers_tspyf': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'avg_adpos_tispg': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'avg_adpos_tspyf': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'communication_notes': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'competitor1_tispg': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'competitor2_tispg': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'competitor3_tispg': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'competitor4_tispg': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'competitor5_tispg': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'contact_url_twhxa': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'contacted_yn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email_twhxa': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'goog_ppckeywds_tispg': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'high_lastmonthclix_tispg': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'high_ppcbudget_tispg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interaction_notes': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'low_lastmonthclix_tispg': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'low_ppcbudget_tispg': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'lower_adwordsppcdaily_tspyfl': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'name_reg_twhxa': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'organicclickday_tspyf': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'paidclickday_tspyf': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'phone1_twhxa': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'platform_shpcart': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'rmt_value': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'scrape_source': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'segment_contact_title': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'tea_value': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'test_domain': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'upper_adwordsppcdaily_tspyfl': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'value_organictrafficday_tspyf': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'value_paidtrafficday_tspyf': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'website_type': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'whois_url_twhxa': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'yahoo_ppckeywds_tispg': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        u'mailman.recipient': {
            'Meta': {'object_name': 'Recipient'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'linkedin_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'mailman.webhandler': {
            'Meta': {'object_name': 'WebHandler'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mail_data': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mailman.MailData']"}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['mailman']