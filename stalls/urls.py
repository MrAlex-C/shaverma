from django.conf.urls import url
from stalls import views

urlpatterns = [
    url(r'^$', views.StallsList.as_view(), name='showListStalls'),
]