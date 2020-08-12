from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from .serializers import CreatePlaylistSerializer,AddRemovePlaylistSongSerializer
from rest_framework.response import Response
from .models import PlaylistSong

# Create your views here.
class CreatePlaylistView(mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = CreatePlaylistSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AddPlaylistSongView(mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = AddRemovePlaylistSongSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RemoveSongFromPlaylist(mixins.DestroyModelMixin,generics.GenericAPIView):
    serializer_class = AddRemovePlaylistSongSerializer
    queryset = PlaylistSong.objects.all()

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response({'status':200,'message':'Song removed from playlist'})
