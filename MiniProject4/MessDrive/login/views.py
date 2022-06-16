import http
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import User, Inmate, Staff
from .forms import InmateSignUpForm, StaffSignUpForm


# Create your views here.
def index(request):
    return render(request, 'index.html')
def signin(request):
    return render(request, 'signin.html') 

class inmate_register(CreateView):
    model = User
    form_class = InmateSignUpForm
    template_name = 'inmate.html'

class staff_register(CreateView):
    model = User
    form_class = StaffSignUpForm
    template_name = 'staff.html'    
