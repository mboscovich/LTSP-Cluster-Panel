# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from Terminal import views

#
# code 1 ?ip=192.168.2.221/mac=00:90:F5:2A:ED:A7/bootservip=192.168.2.253/code=1
#      XTERM is booting and has its bootservip
# code 2 ?ip=192.168.2.221/appservip=192.168.2.254/display=0.0/code=2
#     XTERM has it appserver & display
# code 3 * ?ip=192.168.2.221/appservip=192.168.2.253/display=0.0/code=3/username=3
#      a user is connected
# code 4 * ?ip=192.168.2.221/appservip=192.168.2.253/display=0.0/code=4/username=3
#      a user is de connected
#
urlpatterns = patterns('',
    #url(r'^attribute/(\d+)/$', views.attributeDetail, name='attributeDetail'),
    # code 1
    url(r'^index.php/$', views.code1, name='code1'),
    ## code 2
    #url(r'?ip=', views.code2, name='code2'),
    ## code 3
    #url(r'?ip=', views.code3, name='code3'),
    ## code 4
    #url(r'?ip=', views.code4, name='code4'),

)