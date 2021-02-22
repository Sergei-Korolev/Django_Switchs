# Generated by Django 3.1.4 on 2020-12-23 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('switchs', '0006_auto_20201223_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='switch',
            name='ip_address',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='switch',
            name='quantity_ports',
            field=models.IntegerField(blank=True),
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_port', models.IntegerField(blank=True)),
                ('device_ip_address', models.GenericIPAddressField(null=True)),
                ('device_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='switchs.devicetype')),
            ],
        ),
    ]