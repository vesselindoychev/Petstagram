# Generated by Django 3.2.18 on 2023-04-26 11:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_petphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petphoto',
            name='likes',
        ),
        migrations.AddField(
            model_name='petphoto',
            name='likes',
            field=models.ManyToManyField(related_name='pet_photo_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
