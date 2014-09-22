# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from ControlPanel import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^thinclient/(\d+)/$', views.detail, name='detail'),
    url(r'^thinclient/(\d+)/$', views.detail, name='groupIndex'),
    url(r'^thinclient/(\d+)/$', views.detail, name='attib_detail'),
)