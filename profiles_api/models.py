# Create your custom default django models here.

from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """manager for user profiles"""

    def create_user(self,email,name,password=None):
        """create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)  #second half is lower case
        user = self.model(email=email,name=name)

        user.set_password(password) #encrypt password
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """create and save a new superuser"""
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """database models for users in the system"""
    email= models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(unique=False)

    objects = UserProfileManager()

    """for authentication overriding the existing """

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """retrieve short name of user"""
        return self.name

    def __str__(self):
        """string representation of user"""
        return self.email
