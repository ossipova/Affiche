from rest_framework import serializers
from .models import Movie, Director, Review


class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ['id', 'name', 'movie_count']

    def get_movie_count(self, director):
        return director.movie_count


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director', 'movie_reviews']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars', 'movie']


class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    review_text = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_review_text(self, movie):
        return [i.text for i in movie.review_text.all()]

    def get_reviews(self, movie):
        return [i.stars for i in movie.movie_reviews.all()]

    def get_rating(self, movie):
        return movie.rating
