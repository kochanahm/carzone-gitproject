from django.contrib import admin
from cars.models import Car
from django.utils.html import format_html


# Register your models here.

class CarAdmin(admin.ModelAdmin):
  def thumbnail(self,object):
    return format_html('<img src="{}" width="40" style="border-radius: 50px" />'.format(object.car_photo.url))
  
  thumbnail.short_description = 'Photo'
  
  list_display=('car_title','thumbnail','state', 'city','color','model','year','condition','price','is_featured','created_date')
  list_display_links = ('car_title', 'thumbnail','model', 'year',)
  search_fields=('car_title', 'city','year')
  list_filter = ('city',)
  list_editable =('is_featured',)
  

admin.site.register(Car, CarAdmin)