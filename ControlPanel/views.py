from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.

from ControlPanel.models import ThinClient, Group, ThinClientAttributeValue
from ControlPanel.models import GroupAttributeValue


class IndexView(generic.ListView):
    template_name = 'ControlPanel/index.html'
    context_object_name = 'thinClients_list'

    def get_queryset(self):
        """Return all thinclients."""
        return ThinClient.objects.order_by('dnsName')

def detail(request, thinclient_id):
    thinclient = get_object_or_404(ThinClient, pk=thinclient_id)
    TcAttrib = ThinClientAttributeValue.objects.filter(thinClient=thinclient.id)
    GroupAttrib = GroupAttributeValue.objects.filter(group=thinclient.group.id)
    Attributes = {}
    for attrib in GroupAttrib:
        Attributes[attrib.attribute.name]=attrib.value
    for attrib in TcAttrib:
        Attributes[attrib.attribute.name]=attrib.value

    return render(request, 'ControlPanel/detail.html',
                    {
                        'thinclient': thinclient,
                        'TcAttrib': TcAttrib,
                        'GroupAttrib': GroupAttrib,
                        'Attributes': Attributes,
                        }
                )

def groupIndex(request, thinclient_id):
    thinclient = get_object_or_404(ThinClient, pk=thinclient_id)
    TcAttrib = ThinClientAttributeValue.objects.filter(thinClient=thinclient.id)
    GroupAttrib = GroupAttributeValue.objects.filter(group=thinclient.group.id)
    Attributes = {}
    for attrib in GroupAttrib:
        Attributes[attrib.attribute.name]=attrib.value
    for attrib in TcAttrib:
        Attributes[attrib.attribute.name]=attrib.value

    return render(request, 'ControlPanel/detail.html',
                    {
                        'thinclient': thinclient,
                        'TcAttrib': TcAttrib,
                        'GroupAttrib': GroupAttrib,
                        'Attributes': Attributes,
                        }
                )