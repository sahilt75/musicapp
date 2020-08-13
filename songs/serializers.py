from rest_framework import serializers
from .models import Rating, SongMaster, GenreMaster, ArtistMaster, AlbumMaster, SongArtist


class AddRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['user', 'song', 'rating']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreMaster
        fields = ['genre']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumMaster
        fields = ['id', 'album']


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistMaster
        fields = ['artist']


class SongMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongMaster
        depth = 1
        fields = ['id', 'title', 'name', 'mp3', 'genre', 'song_rating', 'album']


class SongArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongArtist
        depth = 2
        fields = ['song', 'artist']
