# Generated by Django 3.2 on 2022-01-29 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_producthasorder_deliveryboy'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='pincode',
            field=models.CharField(default=None, max_length=6),
            preserve_default=False,
        ),
    ]