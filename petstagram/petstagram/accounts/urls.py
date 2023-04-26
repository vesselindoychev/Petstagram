from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from petstagram.accounts.views import LoginUserView, RegisterUserView, DetailsProfileView, EditProfileView, \
    ChangePasswordView, DeleteProfileView, LogoutUserView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('create-profile/', RegisterUserView.as_view(), name='register'),
    path('profile/<int:pk>/', DetailsProfileView.as_view(), name='profile details'),
    path('edit-profile/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('delete-profile/<int:pk>/', DeleteProfileView.as_view(), name='delete profile'),
    path('edit-password/<int:pk>/', ChangePasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password redirect'),
    # path('')
]