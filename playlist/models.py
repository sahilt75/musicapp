from django.db import models
from django.contrib.auth.models import User
from songs.models import SongMaster


# Create your models here.
class Playlist(models.Model):
    playlist = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.playlist


class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(SongMaster, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.playlist) + " " + str(self.song)
