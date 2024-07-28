from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    role = models.CharField(verbose_name='role', null=True, blank=True)
    telegram = models.CharField(max_length=25, blank=True, null=True, verbose_name='Телеграм')
    password = models.CharField(blank=True, null=True, verbose_name='Пароль')

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
        db_table = 'User'

    def __str__(self):
        return f'{self.username}: {self.telegram}'
