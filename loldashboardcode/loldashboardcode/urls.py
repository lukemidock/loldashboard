from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^calculation/results/', 'loldashboardapp.views.quadratic_calculation', name='results'),
    url(r'^$', 'loldashboardapp.views.index')
)

    # url(r'^$', 'loldashboardcode.views.home', name='home'),
    # url(r'^loldashboardcode/', include('loldashboardcode.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

