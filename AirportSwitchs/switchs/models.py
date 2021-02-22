from django.db import models


class Switch(models.Model):
    ip_address = models.GenericIPAddressField(null=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    number_of_ports = models.PositiveSmallIntegerField(blank=True, null=True)
    device_model = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    note = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.ip_address)

class DeviceType(models.Model):
    device_type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.device_type}'


class PortType(models.Model):
    port_type = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.port_type}'


class PortVlan(models.Model):
    port_vlan_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.port_vlan_id}'


class Port(models.Model):
    this_port_belong_to_switch = models.ForeignKey(Switch, null=True, on_delete=models.CASCADE)
    number_port = models.PositiveSmallIntegerField()
    ip_address_on_port = models.GenericIPAddressField(null=True, blank=True)
    device_type = models.ForeignKey(DeviceType, null=True, blank=True, on_delete=models.SET_NULL)
    port_type = models.ForeignKey(PortType, on_delete=models.SET_DEFAULT, default=1)
    port_vlan_id = models.ForeignKey(PortVlan, null=True, on_delete=models.SET_DEFAULT, default=1)


    def __str__(self):
        return '{} port ({}) on {} is {}:{} in {} vlan'.format(self.number_port,
                                                               self.port_type,
                                                               self.this_port_belong_to_switch,
                                                               self.device_type,
                                                               self.ip_address_on_port,
                                                               self.port_vlan_id)
