from django.conf.urls import url, patterns
from dashboard import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
    )
