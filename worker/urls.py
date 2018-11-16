# django.urls import path
from django.conf.urls import url
from . import views
app_name='worker'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^listvcm/$', views.listvcm,name='listvcm'),
    url(r'^listserver/$', views.listserver, name='listserver'),
    url(r'^applyvcm/$', views.applyvcm, name='applyvcm'),
    url(r'^delvcm/$', views.delvcm, name='delvcm'),
    url(r'^regserver/$', views.regserver, name='regserver'),
]