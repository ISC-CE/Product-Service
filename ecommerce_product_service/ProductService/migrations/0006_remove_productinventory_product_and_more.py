# Generated by Django 4.2.6 on 2023-11-03 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductService', '0005_remove_productdiscount_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinventory',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='product_inventory',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ProductService.productinventory'),
        ),
    ]
