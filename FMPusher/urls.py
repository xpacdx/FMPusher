from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FMPusher.views.home', name='home'),
    # url(r'^FMPusher/', include('FMPusher.foo.urls')),
    url(r'^device$', 'main.views.device'),
    url(r'^clkcount/(?P<pk>\d+)$', 'main.views.clkcountpk'),
    url(r'^clkcount/(?P<url>.+)$', 'main.views.clkcount'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
