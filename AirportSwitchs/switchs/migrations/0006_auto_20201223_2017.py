# Generated by Django 3.1.4 on 2020-12-23 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switchs', '0005_auto_20201223_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='device_type',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
