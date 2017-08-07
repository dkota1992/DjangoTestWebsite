from django.db import models
import time

class photoAlbum(models.Model):
    album_name = models.CharField(max_length=200)
    photographer = models.CharField(max_length=100)
    fb_page = models.CharField(max_length=300)
    
    def __str__(self):
        return "{} photographed by {}".format(self.album_name,self.photographer)
    
class photos(models.Model):
    album = models.ForeignKey(photoAlbum, on_delete=models.CASCADE)
    photo_name = models.CharField(max_length=200)
    photoTime = time.time()