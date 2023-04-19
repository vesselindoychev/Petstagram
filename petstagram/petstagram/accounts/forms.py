import datetime

from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from petstagram.accounts.models import Profile
from petstagram.common.helpers import BootstrapFormMixin


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter first name'
            }
        )
    )

    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter last name'}
        )
    )

    picture = forms.URLField(
        widget=forms.URLInput(
            attrs={'placeholder': 'Enter URL'}
        ),
        label='Link to Profile Picture'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'placeholder': 'Enter password',
                   'class': 'form-control'}
        )
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'placeholder': 'Enter password again',
                   'class': 'form-control'}
        )
        self.fields['password2'].label = 'Confirm Password '

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'picture')
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email'
                }
            )
        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.fields['date_of_birth'].label = 'Date of Birth'

    class Meta:
        model = Profile
        exclude = ('user', )
        current_year = datetime.datetime.now().year
        YEARS = [i for i in range(1920, int(current_year) + 1)]

        widgets = {
            'date_of_birth': forms.SelectDateWidget(
                years=YEARS
            ),
            'description': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Enter description'
                }
            )
        }
