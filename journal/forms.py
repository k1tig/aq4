

from journal.models import Entry
from django.views.generic.edit import CreateView
from django import forms
from catalog.models import Scape

class EntryCreateForm(CreateView):
    scape = forms.ModelChoiceField(
        queryset=Scape.objects.filter(owner = 0)
    )
    
    class Meta:
        model = Entry
        fields = ('scape', 'post_date', 'content')