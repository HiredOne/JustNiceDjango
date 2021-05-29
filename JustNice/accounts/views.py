from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm # Model form
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView
)


class SignUpView(CreateView):
    form_class = UserCreationForm
    # reverse_lazy is used instead of reverse because urls for CBVs are not
    # loaded when the file is imported, so we have to use the lazy form of 
    # reverse to load them later when they're available.
    success_url = reverse_lazy('login') 
    template_name = 'registration/signup.html'
