from django.urls import path
from .views import *

urlpatterns = [
    path('playlist/create/', CreatePlaylistView.as_view(),name='createplaylist'),
    path('playlist/songs/add/', AddPlaylistSongView.as_view(),name='addplaylistsong'),
    path('playlist/songs/<int:pk>/remove/', RemoveSongFromPlaylist.as_view(),name='removeplaylistsong'),
    path('playlist/autogenerate/genre/<int:pk>/', AutoGenerateByGenre.as_view(),name='autogeneratebygenre'),
    path('playlist/autogenerate/artist/<int:pk>/', AutoGenerateByArtist.as_view(),name='autogeneratebyartist'),
]
