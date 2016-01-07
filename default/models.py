from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Todolist(models.Model):
    #id=models.CharField(max_length=1000)
    content = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=8)

class Peoson(models.Model):
    name = models.CharField(max_length=16)
    phonenum = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    qq = models.CharField(max_length=20)