from django.db.models.functions import Length
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from json import dumps
from rest_framework.parsers import JSONParser

from django.contrib.auth.models import User
from .models import *
from .serializers import *
from RecIngred.serializers import *
from RecIngred.models import *
from RecIngred.views import getFullRecipe

# Create your views here.

def home(request):
    return HttpResponse("Home page for grocery list")

def grocListGetter(request, id = 0): # This is for putting an empty list/ getting all the lists
    if request.method == "GET":
        converts = Converts.objects.filter(user_id = id).distinct('list_id')
        # converts.objects.all().delete() # DO NOT UNCOMMENT. THIS IS TO CLEAR THE USER DB
        conv_serializer = ConvListIdSerializer(converts, many = True)
        return JsonResponse(conv_serializer.data, safe = False)
    elif request.method == "POST": # Creating empty groc list 
        conv_data = JSONParser().parse(request)
        user_id, list_id = conv_data['user_id'], conv_data['list_id']
        user = User.objects.get(user_id = user_id) # Get the user 
        rec = Recipe.objects.get(rec_id = 1)
        ingred = Ingredient.objects.get(ingred_id = 1)
        Converts.objects.create(user_id = user, rec_id = rec, ingred_id = ingred, ingred_quantity = 0, )
        return JsonResponse("New list created")
    return JsonResponse("An error has occurred", safe = False)

def grocListUpdater(request, id = 0): # This is for putting stuff into the list and for getting a list 
    if request.method == "GET": # Get the entire list 
        converts = Converts.objects.filter(list_id = id)
        # converts.objects.all().delete() # DO NOT UNCOMMENT. THIS IS TO CLEAR THE USER DB
        conv_serializer = ConvListIdSerializer(converts, many = True)
        return JsonResponse(conv_serializer.data, safe = False)
    elif request.method == 'POST':
        conv_data = JSONParser().parse(request) # First we parse the data
        res = {} # Final result 
        # Iterate through the recipes
        for rec_id, rec_quantity in conv_data.items(): 
            ingredients = getFullRecipe({"rec_id" : rec_id})["ingredients"] # Get the ingredients and qty needed
            for ingredient in ingredients:
                cat = ingredient['ingred_cat']
                if cat in res:
                    res


