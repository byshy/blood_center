# Generated by Django 3.0.3 on 2020-04-23 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200423_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'other')]),
        ),
    ]
