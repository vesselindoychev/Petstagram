from django import forms

from petstagram.common.helpers import BootstrapFormMixin
from petstagram.main.models import PetPhoto


class CreatePetPhotoForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = PetPhoto
        exclude = ('user', 'likes',)
        labels = {
            'photo': 'Pet Image',
            'tagged_pets': 'Tag Pets',
        }

        widgets = {
            'description': forms.Textarea(
                attrs={'placeholder': 'Enter description',
                       'rows': 3,
                       }
            ),
            'tagged_pets': forms.SelectMultiple()
        }
