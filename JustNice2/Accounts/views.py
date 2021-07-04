from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from json import dumps

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, UserManager
from .serializers import UserSerializer

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
        user_data.pop('id', "required_default")
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
        if 'password' in user_data:
            new_pwd = make_password(user_data['password'])
            user_data['password'] = new_pwd
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
        res = {"status" : -1}
        try: 
            # user = authenticate(username = user_data['username'], password = user_data['password'])
            user = User.objects.get(username = user_data['username'])
            users_serializer = UserSerializer(user, data = user_data)
            if users_serializer.is_valid() and user.check_password(user_data['password']):
                res["status"] = 1
                res["user"] = users_serializer.data
                return JsonResponse(res, safe = False)
            res["status"] = 0
            return JsonResponse(res, safe = False)
        except:
            return JsonResponse(res, safe = False)

# Verification view on whether a user exists in our DB
@csrf_exempt
def verifyUser(request): 
    if request.method == "GET":
        return JsonResponse("This page is for verifying users", safe = False)
    elif request.method == "POST":
        username = JSONParser().parse(request)['username'] # Parse info and get username
        user = User.objects.filter(username = username) # Search directly
        res = {"status" : "Does not exist"}
        if user.exists():
            res['user'] = UserSerializer(user.get()).data
            res['status'] = 'Exist'
            return JsonResponse(res, safe = False)
        return JsonResponse(res, safe = False)