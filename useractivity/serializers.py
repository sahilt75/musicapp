from rest_framework import serializers
from .models import Recommendation


class CreateRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ['from_user', 'to_user', 'type_id', 'type']
