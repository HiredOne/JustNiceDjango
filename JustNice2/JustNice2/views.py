from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from json import dumps, load, loads

from django.contrib.auth.models import User
from RecIngred.models import *
from data.dataparser import read_csv

# Create your views here

# This view is used to populate the db with the desired stuff 
@csrf_exempt
def populate(request):
    try:
        rows = load(open("C:/Users/Anthony/dev/JustNice2/data/ingredients.json")).values()
        # print(Ingredient(**rows[0]).save())
        for row in rows:
            ingred = Ingredient(**row).save()
            print(ingred)
        return JsonResponse("Ingredients added", safe = False)
    except:
        return JsonResponse(f"Failed to add {ingred}", safe = False)
