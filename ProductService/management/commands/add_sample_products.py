from django.core.management.base import BaseCommand
from ProductService.models import Product
from decimal import Decimal
from datetime import datetime

class Command(BaseCommand):
    help = 'Add sample electronic products to the database'

    def handle(self, *args, **kwargs):
        # Create sample electronic products
        product1 = Product(
            product_name='Smartphone X1',
            product_description='A high-end smartphone',
            price=Decimal('699.99'),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        product1.save()

        product2 = Product(
            product_name='Laptop L2',
            product_description='A powerful laptop for productivity',
            price=Decimal('1299.99'),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        product2.save()

        self.stdout.write(self.style.SUCCESS('Sample electronic products added successfully.'))
