# Generated by Django 4.2.6 on 2023-11-05 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductService', '0010_productreview_user_alter_product_stock_quantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productreview',
            old_name='user',
            new_name='user_id',
        ),
    ]
