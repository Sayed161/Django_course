# Generated by Django 4.2.7 on 2023-12-16 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_model', '0007_remove_order_already_purchased_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='already_purchased',
            field=models.BooleanField(default=False),
        ),
    ]