from django.contrib import admin
from email.headerregistry import Group
from django.contrib import admin
from.models import Vehicles,customer,staff
from django.contrib.auth.models import Group,User

# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
     list_display=['name','exshowroomprice','available','created','updated']
     list_editable=['exshowroomprice','available']
     list_per_page=20
    # prepopulated_fields={'slug':('name',)}
admin.site.register(Vehicles,VehicleAdmin)

class customerAdmin(admin.ModelAdmin):
    list_display=['username','email','phone']
    exclude=['password']
    def has_add_permission(self,request,obj= None):
        return False
    def has_change_permission(self,request,obj= None):
        return False
    def has_delete_permission(self,request,obj= None):
        return False        
    verbose_name_plural="customers"
admin.site.register(customer,customerAdmin)


class staffAdmin(admin.ModelAdmin):
    list_display=('phone','username')
    # list_display_links=['username']
    # exclude=('password',)
    list_editable=['username']
    
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

    verbose_name_plural = "Staff Details"
admin.site.register(staff,staffAdmin)

# class staffloginAdmin(admin.ModelAdmin):
#     list_display=['username']
#     exclude=('password',)
#     def has_add_permission(self, request, obj=None):
#         return False
#     # def has_change_permission(self, request, obj=None):
#     #     return False

#     def has_delete_permission(self, request, obj=None):
#         return False
#     verbose_name_plural = "Staff Login Details"
# admin.site.register(staff,staffloginAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)