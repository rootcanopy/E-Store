# Generated by Django 3.0.7 on 2020-10-29 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_orderitem_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='town_city',
            new_name='town_or_city',
        ),
    ]
