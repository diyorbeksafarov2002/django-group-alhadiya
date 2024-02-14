from django.db import models


class ModelAla(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=13)
    read = models.BooleanField(default=False)
