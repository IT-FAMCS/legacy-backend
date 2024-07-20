from django.db import models
import datetime
import json

class Event(models.Model):
    short_title = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=50)
    description = models.TextField(default = "Отсутствует")
    dates = models.DateField(default = datetime.date.today)
    preparations = models.TextField(default = "Отсутствует")
    info = models.TextField(default = "Отсутствует")
    FAQ = models.TextField(default = "Отсутствует")
    
    def __str__(self):
        return self.title
class Links(models.Model):
    event = models.ForeignKey(Event, related_name='links', on_delete=models.CASCADE)
    link = models.TextField()
    title = models.TextField()