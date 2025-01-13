from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer

class MovieListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    
class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
