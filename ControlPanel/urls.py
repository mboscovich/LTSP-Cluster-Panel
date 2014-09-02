# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from ControlPanel import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)