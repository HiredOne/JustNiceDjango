from django.shortcuts import render
from .models import Lead
from django.contrib.auth.models import User
from django.core.serializers import serialize
from .serializers import LeadSerializer, CurrentUserSerializer
from rest_framework.generics import ListCreateAPIView
from django.views.generic import (
        ListView,
)
# Create your views here.

class LeadListCreate(ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

# Trying to create a User version of the view2
class UserListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    template_name = 'users/user_list.html'
    serializer_class = CurrentUserSerializer
    data = serialize("json", User.objects.all())

    # # What to (forcefully) render on a GET req
    # def get(self, request, *args, **kwargs):
    #     context = {'data': self.data, "dic" : self.queryset.values()}
    #     return render(request, self.template_name, context)

    # Commented out cause not impl yet
    # def post(self, request, *args, **kwargs):
    #     context = {<fill in stuff>}