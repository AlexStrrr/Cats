from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Cat(models.Model):
    abb = models.CharField(max_length=4)
    name = models.CharField(max_length=30, verbose_name='Breed')
    temperament = models.CharField(max_length=150, verbose_name='Temperament')
    description = models.CharField(max_length=350, verbose_name='Description')
    wikipedia_url = models.CharField(max_length=150, verbose_name='Url')
    image = models.ImageField(upload_to='cat_images/', default='Aegean_Island_Cat.jpg')


class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='about_users',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='about_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )



