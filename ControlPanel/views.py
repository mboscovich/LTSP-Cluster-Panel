from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.

from ControlPanel.models import ThinClient, Group, ThinClientAttributeValue
from ControlPanel.models import GroupAttributeValue, Attribute


class thinClientsIndex(generic.ListView):
    template_name = 'ControlPanel/thinClientsIndex.html'
    context_object_name = 'thinClients_list'

    def get_queryset(self):
        """Return all thinclients."""
        return ThinClient.objects.order_by('dnsName')


class groupsIndex(generic.ListView):
    template_name = 'ControlPanel/groupsIndex.html'
    context_object_name = 'groups_list'

    def get_queryset(self):
        """Return all group."""
        return Group.objects.order_by('name')


class attributesIndex(generic.ListView):
    template_name = 'ControlPanel/attributesIndex.html'
    context_object_name = 'attributes_list'

    def get_queryset(self):
        """Return all attibutes."""
        return Attribute.objects.order_by('name')


def thinClientDetail(request, thinclient_id):
    thinclient = get_object_or_404(ThinClient, pk=thinclient_id)
    TcAttrib = ThinClientAttributeValue.objects.filter(thinClient=thinclient.id)
    GroupAttrib = GroupAttributeValue.objects.filter(group=thinclient.group.id)
    Attributes = {}
    for attrib in GroupAttrib:
        Attributes[attrib.attribute.name]=attrib.value
    for attrib in TcAttrib:
        Attributes[attrib.attribute.name]=attrib.value

    return render(request, 'ControlPanel/thinClientDetail.html',
                    {
                        'thinclient': thinclient,
                        'TcAttrib': TcAttrib,
                        'GroupAttrib': GroupAttrib,
                        'Attributes': Attributes,
                        }
                )

def groupDetail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    GroupAttrib = GroupAttributeValue.objects.filter(group=group.id)

    return render(request, 'ControlPanel/groupDetail.html',
                    {
                        'Group': group,
                        'GroupAttrib': GroupAttrib,
                        }
                )

def attributeDetail(request, attribute_id):
    attribute = get_object_or_404(Attribute, pk=attribute_id)

    return render(request, 'ControlPanel/attributeDetail.html',
                    {
                        'Attribute': attribute,
                        }
                )