from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, views, response, status
from .models import Movie
from .serializers import MovieSerializer, MovieListDetailSerializer
from core.permissions import GlobalDefaultPermissions
from django.db.models import Count, Avg
from reviews.models import Reviews

class MovieListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieSerializer
    
class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieSerializer
    

class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()
    def get(self, request):
        
        total_movies = self.queryset.count()
        movies_by_genres = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Reviews.objects.count()
        average_rates = Reviews.objects.aggregate(Avg('rate'))['rate__avg']
        return response.Response(data={
                'total_movies': total_movies,
                'movies_by_genres': movies_by_genres,
                'total_reviews': total_reviews,
                'average_rates': round(average_rates, 1) if average_rates else 0,
                },
            status=status.HTTP_200_OK,
        )