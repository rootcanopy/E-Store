# Generated by Django 3.0.7 on 2020-06-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='item_total',
            field=models.DecimalField(decimal_places=2, default=True, max_digits=6),
        ),
    ]