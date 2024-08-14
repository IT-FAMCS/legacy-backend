from django.db import models
from django.conf import settings

class Department(models.Model):
    short_title = models.CharField(max_length=settings.LIMITS("short_title"), unique=True)
    title = models.CharField(max_length=settings.LIMITS("title"))
    description = models.TextField(default = "Отсутсвует")
    structure = models.TextField(default = "Отсутсвует")
    work = models.TextField(default = "Отсутсвует")
    in_events = models.TextField(default = "Отсутсвует")
    FAQ =  models.TextField(default = "Отсутсвует")
    def __str__(self):
        return self.title
class Links(models.Model):
    event = models.ForeignKey(Department, related_name='links', on_delete=models.CASCADE)
    link = models.TextField()
    title = models.TextField()