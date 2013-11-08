# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):


        # Adding model 'MshopGoods'
        db.create_table(u'mshop_mshopgoods', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mshop.MshopCategories'])),
            ('name', self.gf('django.db.models.fields.CharField')(default=False, max_length=250)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('description', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'mshop', ['MshopGoods'])

        # Adding model 'MshopGoodsPositions'
        db.create_table(u'mshop_mshopgoodspositions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('good', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mshop.MshopGoods'])),
            ('name', self.gf('django.db.models.fields.CharField')(default=False, max_length=250)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal(u'mshop', ['MshopGoodsPositions'])

        # Adding model 'MshopBasket'
        db.create_table(u'mshop_mshopbasket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('basket_type', self.gf('django.db.models.fields.CharField')(default='new', max_length=10)),
            ('session', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('datetime', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'mshop', ['MshopBasket'])

        # Adding model 'MshopBasketPositions'
        db.create_table(u'mshop_mshopbasketpositions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mshop.MshopGoodsPositions'])),
            ('ammount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mshop', ['MshopBasketPositions'])

        # Adding model 'RecipesComments'
        db.create_table(u'mshop_recipescomments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mshop.MshopGoods'])),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('is_pub', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'mshop', ['RecipesComments'])


    def backwards(self, orm):
        # Deleting model 'MshopCategories'
        db.delete_table(u'mshop_mshopcategories')

        # Deleting model 'MshopGoods'
        db.delete_table(u'mshop_mshopgoods')

        # Deleting model 'MshopGoodsPositions'
        db.delete_table(u'mshop_mshopgoodspositions')

        # Deleting model 'MshopBasket'
        db.delete_table(u'mshop_mshopbasket')

        # Deleting model 'MshopBasketPositions'
        db.delete_table(u'mshop_mshopbasketpositions')

        # Deleting model 'RecipesComments'
        db.delete_table(u'mshop_recipescomments')


    models = {
        u'mshop.mshopbasket': {
            'Meta': {'object_name': 'MshopBasket'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'basket_type': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '10'}),
            'datetime': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'session': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'mshop.mshopbasketpositions': {
            'Meta': {'object_name': 'MshopBasketPositions'},
            'ammount': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mshop.MshopGoodsPositions']"})
        },
        u'mshop.mshopcategories': {
            'Meta': {'object_name': 'MshopCategories'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'mshop.mshopgoods': {
            'Meta': {'object_name': 'MshopGoods'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mshop.MshopCategories']"}),
            'description': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250'})
        },
        u'mshop.mshopgoodspositions': {
            'Meta': {'object_name': 'MshopGoodsPositions'},
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'good': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mshop.MshopGoods']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250'})
        },
        u'mshop.recipescomments': {
            'Meta': {'object_name': 'RecipesComments'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_pub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mshop.MshopGoods']"})
        }
    }

    complete_apps = ['mshop']