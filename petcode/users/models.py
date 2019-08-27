from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractUser
)
from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=225,
        unique=True
    )
    username = models.CharField(max_length=40, unique=False, default='')
    # first_name = models.TextField()
    # last_name = models.TextField()
    # active = models.BooleanField(default=True)
    # staff = models.BooleanField(default=False)
    # admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #email and password are required by default
    objects = UserManager()
    
    def __str__(self):
        return self.email

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     return self.staff

    # @property
    # def is_admin(self):
    #     "Is the user a admin member?"
    #     return self.admin

    # @property
    # def is_active(self):
    #     "Is the user active?"
    #     return self.active

