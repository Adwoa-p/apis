from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .manager import UserManager
# Create your models here.

class User(AbstractBaseUser):
    email=models.EmailField(max_length=225, unique=True, verbose_name=_("Email Address"))
    first_name= models.CharField(max_length=100, verbose_name=_("First Name"))
    last_name= models.CharField(max_length=100, verbose_name=_("Last Name"))
    phone_number = models.CharField(max_length=60, unique=True)

    username = models.CharField(max_length=60, unique=True) # Required
    is_active = models.BooleanField(default=True) # Required - user can login
    is_staff = models.BooleanField(default=False) # Required
    is_superuser = models.BooleanField(default=False) # Required
    is_admin = models.IntegerField(default=0) # Required
    date_joined = models.DateTimeField(auto_now_add= True) # Required

    USERNAME_FIELD='email'

    REQUIRED_FIELDS=['username', 'firstname', 'lastname', 'phone_number']  

    EMAIL_FIELD = 'email' 

    objects= UserManager() 

    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
        