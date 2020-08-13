from rest_framework import serializers

from .models import Playlist, PlaylistSong


class CreatePlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['playlist', 'user']


class PlaylistSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistSong
        fields = ['playlist', 'song']
        depth = 1
