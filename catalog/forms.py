from django.forms import ModelForm
from catalog.models import Scape, Plant

class ScapeForm(ModelForm):
    class Meta:
        model = Scape
        fields = "__all__"

class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"