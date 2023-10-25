from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #stock_quantity = models.PositiveIntegerField()
    #image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product_id = models.IntegerField()
    image_url = models.URLField()

    def __str__(self):
        return self.name
    
class ProductInventory(models.Model):
    product_id = models.IntegerField()
    sku = models.TextField()
    stock_quantity = models.PositiveIntegerField()
    reorder_threshold = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class ProductManufacturers(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField()

    def __str__(self):
        return self.name