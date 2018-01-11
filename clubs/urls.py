from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.information, name='information'),
    url(r'^locations/$', views.locations, name= 'locations'),
    url(r'^dubai/$', views.dubai, name= 'dubai'),
    url(r'^dubai/albarshamixed/$', views.albarshamixed, name= 'albarshamixed'),
    url(r'^dubai/reefmall/$', views.reefmall, name= 'reefmall'),
    url(r'^dubai/ibnbattuta/$', views.ibnbattuta, name= 'ibnbattuta'),
    url(r'^dubai/businessvillagediera/$', views.businessvillagediera, name= 'businessvillagediera'),
    url(r'^dubai/albarshamixed/membership/$', views.albarshamixedmembership, name= 'albarshamixedmembership'),
    url(r'^dubai/albarshamixed/membership/options/$', views.albarshamixedoptions, name= 'albarshamixedoptions'),
    url(r'^register/$', views.register, name= 'register'),
    url(r'^regstore/$',views.reg_store, name = "regstore"),
]