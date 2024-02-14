from django.shortcuts import render,redirect
from journal.forms import EntryCreateForm

def add_entry(request):
    if request.method =='POST':
        form =EntryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={'form' : EntryCreateForm()}
    return render(request,'add-entry.html', context)
    


