from django.contrib import admin
from .models import SongMaster, ArtistMaster, AlbumMaster, GenreMaster, SongArtist, Rating

admin.site.register(SongMaster)
admin.site.register(AlbumMaster)
admin.site.register(ArtistMaster)
admin.site.register(GenreMaster)
admin.site.register(SongArtist)
admin.site.register(Rating)
