# Generated by Django 4.2.7 on 2023-12-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0002_alter_cart_options_alter_cartitems_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]