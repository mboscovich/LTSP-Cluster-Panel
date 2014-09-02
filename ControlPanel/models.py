from django.db import models


# Create your models here.

class Attribute(models.Model):
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    name = models.CharField('Name', max_length=200)
    description = models.CharField(
        'Description',
        max_length=400,
        null=True,
        blank=True
        )


class AttributePossibleValues(models.Model):
    def __unicode__(self):
        output = "%s : %s" % (self.attribute.name, self.value)
        return output

    attribute = models.ForeignKey(Attribute)
    value = models.CharField('Value', max_length=200, null=True, blank=True)


class Group(models.Model):
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

    name = models.CharField('Name', max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True)
    attributes = models.ManyToManyField(
        Attribute,
        through='GroupAttributeValue'
        )


class ThinClient(models.Model):
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.dnsName

    dnsName = models.CharField('DNS Name',
        max_length=200,
        null=True,
        blank=True
        )
    mac = models.CharField('MAC Address',
        max_length=200,
        null=True,
        blank=True
        )
    group = models.ForeignKey(Group)
    attributes = models.ManyToManyField(
        Attribute,
        through='ThinClientAttributeValue'
        )


class GroupAttributeValue(models.Model):
    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s: %s = %s" % (self.group, self.attribute, self.value)
    attribute = models.ForeignKey(Attribute)
    group = models.ForeignKey(Group)
    value = models.CharField(max_length=200, null=True, blank=True)


class ThinClientAttributeValue(models.Model):
    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s: %s = %s" % (self.thinClient, self.attribute, self.value)
    attribute = models.ForeignKey(Attribute)
    thinClient = models.ForeignKey(ThinClient)
    value = models.CharField(max_length=200, null=True, blank=True)
