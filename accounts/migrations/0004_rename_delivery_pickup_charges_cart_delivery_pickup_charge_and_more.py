# Generated by Django 4.0.2 on 2022-03-02 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_user_cart_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='delivery_pickup_charges',
            new_name='delivery_pickup_charge',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='rent_amount',
            new_name='rent_price',
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
