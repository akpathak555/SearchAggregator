from django.db import models

# Create your models here.

class ShopCluesProduct(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    url = models.CharField(max_length=250, null=True, blank=True)
    image = models.CharField(max_length=5000, null=True, blank=True)
    price = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class PaytmProduct(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    url = models.CharField(max_length=250, null=True, blank=True)
    image = models.CharField(max_length=5000, null=True, blank=True)
    price = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class TataProduct(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    url = models.CharField(max_length=250, null=True, blank=True)
    image = models.CharField(max_length=5000, null=True, blank=True)
    price = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.name)

