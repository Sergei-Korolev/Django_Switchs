# Generated by Django 3.1.4 on 2020-12-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switchs', '0011_auto_20201223_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='ip_address_on_port',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
