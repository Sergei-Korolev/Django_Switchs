from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Switch, Port


@login_required(login_url='/admin')
def index(request):
    switchs = Switch.objects.order_by('ip_address')
    context = {'switchs': switchs}
    return render(request, 'switchs/index.html', context)


@login_required(login_url='/admin')
def detail(request, switch_id):
    switch = get_object_or_404(Switch, pk=switch_id)
    switch_ports = Port.objects.filter(this_port_belong_to_switch=switch_id).order_by('number_port')
    used_ports = len([port for port in switch_ports if port.ip_address_on_port])
    free_ports = switch.number_of_ports - used_ports
    context = {
        'switch': switch,
        'used_ports': used_ports,
        'free_ports': free_ports,
        'switch_ports': switch_ports,
    }
    #context = {'switch': switch, 'used_ports': used_ports, 'free_ports': free_ports}
    return render(request, 'switchs/detail.html', context)
