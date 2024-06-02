from django.contrib import admin
from .models import *
# Register your models here.
class CatrgoryAdmin(admin.ModelAdmin):
    list_display=['name','image','description','created_at']
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','created_at',"vendor"]
admin.site.register(Catagory,CatrgoryAdmin)
admin.site.register(Products,ProductAdmin)