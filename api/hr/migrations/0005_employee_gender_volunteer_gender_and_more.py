# Generated by Django 4.2.4 on 2023-10-05 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_departments_remove_contractor_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female'), (3, 'Others')], null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female'), (3, 'Others')], null=True),
        ),
        migrations.AddField(
            model_name='volunteerapplication',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerhour',
            name='time_in',
            field=models.TimeField(default='08:33:30'),
        ),
        migrations.AlterField(
            model_name='volunteerhour',
            name='time_out',
            field=models.TimeField(default='08:33:30'),
        ),
    ]
