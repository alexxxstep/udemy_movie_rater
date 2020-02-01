from rest_framework import serializers
from .models import Movie, Rating


class MovieSerializer(serializers.Serializer):
    class Meta:
        model = Movie
        fields = ['id', 'title']

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class RatingSerializer(serializers.Serializer):
    class Meta:
        model = Rating
        fields = ['id', 'stars', 'user', 'movie']

    def create(self, validated_data):
        return Rating.objects.create(**validated_data)
