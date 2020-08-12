from rest_framework import mixins
from rest_framework import generics
from .serializers import AddRatingSerializer,SongMasterSerializer,SongArtistSerializer
from .models import SongMaster,Rating,SongArtist
from statistics import mean
from rest_framework.response import Response
from rest_framework import filters

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