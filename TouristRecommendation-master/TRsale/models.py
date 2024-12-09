from django.db import models

# Create your models here.
class DmSale(models.Model):
    cityname = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    salesVolume = models.IntegerField()
    introduce = models.CharField(max_length=64)
    isFree = models.CharField(max_length=64)
    specificLocation = models.TextField()

class DmFree(models.Model):
    cityname = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    salesVolume = models.IntegerField()
    introduce = models.CharField(max_length=64)
    isFree = models.CharField(max_length=64)
    specificLocation = models.TextField()

class All(models.Model):
    cityname = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    salesVolume = models.IntegerField()
    introduce = models.CharField(max_length=64)
    isFree = models.CharField(max_length=64)
    specificLocation = models.TextField()

class DmShanghai(models.Model):
    cityname = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    salesVolume = models.IntegerField()
    introduce = models.CharField(max_length=64)
    isFree = models.CharField(max_length=64)
    specificLocation = models.TextField()

class DmGuangdong(models.Model):
    cityname = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    salesVolume = models.IntegerField()
    introduce = models.CharField(max_length=64)
    isFree = models.CharField(max_length=64)
    specificLocation = models.TextField()

class DmYunnan(models.Model):
    cityname = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    salesVolume = models.IntegerField()
    introduce = models.CharField(max_length=64)
    isFree = models.CharField(max_length=64)
    specificLocation = models.TextField()

class DmXinjiang(models.Model):
    cityname = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    salesVolume = models.IntegerField()
    introduce = models.CharField(max_length=64)
    isFree = models.CharField(max_length=64)
    specificLocation = models.TextField()
