from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
# Register your models here.
from ControlPanel.models import Attribute, Group, Node
from ControlPanel.models import GroupAttributeValue, NodeAttributeValue
from ControlPanel.models import AttributePossibleValues


class GroupAttributeInline(admin.TabularInline):
    model = GroupAttributeValue
    extra = 1


class NodeAttributeInline(admin.TabularInline):
    model = NodeAttributeValue
    extra = 1


class AttributeAttributePossibleValuesInline(admin.TabularInline):
    model = AttributePossibleValues
    extra = 1


class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name']
    actions_on_top = False
    actions_selection_counter = True
    fieldsets = [
        ('Atributo', {'fields': ['name', 'description'],
            'classes': ('wide', 'extrapretty'),
            'description': _('Model_Attribute_desc'),
                    }),
    ]
    inlines = [AttributeAttributePossibleValuesInline]


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ['name']
    actions_on_top = False
    inlines = [GroupAttributeInline]
    fieldsets = [
        ('Grupos', {'fields': ['name', 'parent'],
            'classes': ('wide', 'extrapretty'),
            'description': _('Model_Group_desc'),
                    }),
    ]


class NodeAdmin(admin.ModelAdmin):
    list_display = ('dnsName', 'mac', 'group')
    list_filter = ['group']
    search_fields = ['dnsName', 'mac']
    actions_on_top = False
    fieldsets = [
        (_('Nodedata'), {'fields': ['dnsName', 'mac', 'group'],
            'classes': ('wide', 'extrapretty'),
            'description': _('Model_Node_desc'),
                    }),
    ]
    inlines = [NodeAttributeInline]

admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Node, NodeAdmin)
