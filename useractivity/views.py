from rest_framework import mixins
from rest_framework import generics
from .serializers import CreateRecommendationSerializer

class CreateRecommendationView(mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = CreateRecommendationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
