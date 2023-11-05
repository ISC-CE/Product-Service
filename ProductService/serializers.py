from rest_framework import serializers
from .models import Product
from .models import ProductImage
#from .models import ProductInventory
from .models import ProductReview

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        #fields = ('product_name', 'product_description', 'price',  'stock_quantity', 'created_at', 'updated_at', 'product_inventory')
        #exclude = ('product_inventory',)  # Exclude the 'product_inventory' field
    #stock_quantity = serializers.IntegerField()

    #product_inventory = serializers.HiddenField(default=None)

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'

'''class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = '__all__'
'''


