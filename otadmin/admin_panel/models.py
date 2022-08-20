from django.db import models

# Create your models here.
class otData(models.Model):
    sno = models.IntegerField()
    dataStream = models.CharField(max_length=255)

