# Generated by Django 3.1.4 on 2020-12-23 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switchs', '0008_auto_20201223_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='number_port',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='quantity_ports',
            field=models.SmallIntegerField(blank=True),
        ),
    ]