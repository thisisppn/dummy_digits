from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^receive/$', views.receive_sms, name='receive_sms'),
]