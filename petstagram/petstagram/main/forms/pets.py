import datetime

from django import forms

from petstagram.common.helpers import BootstrapFormMixin
from petstagram.main.models import Pet


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        pet = super().save(commit=False)
        pet.user = self.user

        if commit:
            pet.save()
        return pet

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        YEARS = [i for i in range(1920, int(datetime.datetime.now().year) + 1)]
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Day of Birth'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter pet name'}
            ),
            'date_of_birth': forms.SelectDateWidget(
                years=YEARS,
            )
        }


class EditPetForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        YEARS = [i for i in range(1920, int(datetime.datetime.now().year) + 1)]
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Day of Birth'
        }

        widgets = {
            'date_of_birth': forms.SelectDateWidget(
                years=YEARS
            )
        }

