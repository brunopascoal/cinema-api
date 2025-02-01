from rest_framework import generics
from .models import Actors
from .serializers import ActorsSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPermissions
class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer
     

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)

    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer