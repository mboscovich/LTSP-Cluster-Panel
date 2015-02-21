# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from ControlPanel import views

urlpatterns = patterns('',
    url(r'^$', views.thinClientsIndex.as_view(), name='thinClientsIndex'),
    url(r'^groups/$', views.groupsIndex.as_view(), name='groupsIndex'),
    url(r'^attibutes/$', views.attributesIndex.as_view(), name='attributesIndex'),
    url(r'^thinclient/(\d+)/$', views.thinClientDetail, name='thinClientDetail'),
    url(r'^group/(\d+)/$', views.groupDetail, name='groupDetail'),
    url(r'^attribute/(\d+)/$', views.attributeDetail, name='attributeDetail'),

)