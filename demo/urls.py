from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',

    url(r"^$", RedirectView.as_view(url='/b')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'minibugs/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^b/', include('minibugs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
