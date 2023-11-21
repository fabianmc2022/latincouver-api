# Generated by Django 4.2.4 on 2023-11-21 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0009_alter_volunteerhour_time_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(default='default_pic.png', upload_to='static/images/employees'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='photo',
            field=models.ImageField(default='default_pic.png', upload_to='static/images/volunteers'),
        ),
        migrations.AlterField(
            model_name='volunteerhour',
            name='time_in',
            field=models.TimeField(default='13:06:20'),
        ),
        migrations.AlterField(
            model_name='volunteerhour',
            name='time_out',
            field=models.TimeField(default='13:06:20'),
        ),
    ]
