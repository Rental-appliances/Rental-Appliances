# Generated by Django 3.2 on 2022-02-08 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_deliverypickup_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producthasorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='accounts.order'),
        ),
    ]
