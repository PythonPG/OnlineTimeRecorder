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
    phone = models.CharField(max_length=13,default='000-0000-0000', unique=True)
    # password = models.CharField(max_length=30,default='sei-mei')
    name_sei = models.CharField(max_length=30,default='sei')
    name_namae = models.CharField(max_length=30,default='namae')
    
    USERNAME_FIELD = 'phone'

    objects = MyUserManager()

class TimeCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField()
    leave_time = models.DateTimeField()    
    status = models.CharField(max_length=2,default='0')
