from django.shortcuts import render


from rest_framework import generics, mixins, permissions, authentication

from .serializers import AnimalSerializer
from .models import Animal


# Create your views here.


class AnimalListCreateAPIVieww(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    lookup_field = 'pk'

animalListCreateView = AnimalListCreateAPIVieww.as_view()

    
class AnimalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    lookup_field = 'pk'
    
animalRetrieveUpdateDestroyAPIView = AnimalRetrieveUpdateDestroyAPIView.as_view()