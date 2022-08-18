from django.db import models

# Create your models here.


class otModel(models.Model):
    sno1 = models.IntegerField()
    dataStream = models.CharField(max_length=30)