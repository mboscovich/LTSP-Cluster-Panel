from django.shortcuts import render

# Create your views here.

from ControlPanel.models import ThinClient


def index(request):
    thinClients_list = ThinClient.objects.order_by('dnsName')[:5]
    context = {'thinClients_list': thinClients_list}
    return render(request, 'ControlPanel/index.html', context)