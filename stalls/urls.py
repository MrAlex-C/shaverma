from django.conf.urls import url
from stalls import views

urlpatterns = [
    url(r'^$', views.showListStalls, name='showListStalls'),
]