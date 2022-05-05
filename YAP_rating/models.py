from django.db import models

class YAP_rating(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()