from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, AccessRecord, Webpage
from . import forms
# Create your views here.

def index(request):
    return render(request, 'first_app/index.html')

def form_name_view(request):
    form=forms.FormName()

    if request.method=='POST':
        form=forms.FormName(request.POST)
        if form.is_valid():
            print('form submitted!')
            print('name: '+form.cleaned_data['name'])
            print('email: '+form.cleaned_data['email'])
            print('text: '+form.cleaned_data['text'])


    return render(request, 'first_app/form_page.html', context={'form': form})
