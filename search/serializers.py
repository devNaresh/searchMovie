from rest_framework import serializers
from search.models import Genre, Movie, Director


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True, slug_field="name", queryset=Genre.objects.all())
    director = serializers.SlugRelatedField(
        slug_field="name", queryset=Director.objects.all())

    class Meta:
        model = Movie
