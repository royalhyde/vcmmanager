# django.urls import path
from django.conf.urls import url
from . import views
app_name='state'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reportstate/$', views.reportstate, name='reportstate'),
    url(r'^doreport/$', views.doreport, name='doreport'),
]