# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MshopGoodsPositions.descr'
        db.add_column(u'mshop_mshopgoodspositions', 'descr',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MshopGoodsPositions.descr'
        db.delete_column(u'mshop_mshopgoodspositions', 'descr')


    models = {
        u'mshop.mshopbasket': {
            'Meta': {'object_name': 'MshopBasket'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'basket_type': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '10'}),
            'datetime': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'session': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'mshop.mshopgoodspositions': {
            'Meta': {'object_name': 'MshopGoodsPositions'},
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'good': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mshop.MshopGoods']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
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