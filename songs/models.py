from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class ArtistMaster(models.Model):
    artist = models.CharField(max_length=255)

    def __str__(self):
        return self.artist

class GenreMaster(models.Model):
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.genre

class AlbumMaster(models.Model):
    album = models.CharField(max_length=255)

    def __str__(self):
        return self.album

class SongMaster(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mp3 = models.FileField(upload_to='songs')
    album = models.ForeignKey(AlbumMaster,on_delete=models.CASCADE,null=True)
    genre = models.ForeignKey(GenreMaster,on_delete=models.CASCADE,null=True)
    song_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class SongArtist(models.Model):
    song = models.ForeignKey(SongMaster,on_delete=models.CASCADE)
    artist = models.ForeignKey(ArtistMaster,on_delete=models.CASCADE)

class Rating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    song = models.ForeignKey(SongMaster,on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)],null=True)

    def __str__(self):
        return self.song.title