# Generated by Django 4.2.7 on 2023-12-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
