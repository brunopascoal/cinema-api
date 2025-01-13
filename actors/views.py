from ast import Is
from django.shortcuts import render
from rest_framework import generics
from .models import Actors
from .serializers import ActorsSerializer
from rest_framework.permissions import IsAuthenticated
class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer
     

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer