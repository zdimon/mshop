# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table(u'page_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('content', self.gf('tinymce.models.HTMLField')()),
            ('seo_content', self.gf('django.db.models.fields.TextField')()),
            ('seo_title', self.gf('django.db.models.fields.TextField')()),
            ('seo_keywords', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'page', ['Page'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table(u'page_page')


    models = {
        u'page.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seo_content': ('django.db.models.fields.TextField', [], {}),
            'seo_keywords': ('django.db.models.fields.TextField', [], {}),
            'seo_title': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['page']