from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^(?P<album_id>[0-9]+)/$', views.detailedAlbum,name="Albums"),
]

