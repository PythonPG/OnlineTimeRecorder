from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, phone, password, name_sei, name_namae, master=False):
        user = self.model(phone=phone)
        user.name_sei = name_sei
        user.name_namae = name_namae
        user.master = master
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, phone, password):
        self.create_user(phone, password, 'sei', 'name', True)

class User(AbstractBaseUser):
    master = models.BooleanField(default=False)
    secret = models.BooleanField(default=False)
    # email = models.EmailField(max_length=128, unique=True)
    phone = models.CharField(max_length=13, default=None, null=True, unique=True)
    # post_code = models.CharField(max_length=10, default=None, null=True)
    # address = models.CharField(max_length=128, default=None, null=True)
    name_sei = models.CharField(max_length=30,default=None, null=True)
    name_namae = models.CharField(max_length=30,default=None, null=True)
    # birthday = models.DateField(default=None, null=True)

    USERNAME_FIELD = 'phone'
    # USERNAME_FIELD = 'email'

    objects = MyUserManager()

class TimeCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField()
    leave_time = models.DateTimeField()    
    status = models.CharField(max_length=2,default='0')

class DemoUser(models.Model):
    phone = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    name_sei = models.CharField(max_length=30)
    name_namae = models.CharField(max_length=30)
    
