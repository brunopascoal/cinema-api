from django.shortcuts import render
from rest_framework import generics
from .models import Actors
from .serializers import ActorsSerializer

class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer
     

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer