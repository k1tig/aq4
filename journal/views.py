from django.shortcuts import render
from journal.forms import EntryForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from journal.models import Entry
from journal.forms import EntryCreateForm


class AddEntryView(CreateView, LoginRequiredMixin):
    model = Entry
    fields = ["content"]
    success_url = "/"

    def form_valid(self, form):
        #form.instance.
        form.save()
        return super().form_valid(form)
    

def add_entry(request):
    context = {'form'  : EntryCreateForm()}
    return render(request, 'jounral/add-entry.html', context)

#https://www.youtube.com/watch?v=Zzd4sL7drKQ&t=178s
    



