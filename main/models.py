from django.db import models

# Create your models here.

class Item(models.Model):
    count = models.TextField(default="0000")
    name = models.TextField(default="name")
    status = models.BooleanField(default=False)
