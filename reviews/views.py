from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Reviews
from .serializers import ReviewsSerializer
from core.permissions import GlobalDefaultPermissions
class ReviewListCreateApiView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)

    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
       
    
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView, GlobalDefaultPermissions,):
    permission_classes = (IsAuthenticated,)

    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer