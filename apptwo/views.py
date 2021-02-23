from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import User
from .forms import UserForm, UploadForm, NewUploadForm

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


def name_view(request): 

    form = NewUploadForm()
    if request.method == "POST":
        form=NewUploadForm(request.POST)

    return render(request, 'apptwo/name.html', {'form':form})


from rest_framework.views import APIView
from rest_framework.response import Response

class NameApiView(APIView):

    def post(self, request):
        form = NewUploadForm(request.POST)

        result = {'name':form.cleaned_data['name'], 'last_name':form.cleaned_data['last_name']}

        return Response({'result':result})

