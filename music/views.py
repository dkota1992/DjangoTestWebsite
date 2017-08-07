from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.template import loader

def index(request):
    all_albums = Album.objects.all()
    html = ""
    for album in all_albums:
        url = "/music/{}/".format(album.id)
        html += '<a href ={}>{}</a><br>'.format(url,album.album_title)
    return HttpResponse(html)

def index3(request):
    all_albums = Album.objects.all()
    context = {'albums':all_albums}
    return render(request, 'music/index.html', context)

def index2(request):
    all_albums = Album.objects.all()
    template = loader.get_template("music/index.html")
    context = {'albums': all_albums}
    return HttpResponse(template.render(context,request))

def detailAlbum(request,album_id):
    return HttpResponse("<h2>Details for album id : {} </h2>".format(album_id.strip("/")))