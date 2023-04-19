from django.contrib.auth import views as auth_views, login, get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import CreateProfileForm, EditProfileForm
from petstagram.accounts.models import Profile
from petstagram.main.models import Pet, PetPhoto


class RegisterUserView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')


class DetailsProfileView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pets = Pet.objects.filter(user=self.object.user)
        pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()
        total_pet_photos_likes = sum(pp.likes for pp in pet_photos)
        total_pet_images = pet_photos.count()

        context['pets'] = pets
        context['total_pet_photos_likes'] = total_pet_photos_likes
        context['total_pet_images'] = total_pet_images
        context['is_owner'] = self.object.user_id == self.request.user.id

        return context


class EditProfileView(views.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'accounts/profile_edit.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class ChangePasswordView:
    pass
