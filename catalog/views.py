
from django.shortcuts import render
from catalog.forms import ScapeForm, PlantForm
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from catalog.models import Scape, Plant


class HomePageView(TemplateView):
    template_name= "home.html"


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class ScapeListView(ListView):
    model = Scape
    template_name= "list_scape.html"

class ScapeView(DetailView):
    model = Scape
    template_name = "scape.html"

class AddScapeView(FormView):
    template_name = "add_scape.html"
    form_class = ScapeForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class UpdateScapeView(UpdateView):
    model = Scape
    fields = "__all__"
    template_name = "update_scape.html"
    success_url = "/"

    
class AddPlantView(FormView):
    template_name = "add_plant.html"
    form_class = PlantForm
    success_url = "/catalog/add-plant"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UpdatePlantView(UpdateView):
    model = Plant
    fields = "__all__"
    template_name = "update_plant.html"
    success_url = "/"
        
