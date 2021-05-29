from django.shortcuts import render
from .models import Lead
from django.contrib.auth.models import User
from .serializers import LeadSerializer, CurrentUserSerializer
from rest_framework.generics import ListCreateAPIView
from django.views.generic import (
        CreateView,
        DetailView,
        ListView,
        UpdateView,
        ListView,
        DeleteView
)
# Create your views here.

class LeadListCreate(ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

# Trying to create a User version of the view
class UserListCreate(ListView):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer