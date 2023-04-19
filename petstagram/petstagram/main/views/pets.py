from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.main.forms.pets import CreatePetForm
from petstagram.main.models import Pet


class CreatePetView(views.CreateView):
    model = Pet
    form_class = CreatePetForm
    template_name = 'main/pet_create.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
