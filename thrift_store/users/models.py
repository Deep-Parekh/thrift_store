from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
# from django.utils import timezone

from .managers import CustomUserManager

class CustomUser(AbstractUser, PermissionsMixin):
    #username =  models.CharField(_('username'), max_length=20, blank=False, unique=True)
    #first_name = models.CharField(_('first name'), max_length=50, blank=True)
    #last_name = models.CharField(_('last name'), max_length=50, blank=True)
    #email = models.EmailField(_('email address'), unique=False)
    #password = models.CharField(max_length=128, verbose_name='password')
    contact_no = models.CharField(max_length=20, blank=False, default='')
    location = models.CharField(max_length=100, blank=False, default='')
    # products_listed
    # wishlist
    # cart
    date_joined = models.DateTimeField(auto_now_add=True, blank=True)

    is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
