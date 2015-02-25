# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from ControlPanel import views

urlpatterns = patterns('',
    url(r'^$', views.NodesIndex.as_view(), name='NodesIndex'),
    url(r'^groups/$', views.groupsIndex.as_view(), name='groupsIndex'),
    url(r'^attibutes/$', views.attributesIndex.as_view(), name='attributesIndex'),
    url(r'^Node/(\d+)/$', views.NodeDetail, name='NodeDetail'),
    url(r'^group/(\d+)/$', views.groupDetail, name='groupDetail'),
    url(r'^attribute/(\d+)/$', views.attributeDetail, name='attributeDetail'),
)