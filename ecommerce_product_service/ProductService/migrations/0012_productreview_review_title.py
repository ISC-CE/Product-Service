# Generated by Django 4.2.6 on 2023-11-05 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductService', '0011_rename_user_productreview_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='review_title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
