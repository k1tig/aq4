
from django.shortcuts import render, redirect
from catalog.forms import ScapeCreateForm, PlantForm
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import TemplateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from catalog.models import Scape, Plant,Profile
from journal.models import Entry
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin



class HomePageView(TemplateView):
    template_name= "home.html"

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

def logout_view(request):
    logout(request)
    messages.success(request, ("Logout Successful"))
    return redirect("home")

class ScapeListView(ListView):
    model = Scape
    template_name= "list_scape.html"



###### Below: User Scapes page view

def user_scapesView(request, pk):
    profile = Profile.objects.get(id=pk)
    scape = Scape.objects.filter(owner = pk)

    context = {
        'scape' : scape,
        'profile' : profile,
    }
    return render(request, 'user_page.html', context)




'''
class AddScapeView(FormView):
    template_name = "add_scape.html"
    form_class = ScapeForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''

class AddScapeView(LoginRequiredMixin ,CreateView):
    model = Scape
    form_class=ScapeCreateForm
    success_url = reverse_lazy('home')
    template_name = 'add_scape.html'

    def get_form_kwargs(self):
        kwargs = super(AddScapeView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs





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



### not fixed 
def tag_view(request, pk):
    tag= Plant.objects.get( id =  pk)
    scape = tag.scape_set.all()


    context = {
        'tag' : tag,
        'scape': scape,
    }

    return render(request, 'tag_view.html', context)   

def scapeview(request, pk):
    scape = Scape.objects.get(id=pk)
    feed = Entry.objects.filter(scape = pk)
    
    paginator = Paginator(feed, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'scape' : scape,
        'feed' : feed,
        'page_obj' : page_obj,
    }

    return render(request, 'scape.html', context)

