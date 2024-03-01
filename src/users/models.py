from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from src.users import managers


class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        STUDENT = 'student'
        TEACHER = 'teacher'

    username = None
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(max_length=9, choices=Roles.choices, default=Roles.STUDENT)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = managers.CustomUserManager()

    def __str__(self):
        return self.email
