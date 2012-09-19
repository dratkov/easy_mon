# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from profile.fields import AutoOneToOneField


class Profile(models.Model):
    user = AutoOneToOneField(User, related_name='profile', verbose_name=('User'), primary_key=True)
    birthday = models.DateField(verbose_name="День рождения")
# Create your models here.
