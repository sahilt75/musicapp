from django.contrib import admin
from .models import Playlist,PlaylistSong

# Register your models here.
admin.site.register(PlaylistSong)
admin.site.register(Playlist)