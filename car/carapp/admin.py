from django.contrib import admin
from email.headerregistry import Group
from django.contrib import admin

from.models import Vehicles,customer,staff,Bank,Productgallery,test_drive,showroom_visit,Payments
from.models import Vehicles,customer,staff,Bank
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

class test_driveAdmin(admin.ModelAdmin):
    list_display=['username','venue','carmodel','testdate','testtime']
    def has_add_permission(self,request,obj= None):
        return False
    def has_change_permission(self,request,obj= None):
        return False
    def has_delete_permission(self,request,obj= None):
        return False        
    verbose_name_plural="testdrive"
admin.site.register(test_drive,test_driveAdmin)

class showroom_visitAdmin(admin.ModelAdmin):
    list_display=['username','carmodel','visitdate','visittime']
    def has_add_permission(self,request,obj= None):
        return False
    def has_change_permission(self,request,obj= None):
        return False
    def has_delete_permission(self,request,obj= None):
        return False        
    verbose_name_plural="showroomvisit"
admin.site.register(showroom_visit,showroom_visitAdmin)

class staffAdmin(admin.ModelAdmin):
    list_display=['username','email','phone']

    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

    verbose_name_plural = "Staff Details"

    actions = ['assign_customers']

    def assign_customers(self, request, queryset):
        selected_staff = queryset.first()
        customers = customer.objects.all()
        for c in customers:
            if not c.staff_assigned:
                c.staff_assigned = selected_staff
                c.save()
        self.message_user(request, f'Successfully assigned customers to {selected_staff.username}')

    assign_customers.short_description = "Assign selected staff to all unassigned customers"

admin.site.register(staff,staffAdmin)


class BankAdmin(admin.ModelAdmin):
     list_display=['name','interest_rate']
     
    # prepopulated_fields={'slug':('name',)}
admin.site.register(Bank,BankAdmin)

class PaymentAdmin(admin.ModelAdmin):
     list_display=['user','amount']
     
    # prepopulated_fields={'slug':('name',)}
admin.site.register(Payments,PaymentAdmin)
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