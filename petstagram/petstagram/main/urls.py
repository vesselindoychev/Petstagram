from django.urls import path

from petstagram.main.views.generic import HomeView, DashboardView
from petstagram.main.views.pet_photos import CreatePetPhotoView, PetPhotoDetailsView
from petstagram.main.views.pets import CreatePetView

urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='show home'),

    # Dashboard
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # Pets
    path('pet/add/', CreatePetView.as_view(), name='create pet'),

    # PetPhotos
    path('photo/add/', CreatePetPhotoView.as_view(), name='create pet photo'),
    path('photo/details/<int:pk>/', PetPhotoDetailsView.as_view(), name='pet photo details'),
]