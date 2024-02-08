
from django.shortcuts import render
from catalog.forms import ScapeForm, PlantForm
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, ListView
from catalog.models import Scape, Plant


class HomePageView(TemplateView):
    template_name= "home.html"

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
        
# Create your views here.
