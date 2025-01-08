from django.urls import path
from .views import MovieListCreateAPIView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    path("movie/", MovieListCreateAPIView.as_view(), name='movie-create-list'),
    path("movie/<int:pk>/", MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-list'),
]
