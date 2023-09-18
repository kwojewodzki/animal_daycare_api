from django.urls import path

from . import views

urlpatterns = [
    path('', views.animalListCreateView),
    path('<int:pk>/', views.animalRetrieveUpdateDestroyAPIView),
    path('my-animals/', views.userAnimalsListAPIView),
    path("check-animals", views.AnimalListAPIView.as_view())
]
