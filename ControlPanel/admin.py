from django.contrib import admin

# Register your models here.
from ControlPanel.models import Attribute, Group, ThinClient
from ControlPanel.models import GroupAttributeValue, ThinClientAttributeValue


class GroupAttributeInline(admin.TabularInline):
    model = GroupAttributeValue
    extra = 1


class ThinClientAttributeInline(admin.TabularInline):
    model = ThinClientAttributeValue
    extra = 1


class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'defaultValue', 'description')
    search_fields = ['name']
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True
    fieldsets = [
        ('Atributo', {'fields': ['name', 'defaultValue', 'description'],
            'classes': ('wide', 'extrapretty'),
            'description': ('Attributes define specific properties that can be'
                            ' later assigned to ThinClients or groups.'
                            ),
                    }),
    ]


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ['name']
    inlines = [GroupAttributeInline]
    fieldsets = [
        ('Grupos', {'fields': ['name', 'parent'],
            'classes': ('wide', 'extrapretty'),
            'description': ('Groups allow you tu associate a set of attributes'
                            ' and values to a group of ThinClients.'
                            ),
                    }),
    ]


class ThinClientAdmin(admin.ModelAdmin):
    list_display = ('dnsName', 'mac', 'group')
    list_filter = ['group']
    search_fields = ['dnsName', 'mac']
    fieldsets = [
        ('Datos del cliente', {'fields': ['dnsName', 'mac', 'group'],
            'classes': ('wide', 'extrapretty'),
            'description': ('Each thinclient must belong to a group and can '
                            'contain special attributes. By default, everything'
                            ' thinclient belongs to the Default group.'
                            ),
                    }),
    ]
    inlines = [ThinClientAttributeInline]

admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(ThinClient, ThinClientAdmin)
