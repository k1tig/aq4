from django.forms import ModelForm
from catalog.models import Scape, Plant, Profile
from django import forms

class ScapeForm(ModelForm):
    class Meta:
        model = Scape
        fields = "__all__"

class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"




class ScapeCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ScapeCreateForm, self).__init__(*args, **kwargs)
        self.fields['owner'].queryset= Profile.objects.filter(user_name_id = self.request.user)

    class Meta:
        model = Scape
        fields = ('scape_name', 'owner', 'size', 'volume', 'filtration', 'lighting', 'co2', 'soil', 'hardscape', 'fish', 'invertebrate', 'plants')        
