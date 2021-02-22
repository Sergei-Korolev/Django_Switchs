# Generated by Django 3.1.4 on 2021-01-21 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('switchs', '0019_auto_20210121_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_type', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PortVlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_vlan_id', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='port',
            name='port_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='switchs.porttype'),
        ),
        migrations.AddField(
            model_name='port',
            name='port_vlan_id',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='switchs.portvlan'),
        ),
    ]