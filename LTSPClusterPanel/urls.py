from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LTSPClusterPanel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ControlPanel/', include('ControlPanel.urls')),
    #url(r'^admin/$', RedirectView.as_view(url=reverse_lazy('admin:app_list',
        #args=('ControlPanel',)))),
    url(r'^admin/$',RedirectView.as_view(url='/admin/ControlPanel/thinclient/')),
    url(r'^admin/', include(admin.site.urls)),
)
