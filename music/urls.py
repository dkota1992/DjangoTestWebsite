from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name="indexing"),
    url(r'^index2/$', views.index2,name="indexing"),
    url(r'^index3/$', views.index3,name="indexing"),
    url(r'^(?P<album_id>[0-9]+)/$', views.detailAlbum ,name="DetailAlbums"),
]