# Generated by Django 4.2.7 on 2023-12-07 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='albumsform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Album_name', models.CharField(max_length=80)),
                ('Album_release_date', models.DateField()),
                ('Rating', models.CharField(max_length=20)),
            ],
        ),
    ]
