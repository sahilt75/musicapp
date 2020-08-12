from django.urls import path
from .views import CreatePlaylistView,AddPlaylistSongView,RemoveSongFromPlaylist

urlpatterns = [
    path('playlist/create/', CreatePlaylistView.as_view(),name='createplaylist'),
    path('playlist/songs/add/', AddPlaylistSongView.as_view(),name='addplaylistsong'),
    path('playlist/songs/<int:pk>/remove/', RemoveSongFromPlaylist.as_view(),name='removeplaylistsong'),
]
