from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    article = models.IntegerField(null=True)
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.name
