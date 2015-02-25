from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.

from ControlPanel.models import Node, Group, NodeAttributeValue
from ControlPanel.models import GroupAttributeValue, Attribute


class NodesIndex(generic.ListView):
    template_name = 'ControlPanel/NodesIndex.html'
    context_object_name = 'Nodes_list'

    def get_queryset(self):
        """Return all Nodes."""
        return Node.objects.order_by('dnsName')


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


def NodeDetail(request, Node_id):
    Node = get_object_or_404(Node, pk=Node_id)
    TcAttrib = NodeAttributeValue.objects.filter(Node=Node.id)
    GroupAttrib = GroupAttributeValue.objects.filter(group=Node.group.id)
    Attributes = {}
    for attrib in GroupAttrib:
        Attributes[attrib.attribute.name]=attrib.value
    for attrib in TcAttrib:
        Attributes[attrib.attribute.name]=attrib.value

    return render(request, 'ControlPanel/NodeDetail.html',
                    {
                        'Node': Node,
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