from django.conf.urls import url, patterns
from dashboard import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^login/$', views.login, name='login'),
    )
