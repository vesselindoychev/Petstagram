from django.contrib.auth import mixins as auth_mixins
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.main.forms.pet_photos import CreatePetPhotoForm, EditPetPhotoForm, DeletePetPhotoForm
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


class DeletePetPhotoView(views.DeleteView):
    model = PetPhoto
    form_class = DeletePetPhotoForm
    template_name = 'main/photo_delete.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')


class PetPhotoDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = PetPhoto
    template_name = 'main/photo_details.html'
    context_object_name = 'pet_photo'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('tagged_pets')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user

        likes_connected = get_object_or_404(
            PetPhoto,
            id=self.kwargs['pk']
        )
        liked = False

        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['number_of_likes'] = likes_connected.number_of_likes()
        context['photo_is_liked'] = liked
        return context


def like_photo(request, pk):
    photo = get_object_or_404(
        PetPhoto,
        id=request.POST.get('pet_photo_id')
    )

    if photo.likes.filter(id=request.user.id).exists():
        photo.likes.remove(request.user)
    else:
        photo.likes.add(request.user)
    # photo.likes += 1
    # photo.save()

    # return redirect('pet photo details', pk)
    return HttpResponseRedirect(reverse_lazy('pet photo details', args=[str(pk)]))
