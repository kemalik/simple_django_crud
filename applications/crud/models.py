# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class Cars(models.Model):
    make = models.CharField(u'Марка', max_length=50)
    model = models.CharField(u'Модель', max_length=50)
    year = models.DateField(u'Год выпуска')
    characteristic = models.TextField(u'Характеристика')

    def __unicode__(self):
        return self.make

    class Meta:
        verbose_name = u'Машина'
        verbose_name_plural = u'Машины'
