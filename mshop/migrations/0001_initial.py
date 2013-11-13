# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MshopGoods.masure'
        db.add_column(u'mshop_mshopgoods', 'masure',
                      self.gf('django.db.models.fields.CharField')(default='кг.', max_length=6),
                      keep_default=False)

        # Adding field 'MshopBasket.description'
        db.add_column(u'mshop_mshopbasket', 'description',
                      self.gf('django.db.models.fields.TextField')(default=False, blank=True),
                      keep_default=False)

        # Adding field 'MshopBasket.city'
        db.add_column(u'mshop_mshopbasket', 'city',
                      self.gf('django.db.models.fields.CharField')(default=False, max_length=250),
                      keep_default=False)

        # Adding field 'MshopBasket.email'
        db.add_column(u'mshop_mshopbasket', 'email',
                      self.gf('django.db.models.fields.EmailField')(default=False, max_length=75),
                      keep_default=False)

        # Adding field 'MshopBasket.user'
        db.add_column(u'mshop_mshopbasket', 'user',
                      self.gf('django.db.models.fields.IntegerField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MshopGoods.masure'
        db.delete_column(u'mshop_mshopgoods', 'masure')

        # Deleting field 'MshopBasket.description'
        db.delete_column(u'mshop_mshopbasket', 'description')

        # Deleting field 'MshopBasket.city'
        db.delete_column(u'mshop_mshopbasket', 'city')

        # Deleting field 'MshopBasket.email'
        db.delete_column(u'mshop_mshopbasket', 'email')

        # Deleting field 'MshopBasket.user'
        db.delete_column(u'mshop_mshopbasket', 'user')


    models = {
        u'mshop.mshopbasket': {
            'Meta': {'object_name': 'MshopBasket'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'basket_type': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '10'}),
            'city': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250'}),
            'datetime': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'default': 'False', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': 'False', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'session': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'user': ('django.db.models.fields.IntegerField', [], {'default': 'False'})
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
            'masure': ('django.db.models.fields.CharField', [], {'default': "'kg'", 'max_length': '6'}),
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