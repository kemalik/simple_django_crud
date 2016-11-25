# coding=utf-8
from __future__ import unicode_literals

from django.db import models

YEARS_CHOICE = (
    ('2000', '2000'),
    ('2001', '2001'),
    ('2002', '2002'),
    ('2003', '2003'),
    ('2004', '2004'),
    ('2005', '2005'),
    ('2006', '2006'),
    ('2007', '2007'),
    ('2008', '2008'),
    ('2009', '2009'),
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
    ('2015', '2015'),
    ('2016', '2016'),
)

class Cars(models.Model):
    make = models.CharField(u'Марка', max_length=50)
    model = models.CharField(u'Модель', max_length=50)
    year = models.CharField(u'Год выпуска', max_length=20, choices=YEARS_CHOICE)
    characteristic = models.TextField(u'Характеристика')

    def __unicode__(self):
        return self.make

    class Meta:
        verbose_name = u'Машина'
        verbose_name_plural = u'Машины'
