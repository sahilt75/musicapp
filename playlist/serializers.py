from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Playlist,PlaylistSong

class CreatePlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['playlist','user']

class AddRemovePlaylistSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistSong
        fields = ['playlist','song']