# Generated by Django 3.1.4 on 2020-12-23 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switchs', '0014_auto_20201224_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='number_port',
            field=models.PositiveSmallIntegerField(unique=True),
        ),
    ]
