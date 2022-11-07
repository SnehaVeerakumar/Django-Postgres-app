from django.db import models

class GeeksforGeeks(models.Model):
    fullname = models.CharField(max_length=200)
    mobile_number = models.IntegerField()