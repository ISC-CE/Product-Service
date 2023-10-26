from django.db import models
import random

def generate_unique_product_id():
    while True:
        # Generate a potential product_id, e.g., a random integer
        potential_product_id = random.randint(1000, 9999)  # Adjust the range as needed

        # Check if the generated product_id is already in use
        if not Product.objects.filter(product_id=potential_product_id).exists():
            return potential_product_id

class Product(models.Model):
    #product_id = models.AutoField()
    product_name = models.CharField(max_length=255)
    product_description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey('ProductManufacturer', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

class ProductCategory(models.Model):
    #category_id = models.AutoField()
    category_name = models.CharField(max_length=100)
    category_description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

class ProductManufacturer(models.Model):
    #manufacturer_id = models.AutoField()
    manufacturer_name = models.CharField(max_length=100)
    manufacturer_description = models.TextField(null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.manufacturer_name

class ProductImage(models.Model):
    #image_id = models.AutoField(primary_key = True, default=generate_unique_product_id, unique=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProductInventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()
    reorder_threshold = models.PositiveIntegerField()

    

class ProductReview(models.Model):
    #review_id = models.AutoField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    review_text = models.TextField(null=True, blank=True)
    review_date = models.DateTimeField(auto_now_add=True)

  
class ProductVariation(models.Model):
    #variation_id = models.AutoField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations_name = models.CharField(max_length=100)
    price_adjustment = models.DecimalField(max_digits=10, decimal_places=2)
    SKU = models.CharField(max_length=50)
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.variations_name

class ProductDiscount(models.Model):
    #discount_id = models.AutoField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    
class ProductRecommendation(models.Model):
    #recommendation_id = models.AutoField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    