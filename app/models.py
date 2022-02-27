from django.db import models
from django.utils import timezone


class DO(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField(default="", max_length=2000)
    priority = models.CharField(max_length=50)
    category = models.CharField(max_length=200)
    due_date = models.DateField(default=timezone.now)
    username = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
