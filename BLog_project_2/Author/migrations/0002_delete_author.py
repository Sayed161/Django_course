# Generated by Django 4.2.7 on 2023-12-12 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_author'),
        ('Author', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='author',
        ),
    ]
