from django.db import models

# Create your models here.
class Profile(models.Model):
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  phone = models.CharField(max_length=200)
  summary = models.TextField(max_length=200)
  degree = models.CharField(max_length=300)
  school = models.CharField(max_length=300)
  university = models.CharField(max_length=300)
  previous_work = models.TextField(max_length=300)
  skills = models.TextField(max_length=300)
