from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm

def index(request):
    return HttpResponse('<em> Welcome! </em>')

def help(request):
    return render(request, 'apptwo/help.html', {'name' : 'Help Page'})

def users(request):
    persons = User.objects.all()
    return render(request, 'apptwo/users.html', context={'persons':persons})

def sign_up(request):
    form = UserForm()
    if request.method == "POST":
        form=UserForm(request.POST)
        if form.is_valid():
            print('its okay, go on')
            print(form.cleaned_data['first_name'])
            form.save()
            return index(request) #после сохранения перейти на стартовую страницу

    return render(request, 'apptwo/signup.html', {'form' : form})

