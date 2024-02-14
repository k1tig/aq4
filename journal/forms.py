

from journal.models import Entry
from django.utils import timezone
from django import forms
from catalog.models import Scape


class EntryCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(EntryCreateForm, self).__init__(*args, **kwargs)
        self.fields['scape'].queryset= Scape.objects.filter(owner = self.request.user.id)

    class Meta:
        model = Entry
        fields = ('scape', 'post_date', 'content')
    