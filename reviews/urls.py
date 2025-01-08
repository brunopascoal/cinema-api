from django.urls import path
from .views import ReviewListCreateApiView, ReviewRetrieveUpdateDestroyView


urlpatterns = [
    path("reviews/", ReviewListCreateApiView.as_view(), name="review-create-list"),
    path("reviews/", ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-list')
]
