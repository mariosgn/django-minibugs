from django.conf.urls import patterns, include, url

from .views import MinibugsHome, MinibugsCreate, MinibugsDetails, MinibugsUpdate

urlpatterns = patterns('',
    url('^new$', MinibugsCreate.as_view(), name="minibugs_create"),
    url(r"^(?P<pk>[\.\w]+)/$", MinibugsDetails.as_view(), name="minibugs_details"),
    url(r"^update/(?P<pk>[\.\w]+)/$", MinibugsUpdate.as_view(), name="minibugs_update"),
    url('^$', MinibugsHome.as_view(), name="minibugs_home"),
)
