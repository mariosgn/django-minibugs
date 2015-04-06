from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = patterns('',

    url(r"^$", TemplateView.as_view(template_name='base.html')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'minibugs/login.html'}, name="sample_login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^b/', include('minibugs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
