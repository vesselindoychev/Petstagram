from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.main.forms.pet_photos import CreatePetPhotoForm, EditPetPhotoForm
from petstagram.main.models import PetPhoto


class CreatePetPhotoView(views.CreateView):
    model = PetPhoto
    form_class = CreatePetPhotoForm
    template_name = 'main/photo_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')


class EditPetPhotoView(views.UpdateView):
    model = PetPhoto
    form_class = EditPetPhotoForm
    template_name = 'main/photo_edit.html'

    def get_success_url(self):
        return reverse_lazy('pet photo details', kwargs={'pk': self.object.pk})


class PetPhotoDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = PetPhoto
    template_name = 'main/photo_details.html'
    context_object_name = 'pet_photo'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('tagged_pets')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user

        return context
