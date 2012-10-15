# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from profile.fields import AutoOneToOneField


class Profile(models.Model):
    user = AutoOneToOneField(User, related_name='profile', verbose_name=('User'), primary_key=True)
    summa = models.SmallIntegerField(verbose_name="Сумма на счету")
# Create your models here.
