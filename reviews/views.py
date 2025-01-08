from rest_framework import generics
from django.shortcuts import render
from .models import Reviews
from .serializers import ReviewsSerializer

class ReviewListCreateApiView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer