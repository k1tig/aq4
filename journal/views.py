from django.shortcuts import render
from journal.forms import EntryForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from journal.models import Entry


class AddEntryView(CreateView, LoginRequiredMixin):
    model = Entry
    fields = ["content"]
    success_url = "/"

    def form_valid(self, form):
        #form.instance.
        form.save()
        return super().form_valid(form)


