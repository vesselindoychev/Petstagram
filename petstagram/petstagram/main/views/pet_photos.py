from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.main.forms.pet_photos import CreatePetPhotoForm
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
