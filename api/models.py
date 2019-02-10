# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField
# To use Json Fields

class Client(models.Model):
   """A model of user"""
   name = models.CharField(max_length=200)
   email = models.CharField(max_length=200)
   zoop_id = models.CharField(max_length=200)
   phone = models.CharField(max_length=200)
   balance = models.FloatField()

class Transaction(models.Model):
   """A model of user's trasactions"""
   buyer = models.ForeignKey("Client", related_name='%(class)s_bought')
   seller = models.ForeignKey("Client", related_name='%(class)s_sold')
   
   buyer_local = JSONField()
   seller_local = JSONField()

   token = models.CharField(max_length=6)

   value = models.FloatField()

class AliveToken(models.Model):
    """A model of token's that can be part of a transaction"""
    token = models.CharField(max_length=6)
    user = models.ForeignKey("Client")
    beginning_at = models.DateTimeField()
    end_at = models.DateTimeField()
    local = JSONField()

class Input(models.Model):
   """A model that tracks the user's inputs"""
   MEHTODS = (
      (0, 'Boleto'),
   )
   client = models.ForeignKey("Client")
   at = models.DateTimeField()
   value = models.FloatField()
   method = models.IntegerField(choices=MEHTODS)
   paid = models.BooleanField(default=False)
   paid_at = models.DateTimeField()
