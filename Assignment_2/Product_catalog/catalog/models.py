from django.db import models

# Create your models here.
class Catalog(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock_quantity = models.IntegerField()

    def __str__(self):
        return self.name