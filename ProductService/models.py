from django.db import models
import random



class Product(models.Model):
    #product_id = models.AutoField()
    product_name = models.CharField(max_length=255)
    #product_inventory = models.OneToOneField(ProductInventory, on_delete=models.CASCADE, related_name='product')
    #product_inventory = models.ForeignKey(ProductInventory, on_delete=models.CASCADE, null=True, blank=True)
    product_description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

'''class ProductInventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True)
    stock_quantity = models.PositiveIntegerField()
    reorder_threshold = models.PositiveIntegerField()
'''
class ProductImage(models.Model):
    #image_id = models.AutoField(primary_key = True, default=generate_unique_product_id, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class ProductReview(models.Model):
    #review_id = models.AutoField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.PositiveIntegerField(null=True, blank=True)
    rating = models.PositiveIntegerField()
    review_title = models.TextField(null=True, blank=True)
    review_text = models.TextField(null=True, blank=True)
    review_date = models.DateTimeField(auto_now=True)

  
