from django.shortcuts import render
from django.http import HttpResponse
from .models import photoAlbum as Album

def index(request):
    return HttpResponse("<h1> This is the Index Page </h1>")
#     all_albums = photoAlbum.objects.all()
#     html = ""
#     for album in all_albums:
#         html += "<a"
#     
def detailedAlbum(request,album_id):
    return HttpResponse("<h2> This is album : {}".format(Album.objects.get(id=album_id)))
    