from django.db import models

class Information(models.Model):
    short_title = models.CharField(max_length = 10, unique=True)
    title = models.TextField()
    info = models.TextField()