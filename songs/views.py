from rest_framework import mixins
from rest_framework import generics
from .serializers import AddRatingSerializer,SongMasterSerializer,SongArtistSerializer
from .models import SongMaster,Rating,SongArtist
from statistics import mean
from rest_framework.response import Response
from rest_framework import filters
from playlist.models import Playlist,PlaylistSong
from playlist.serializers import PlaylistSongSerializer

class AddRatingView(mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = AddRatingSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            rating,created= Rating.objects.get_or_create(song_id=serializer.data['song'],user_id=serializer.data['user'])
            rating.rating = serializer.data['rating']
            rating.save()

            song = SongMaster.objects.get(id=rating.song_id)
            ratings = Rating.objects.filter(song=rating.song).values('rating')
            ratings_list = [item['rating'] for item in list(ratings)]
            mean_rating = mean(ratings_list)
            song.song_rating = int(mean_rating)
            song.save()

            return Response({'status':200,'message':'Rating added'})

class SongsListView(generics.ListAPIView):
    queryset = SongMaster.objects.all()
    serializer_class = SongMasterSerializer

class SearchByGenre(generics.ListAPIView):
    queryset = SongMaster.objects.all()
    serializer_class = SongMasterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['genre__genre']

class SearchByAlbum(generics.ListAPIView):
    queryset = SongMaster.objects.all()
    serializer_class = SongMasterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['album__album']

class SearchByTitle(generics.ListAPIView):
    queryset = SongMaster.objects.all()
    serializer_class = SongMasterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class SearchByArtist(generics.ListAPIView):
    queryset = SongArtist.objects.all()
    serializer_class = SongArtistSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['artist__artist']

class AutoSuggest(generics.GenericAPIView):

    @staticmethod
    def get(request, *args, **kwargs):
        songs_queryset = SongMaster.objects.all()
        songs_serializer = SongMasterSerializer(songs_queryset,many=True)
        songs = songs_serializer.data

        playlist_songs = PlaylistSong.objects.filter(playlist__user_id=kwargs['pk'])
        playlist_songs_serializer = PlaylistSongSerializer(playlist_songs,many=True)
        playlist_songs_serializer = playlist_songs_serializer.data
        genre_list = [item['song']['genre'] for item in playlist_songs_serializer]
        album_list = [item['song']['album'] for item in playlist_songs_serializer]
        suggested_songs = [item for item in songs if item['genre']['id']  in genre_list or item['album']['id']  in album_list]

        return  Response({'status':200,'message':'Suggested songs based on your playlist','data':suggested_songs})

