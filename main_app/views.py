from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponse, HttpResponseRedirect
# bring in some things to make auth easier
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# bring in decorator
from django.contrib.auth.decorators import login_required


# attempt form
from django.forms.models import model_to_dict

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def projects(request):
  return render(request, 'projects.html')

def skills(request):
  return render(request, 'skills.html')


# Instrcutions
# 1. Update index view function to look similar to the contact view function
# 2. Add a index.html page with the current HTML that is displayed
# 3. Update about view function to look similar to the contact view function
# 4. Add a about.html page with the current HTML that is displayed
# 5. Update your urls.py file (main_app) to look similar to the contact path

# 1. Make a view function
# 2. Make the html page
# 3. Add the view to the urls.py inside of main_app.urls

# In browser
# When I go to localhost:8000/contact
# Django -> urls -> /contact -> vews.contact (runs function) -> templates -> contact.html
