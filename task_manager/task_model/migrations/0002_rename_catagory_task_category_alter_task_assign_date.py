# Generated by Django 4.2.7 on 2023-12-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_model', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='catagory',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='task',
            name='Assign_date',
            field=models.DateField(),
        ),
    ]