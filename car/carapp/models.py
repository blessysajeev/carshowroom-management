from django.db import models 




# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
# Create your models here.

class customer(models.Model):
    username = models.CharField(max_length=100,unique=True)
    phone = models.CharField(max_length=15,unique=True,null=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=250)
    
    class Meta:
        ordering=('username',)
        verbose_name='customer'
        verbose_name_plural='customers'

    def _str_(self):
        return '{}'.format(self.username)

class Vehicles(models.Model):
    name=models.CharField(max_length=250,unique=True)
    #slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    exshowroomprice=models.DecimalField(max_digits=10,decimal_places=2,default=True)
    fueltype=models.TextField(blank=True)
    fuelfuelcapacity=models.CharField(max_length=200,blank=True)
    fueltype=models.TextField(blank=True)
    image = models.ImageField(upload_to='product',blank=True)
    image1=models.ImageField(upload_to='product',blank=True)
    image2=models.ImageField(upload_to='product',blank=True)
    image3=models.ImageField(upload_to='product',blank=True)
    image4=models.ImageField(upload_to='product',blank=True)
    image5=models.ImageField(upload_to='product',blank=True)
    image6=models.ImageField(upload_to='product',blank=True)
    brochure=models.FileField(upload_to='product',blank=True)
    # stock=models.CharField(max_length=250,default="null")
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        verbose_name='Vehicle'
        verbose_name_plural='Vehicles'

    def _str_(self):
        return '{}'.format(self.name)


class test_drive(models.Model):
   
    username = models.ForeignKey(customer, null=True, on_delete=models.CASCADE,related_name="customername")
    venue = models.CharField(max_length=100,null=True)
    carmodel = models.CharField(max_length=100,null=True)
    Contact = models.BigIntegerField(default=0)
    Email = models.EmailField(max_length=100,null=True)
    testdate = models.DateField(null=True, auto_now_add=False)
    testtime = models.TimeField(null=True, blank=True)


    class Meta:
        ordering=('carmodel',)
        verbose_name='test_drive'
        verbose_name_plural='test_drive'

    def _str_(self):
        return '{}'.format(self.carmodel)
    def __str__(self):
        return self.username.username   


class showroom_visit(models.Model):
   
    username = models.ForeignKey(customer, null=True, on_delete=models.CASCADE,related_name="visitername")
    carmodel = models.CharField(max_length=100,null=True)
    Contact = models.BigIntegerField(default=0)
    Email = models.EmailField(max_length=100,null=True)
    visitdate = models.DateField(null=True, auto_now_add=False)
    visittime = models.TimeField(null=True, blank=True)


    class Meta:
        ordering=('carmodel',)
        verbose_name='showroom_visit'
        verbose_name_plural='showroom_visit'

    def _str_(self):
        return '{}'.format(self.carmodel)
    def __str__(self):
        return self.username.username   



class staff(models.Model):
    username = models.CharField(max_length=100,unique=True)
    phone = models.CharField(max_length=15,unique=True,null=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=250)
    
    class Meta:
        ordering=('username',)
        verbose_name='staff'
        verbose_name_plural='staffs'

    def _str_(self):
        return '{}'.format(self.username)



class car(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    year = models.IntegerField()
    kms_driven = models.IntegerField()
    fuel_type = models.CharField(max_length=50)

class Bank(models.Model):
    name = models.CharField(max_length=255)
    interest_rate = models.FloatField()

class CarLoan(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    loan_amount = models.FloatField()
    loan_tenure = models.IntegerField()
    interest_rate = models.FloatField()
    emi_amount = models.FloatField()

    
# class MyAccountManager(BaseUserManager):
#     def create_user(self,username,phonenumber,email,password=None):
        
#         if not email:
#             raise ValueError('User must have an email address')

#         if not username:
#             raise ValueError('User must have an username')

#         user = self.model(
#             email = self.normalize_email(email),
#             username = username,
#             phonenumber = phonenumber,
            
           
            

#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user


# # class MyAccountManager(BaseUserManager):
# #     def create_user(self,username, email, password=None):
# #         if not email:
# #             raise ValueError('User must have an email address')

# #         if not username:
# #             raise ValueError('User must have an username')

# #         user = self.model(
# #             email = self.normalize_email(email),
# #             username = username,
            
# #         )

# #         user.set_password(password)
# #         user.save(using=self._db)
# #         return user


    
#     def create_superuser(self,username,password,email,**extra_fields):
#         user = self.create_user(
#             email = self.normalize_email(email),
#             username = username,
#             password = password, **extra_fields
#             # first_name = first_name,
#             # last_name = last_name,
#         )
#         user.is_admin = True
#         user.is_active = True
#         user.is_staff = True
#         user.is_superadmin = True
#         user.save(using=self._db)
#         return user


 
# class Account(AbstractBaseUser,PermissionsMixin):
#     # status_choices=(('Approved','Approved'),('Pending','Pending'), ('None','None'))
#     # role_choices=(('is_admin','is_admin'),('is_customer','is_customer'),('is_staff','is_staff'))
    


#     id            = models.AutoField(primary_key=True)
#     username      = models.CharField(max_length=100, default='')
#     phonenumber   = models.BigIntegerField(default=0)
#     email         = models.EmailField(max_length=100, unique=True)
#     # role          = models.CharField(max_length=100,choices=role_choices)
    
    

#     # required
#     date_joined     = models.DateTimeField(auto_now_add=True)
#     last_login      = models.DateTimeField(auto_now_add=True)
#     is_admin        = models.BooleanField(default=False)
#     # is_customer     = models.BooleanField(default=False)
#     # is_staff        = models.BooleanField(default=False)
    
    

    
#     is_active       = models.BooleanField(default=True)
#     is_superadmin   = models.BooleanField(default=False)
#     # is_staff      = models.BooleanField(default=False) 
#     # is_superadmin     = models.BooleanField(default=False)  
   

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username','phonenumber', 'address','city','pincode','is_customer','is_staff']
#     # REQUIRED_FIELDS = [,'password']



#     objects = MyAccountManager()

#     # def full_name(self):
#     #     return f'{self.first_name} {self.last_name}'

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, add_label):
#         return True