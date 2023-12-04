from .managers import CustomUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from PIL import Image
from django.urls import reverse

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, max_length=255)
    username = models.CharField(_('username'), unique=True, max_length=100)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['date_joined', ]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_absolute_url(self):
         return reverse('user-detail', args=[str(self.id)])
    
    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    objects = CustomUserManager()