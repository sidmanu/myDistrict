from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^', include('dashboard.urls', namespace="dashboard")),
    # Examples:
    # url(r'^$', 'myDistrict.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
) 
