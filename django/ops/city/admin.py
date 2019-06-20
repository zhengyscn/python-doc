from django.contrib import admin

# Register your models here.
from .models import CityInfo

class CityInfoAdmin(admin.ModelAdmin):
    list_display = ['city', 'intro', 'pid']


admin.site.register(CityInfo, CityInfoAdmin)
