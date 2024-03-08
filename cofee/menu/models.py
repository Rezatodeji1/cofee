from django.db import models
class barcold(models.Model):
    status = (('df','draft'),('pb','published'))
    name = models.CharField(max_length=50)
    note = models.CharField(max_length=255)
    price = models.CharField(max_length=20000000)
    status = models.CharField(max_length=2,choices=status,default='df')

