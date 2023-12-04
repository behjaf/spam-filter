# models.py

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=255, blank=True, null=True)
    # other fields...

    def __str__(self):
        return self.name

    # other fields...

    def __str__(self):
        return self.name
