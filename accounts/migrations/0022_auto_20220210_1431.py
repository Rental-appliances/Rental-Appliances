# Generated by Django 3.2 on 2022-02-10 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20220210_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subcategory_idcategory',
            field=models.ForeignKey(blank=True, db_column='subcategory_idcategory', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='product',
            field=models.ForeignKey(blank=True, db_column='product', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.product'),
        ),
    ]
