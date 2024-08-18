from django.db import models
from django.conf import settings
import datetime
import json

class Event(models.Model):
    short_title = models.CharField(max_length=settings.LIMITS("short_title"), unique=True)
    title = models.CharField(max_length=settings.LIMITS("title"))
    description = models.TextField(default = "Отсутствует")
    dates = models.CharField(default = datetime.date.today, max_length=150)
    preparations = models.TextField(default = "Отсутствует")
    info = models.TextField(default = "Отсутствует")
    FAQ = models.TextField(default = "Отсутствует")
    
    def __str__(self):
        return self.title
class Links(models.Model):
    event = models.ForeignKey(Event, related_name='links', on_delete=models.CASCADE)
    link = models.TextField()
    title = models.TextField()