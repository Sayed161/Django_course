# Generated by Django 4.2.7 on 2023-12-16 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_model', '0008_order_already_purchased'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity_purchased',
            field=models.IntegerField(default=1),
        ),
    ]
