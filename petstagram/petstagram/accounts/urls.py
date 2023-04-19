from django.urls import path

from petstagram.accounts.views import LoginUserView, RegisterUserView, DetailsProfileView, EditProfileView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('create-profile/', RegisterUserView.as_view(), name='register'),
    path('profile/<int:pk>/', DetailsProfileView.as_view(), name='profile details'),
    path('edit-profile/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
]