import datetime
from os import read
from rest_framework import serializers
from .models import Movie
from genres.models import Genre
from actors.models import Actors
from django.db.models import Avg
class MovieSerializer(serializers.ModelSerializer):
    
    rate = serializers.SerializerMethodField(read_only=True) # A field that gets its value by calling a method on the serializer class it is attached to
    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj): # must be get_<field_name>, obj is the instance of the model, run for each instance of the model
        rate = obj.reviews.aggregate(Avg('rate'))['rate__avg']
        if rate:
            return round(rate, 1)
        # obj_reviews = obj.reviews.all()
        # if obj_reviews:
        #     return sum([review.rate for review in obj_reviews]) / len(obj_reviews)
        return None
    
    def validate_release_date(self, value):
        if value.year < 1800 or value > datetime.datetime.now():
            raise serializers.ValidationError("Release Date cant be less than 1990")
        return value
    
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("Resume cant be greater than 200 caracters")
        return value