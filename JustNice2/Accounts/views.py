from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from django.contrib.auth.models import User, UserManager
from .serializers import UserSerializer

from django.core.files.storage import default_storage
# Create your views here

@csrf_exempt
def userApi(request, id = 0, *args, **kwargs):
    if request.method == "GET":
        users = User.objects.all()
        # User.objects.all().delete() # DO NOT UNCOMMENT. THIS IS TO CLEAR THE USER DB
        users_serializer = UserSerializer(users, many = True)
        return JsonResponse(users_serializer.data, safe = False)
    elif request.method == "POST":
        user_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data = user_data)
        #print(users_serializer)
        if users_serializer.is_valid():
            User.objects.create_user(**user_data)
            # users_serializer.save()
            # user = User.objects.get(username = user_data['username'])
            # user.set_password(user_data['password'])
            # user.save()
            return JsonResponse("Added Successfully", safe = False)
        print(users_serializer.errors)
        return JsonResponse("Failed to add", safe = False)
    elif request.method == "PUT":
        user_data = JSONParser().parse(request)
        user = User.objects.get(username = user_data['username'])
        users_serializer = UserSerializer(user, data = user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated Successfully", safe = False)
        return JsonResponse("Failed to update", safe = False)
    elif request.method == "DELETE":
        user = User.objects.get(id = id)
        user.delete()
        return JsonResponse("Deleted successfully", safe = False)

# LOGIN SCREEN
@csrf_exempt
def login(request, id = 0, *args, **kwargs):
    if request.method == "GET":
        users = User.objects.all()
        # User.objects.all().delete() # DO NOT UNCOMMENT. THIS IS TO CLEAR THE USER DB
        users_serializer = UserSerializer(users, many = True)
        return JsonResponse(users_serializer.data, safe = False)
    elif request.method == "POST":
        user_data = JSONParser().parse(request)
        try: 
            user = User.objects.get(username = user_data['username'])
            users_serializer = UserSerializer(user, data = user_data)
            #print(users_serializer.errors)
            if user.check_password(user_data['password']):
                return JsonResponse("User exists", safe = False)
            return JsonResponse("Wrong Password", safe = False)
        except:
            return JsonResponse("User does not exist", safe = False)

@csrf_exempt
def SaveFile(request):
    print(request.FILES)
    file = request.FILES['myFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe = False)