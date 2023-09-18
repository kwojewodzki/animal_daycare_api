from django.urls import path

from . import views

urlpatterns = [
    path('', views.animalListCreateView),
    path('<int:pk>/', views.animalRetrieveUpdateDestroyAPIView),
]
