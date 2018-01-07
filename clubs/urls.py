from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.information, name='information'),
    url(r'^locations/$', views.locations, name= 'locations'),
    url(r'^dubai/$', views.dubai, name= 'dubai'),
]