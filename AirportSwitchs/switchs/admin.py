from django.contrib import admin
from .models import Switch, Port, DeviceType, PortType, PortVlan


class PortInline(admin.TabularInline):
    model = Port
    extra = 0


class SwitchPorts(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['ip_address']}),
        ('Info', {'fields': ['location', 'device_model', 'number_of_ports', 'image', 'note']}),
    ]
    inlines = [PortInline]

admin.site.register(Switch, SwitchPorts)
admin.site.register(DeviceType)
admin.site.register(Port)
admin.site.register(PortType)
admin.site.register(PortVlan)