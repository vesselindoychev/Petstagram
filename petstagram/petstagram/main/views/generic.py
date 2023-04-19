from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.common.views_mixins import RedirectToDashboard
from petstagram.main.models import PetPhoto


class HomeView(RedirectToDashboard, views.TemplateView):
    template_name = 'main/home_page.html'


class DashboardView(views.ListView):
    model = PetPhoto
    template_name = 'main/dashboard.html'
