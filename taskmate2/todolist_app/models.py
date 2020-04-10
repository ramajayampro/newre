from django.db import models
from django.utils import timezone
import datetime



# Create your models here.
class Tasklist(models.Model):
    clientname= models.CharField(max_length=30)
    task = models.CharField(max_length=100)
    startdate = models.DateField(default=timezone.now, blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    messagelogs = models.TextField(blank=True, null=True)
    assignee = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    fstatus = models.BooleanField(default=False)

    def __str__(self):
        return self.task + " - Task - " + str(self.fstatus)

