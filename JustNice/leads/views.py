from django.shortcuts import render
from .models import Lead
from django.contrib.auth.models import User
from .serializers import LeadSerializer, CurrentUserSerializer
from rest_framework.generics import ListCreateAPIView

# Create your views here.

class LeadListCreate(ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

# Trying to create a User version of the view
class UserListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer