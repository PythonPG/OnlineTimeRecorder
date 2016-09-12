from django.db import models

class Syain(models.Model):
    name = models.CharField(max_length=30)
    corporation_name = models.CharField(max_length=30)
    expire_date = models.DateField(max_length=10)
    job_start = models.FloatField(max_length=6)
    job_end = models.FloatField(max_length=6)
    status = models.CharField(max_length=2)
    min = models.FloatField(max_length=6)
    max = models.FloatField(max_length=6)
    overtime = models.FloatField(max_length=6)
    