from django.shortcuts import render
from .models import Lead
from django.contrib.auth.models import User
from django.core.serializers import serialize
from .serializers import LeadSerializer, CurrentUserSerializer
from django.views.generic import (
        ListView,
)
from json import dumps
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from django.utils.decorators import method_decorator

# Create your views here.

class LeadListCreate(ListView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

# Trying to create a User version of the view2
@method_decorator(csrf_exempt, name='dispatch')
class UserListCreate(ListView):
    queryset = User.objects.all()
    template_name = 'users/user_list.html'
    serializer_class = CurrentUserSerializer
    data = CurrentUserSerializer(queryset, many = True) # serialize("json", User.objects.all())
    #data = JSONRenderer().render(data.data)
    # def get(self, request, id = 0, *args, **kwargs):
    #     users = User.objects.all()
    #     users_serializer = CurrentUserSerializer(users, many = True)
    #     return JsonResponse(users_serializer, safe = False)
    
    def post(self, request, id = 0, *args, **kwargs):
        users_data = JSONParser.parse(request)
        users_serializer = CurrentUserSerializer(data = users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully.", safe = False)
        return JsonResponse("Failed to add", safe = False)
    
    # def put(self, request, id = 0, *args, **kwargs):
    #     users_data = JSONParser.parse(request)
    #     user1 = User.objects.get(id = users_data['id'])
    #     users_serializer = CurrentUserSerializer(user1, data = users_data)
    #     if users_serializer.is_valid():
    #         users_serializer.save()
    #         return JsonResponse("Updated Successfully", safe = False)
    #     return JsonResponse("Failed to add", safe = False)
    
    # def delete(self, request, id = 0, *args, **kwargs):
    #     user1 = User.objects.get(id = id)
    #     user1.delete()
    #     return JsonResponse("Deleted successfully", safe = False)


    # queryset = User.objects.all()
    # template_name = 'users/user_list.html'
    # serializer_class = CurrentUserSerializer
    # data = serialize("json", User.objects.all())

    # # What to (forcefully) render on a GET req
    def get(self, request, *args, **kwargs):
        strData = ''  #dumps(self.data)
        # context = {'data': self.data, "dic" : self.queryset.values(), "strData" : strData}
        # print(strData)
        return JsonResponse(self.data.data, safe = False) # String of HTML code
        # context = {'data': self.data, "dic" : self.queryset.values()}
        # return render(request, self.template_name, context)

    # # Commented out cause not impl yet
    # def post(self, request, *args, **kwargs):
    #     strData = dumps(self.data)
    #     context = {'data': self.data, "dic" : self.queryset.values(), "strData" : strData}
    #     return HttpResponse(strData) # String of HTML code