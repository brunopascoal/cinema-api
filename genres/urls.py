from django.urls import path
from genres.views import GenreListCreateApiView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path("genres/", GenreListCreateApiView.as_view(), name='genre-create-list'),
    path("genres/<int:pk>/", GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-list'),
]
