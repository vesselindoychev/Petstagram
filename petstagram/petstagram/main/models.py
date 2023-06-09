import datetime

from django.contrib.auth import get_user_model
from django.db import models

from petstagram.common.custom_validators import ImageMaxSizeInMbValidator

UserModel = get_user_model()


class Pet(models.Model):
    NAME_MAX_LENGTH = 30
    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'
    ANIMALS = (
        CAT,
        DOG,
        BUNNY,
        PARROT,
        FISH,
        OTHER,
    )

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=(max(len(a) for a in ANIMALS)),
        choices=((a, a) for a in ANIMALS),
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return f"{self.name} the {self.type}"


class PetPhoto(models.Model):
    MAX_SIZE_IMAGE_IN_MB = 5

    photo = models.ImageField(
        validators=(
            ImageMaxSizeInMbValidator(MAX_SIZE_IMAGE_IN_MB),
        )
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date_time = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.ManyToManyField(
        UserModel,
        related_name='pet_photo_like',
    )

    tagged_pets = models.ManyToManyField(
        Pet,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def number_of_likes(self):
        return self.likes.count()
