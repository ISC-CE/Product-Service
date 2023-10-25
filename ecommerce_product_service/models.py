from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #stock_quantity = models.PositiveIntegerField()
    #image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name