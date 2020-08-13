from rest_framework import mixins
from rest_framework import generics
from .serializers import CreatePlaylistSerializer,PlaylistSongSerializer
from rest_framework.response import Response
from .models import PlaylistSong,Playlist
from songs.models import SongMaster,SongArtist
from songs.serializers import SongMasterSerializer,SongArtistSerializer

class CreatePlaylistView(mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = CreatePlaylistSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AddPlaylistSongView(mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = PlaylistSongSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RemoveSongFromPlaylist(mixins.DestroyModelMixin,generics.GenericAPIView):
    serializer_class = PlaylistSongSerializer
    queryset = PlaylistSong.objects.all()

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response({'status':200,'message':'Song removed from playlist'})

class AutoGenerateByGenre(generics.GenericAPIView):

    def get(self,request, *args, **kwargs):
        playlist = Playlist.objects.create(playlist='Auto Generated Genre Playlist')
        songs_queryset = SongMaster.objects.filter(genre_id=kwargs['pk'])
        song_serializer = SongMasterSerializer(songs_queryset,many=True)
        songs = song_serializer.data
        if songs:
            batch = [PlaylistSong(playlist=playlist,song_id=song['id']) for song in songs]
            PlaylistSong.objects.bulk_create(batch)
            return Response({'status': 200, 'message': 'Playlist auto generated'})
        else:
            return Response({'status': 400, 'message': 'Playlist could not be generated'})


class AutoGenerateByArtist(generics.GenericAPIView):
    def get(self,request, *args, **kwargs):
        playlist = Playlist.objects.create(playlist='Auto Generated Artist Playlist')
        songs_queryset = SongArtist.objects.filter(artist_id=kwargs['pk'])
        song_serializer = SongArtistSerializer(songs_queryset, many=True)
        songs = song_serializer.data
        if songs:
            batch = [PlaylistSong(playlist=playlist, song_id=song['song']['id']) for song in songs]
            PlaylistSong.objects.bulk_create(batch)
            return Response({'status': 200, 'message': 'Playlist auto generated'})
        else:
            return Response({'status': 400, 'message': 'Playlist could not be generated'})


