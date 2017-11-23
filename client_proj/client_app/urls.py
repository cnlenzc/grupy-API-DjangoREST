from django.conf.urls import url
from client_app import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^cliente/$', views.ClienteList.as_view()),
    url(r'^cliente/(?P<pk>[0-9]+)/$', views.ClienteDetail.as_view()),
]
