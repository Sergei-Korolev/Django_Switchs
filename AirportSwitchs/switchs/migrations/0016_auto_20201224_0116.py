# Generated by Django 3.1.4 on 2020-12-23 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switchs', '0015_auto_20201224_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='number_port',
            field=models.PositiveSmallIntegerField(),
        ),
    ]