from django.db import models
from django.conf import settings

class Information(models.Model):
    short_title = models.CharField(max_length=settings.LIMITS("short_title"), unique=True)
    title = models.CharField(max_length=settings.LIMITS("title"))
    info = models.TextField()