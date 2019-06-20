from django.db import models

# Create your models here.

class CityInfo(models.Model):

    city    =   models.CharField(max_length=100, null=True, blank=True, verbose_name='地址')
    intro   =   models.TextField(null=True, blank=True, verbose_name='介绍')
    pid     =   models.ForeignKey('self', null=True, blank=True, verbose_name='自关联')

    def __str__(self):
        return self.city

    class Meta:
        db_table = 'city_info'
        verbose_name = '城市'
        verbose_name_plural = verbose_name
