from django.contrib import admin
from email.headerregistry import Group
from django.contrib import admin
<<<<<<< HEAD
from.models import Vehicles,customer,staff,Bank,Productgallery
=======
from.models import Vehicles,customer,staff,Bank
>>>>>>> dbe8adc81f270ff8faf1403c5d073de8decd1232
from django.contrib.auth.models import Group,User

# Register your models here.

class ProductGalleryInline(admin.TabularInline):
    model=Productgallery
    extra=1


class VehicleAdmin(admin.ModelAdmin):
     list_display=['name','exshowroomprice','available','created','updated']
     list_editable=['exshowroomprice','available']
     list_per_page=20
    #  prepopulated_fields={'slug':('name',)}
     inlines=[ProductGalleryInline]

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

class BankAdmin(admin.ModelAdmin):
     list_display=['name','interest_rate']
     
    # prepopulated_fields={'slug':('name',)}
admin.site.register(Bank,BankAdmin)


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