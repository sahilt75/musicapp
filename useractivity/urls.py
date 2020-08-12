from django.urls import path
from .views import CreateRecommendationView

urlpatterns = [
    path('recommendation/create/', CreateRecommendationView.as_view(),name='createrecommendation'),
]
