from django.contrib.auth.models import AbstractUser
from apps.core import translations


class User(AbstractUser):
    class Meta:
        verbose_name = translations.USER
        verbose_name_plural = translations.USERS

    def __str__(self):
        if self.get_full_name():
            return f'{self.get_username()} ({self.get_full_name()})'
        else:
            return self.get_username()
