from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta


def get_activation_key_expiration_date():
    return now() + timedelta(days=2)


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users', blank=True, verbose_name='Аватарка')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(
        default=get_activation_key_expiration_date
    )

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
