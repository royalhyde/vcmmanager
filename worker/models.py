from __future__ import unicode_literals

from django.db import models
from django.forms.models import model_to_dict
# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=200)
    pwd = models.IntegerField(default=0)


class vcms(models.Model):
    name = models.CharField(max_length=200)
    server = models.CharField(max_length=200)
    busy = models.CharField(max_length=200)


class servers(models.Model):
    name = models.CharField(max_length=200)
    ip = models.CharField(max_length=200, default='')
    sys = models.CharField(max_length=200, default='')
    cpu = models.IntegerField(default=0)
    mem = models.IntegerField(default=0)
    totalInst = models.IntegerField(default=0)
    spec = models.CharField(max_length=300, default='')
    availableInst = models.CharField(max_length=250, default='')
    nance = models.IntegerField(default=0)
    lastreport = models.DateTimeField(default='')


class kmc(models.Model):
    name = models.CharField(max_length=200)
    ip = models.CharField(max_length=200, default='')
    sys = models.CharField(max_length=200, default='')
    cpu = models.IntegerField(default=0)
    mem = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    available = models.IntegerField(default=0)
    nance = models.IntegerField(default=0)
    lastreport = models.DateTimeField(default='')



def records2dict(records, prefix):
    dict = {}
    n = 1
    for rec in records:
        tempdict = {}
        tempkey = '%s%d' % (prefix, n)
        tempdict[tempkey] = model_to_dict(rec,exclude='id')
        dict.update(tempdict)
        n += 1
    return dict
