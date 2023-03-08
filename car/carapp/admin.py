from django.contrib import admin
from email.headerregistry import Group
from django.contrib import admin
from.models import Vehicles
from django.contrib.auth.models import Group,User

# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
     list_display=['name','exshowroomprice','available','created','updated']
     list_editable=['exshowroomprice','available']
     list_per_page=20
    # prepopulated_fields={'slug':('name',)}
admin.site.register(Vehicles,VehicleAdmin)