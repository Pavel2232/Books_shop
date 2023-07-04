from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from user.manager import UserManager


class Author(AbstractBaseUser):
    username = models.CharField(max_length=55, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.full_name
