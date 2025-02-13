from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .manager import UserManager                                                               
# Create your models here.

class User(AbstractBaseUser):
    class UserType(models.TextChoices):
        admin = 'Admin'
        user = 'User'
        guest = 'Guest'

    email=models.EmailField(max_length=225, unique=True, verbose_name=_("Email Address"))
    first_name= models.CharField(max_length=100, verbose_name=_("First Name"))
    last_name= models.CharField(max_length=100, verbose_name=_("Last Name"))
    phone_number = models.CharField(max_length=60, unique=True)
    user_type = models.CharField(max_length=7, choices=UserType.choices, default=UserType.user)
    
    user_id=models.AutoField(primary_key=True)
    username = models.CharField(max_length=60, unique=True) 
    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False) 
    date_joined = models.DateTimeField(auto_now_add= True) 

    USERNAME_FIELD='email'

    REQUIRED_FIELDS=['username', 'first_name', 'last_name', 'phone_number']  

    EMAIL_FIELD = 'email' 

    objects= UserManager() 

    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def has_perm(self, perm, obj=None):
        """Check if the user has a specific permission."""
        # For now, we assume all permissions are granted to superusers
        if self.is_superuser:
            return True
        return False

    def has_module_perms(self, app_label):
        """Check if the user has permissions for the given app."""
        # For now, we assume all permissions are granted to superusers
        if self.is_superuser:
            return True
        return False
        