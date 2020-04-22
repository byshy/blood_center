# Generated by Django 3.0.3 on 2020-04-22 10:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_history_blood_center_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date-time created'),
        ),
    ]
