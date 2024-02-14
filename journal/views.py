from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from journal.forms import EntryCreateForm
from journal.models import Entry
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class AddEntry(LoginRequiredMixin ,CreateView):
    model = Entry
    form_class=EntryCreateForm
    success_url = reverse_lazy('home')
    template_name = 'add-entry.html'

    def get_form_kwargs(self):
        kwargs = super(AddEntry, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

