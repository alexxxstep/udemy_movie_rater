from rest_framework import serializers
from .models import Movie, Rating


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'no_of_ratings', 'avr_rating']

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'stars', 'user', 'movie']

    def create(self, validated_data):
        return Rating.objects.create(**validated_data)
