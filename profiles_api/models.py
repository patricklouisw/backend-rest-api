from statistics import mode
from unicodedata import name
from django.db import models
# Standard base classes to customize the default Django user model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Custom User Profile Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""

        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a newsuperuser with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        return user



# UserModel
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Custom User Model for users in the system"""
    # Various fields in our model
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Link to Model Manager
    objects = UserProfileManager()

    # Required fields
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self) -> str:
        """Return string representation of our user"""
        return self.email

