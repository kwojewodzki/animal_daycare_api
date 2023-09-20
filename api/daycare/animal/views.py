from django.shortcuts import render


from rest_framework import generics, mixins, permissions, authentication

from .serializers import AnimalSerializer, ListAnimalSerializer
from .models import Animal


# Create your views here.

class AnimalListAPIView(generics.ListAPIView):
    queryset = Animal.objects.all()
    serializer_class = ListAnimalSerializer

class AnimalListCreateAPIView(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    lookup_field = 'pk'

animalListCreateView = AnimalListCreateAPIView.as_view()

    
class AnimalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    lookup_field = 'pk'
    
animalRetrieveUpdateDestroyAPIView = AnimalRetrieveUpdateDestroyAPIView.as_view()

class UserAnimalsListAPIView(generics.ListAPIView):
    serializer_class = AnimalSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Animal.objects.filter(owner=user)
    
userAnimalsListAPIView = UserAnimalsListAPIView.as_view()
    