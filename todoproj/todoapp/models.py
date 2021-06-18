from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Activity(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "activities"
