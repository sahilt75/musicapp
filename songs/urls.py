from django.urls import path
from .views import AddRatingView,SearchByGenre,SearchByAlbum,SearchByTitle,SearchByArtist,SongsListView

urlpatterns = [
    path('songs/', SongsListView.as_view(),name='songslist'),
    path('songs/rating/', AddRatingView.as_view(),name='addrating'),
    path('songs/searchbygenre/', SearchByGenre.as_view(),name='searchsongsbygenre'),
    path('songs/searchbyalbum/', SearchByAlbum.as_view(),name='searchbyalbum'),
    path('songs/searchbytitle/', SearchByTitle.as_view(),name='searchbytitle'),
    path('songs/searchbyartist/', SearchByArtist.as_view(),name='searchbyartist'),
]
