from django.core.files.storage import default_storage
from django.db.models.functions import Length
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from json import dumps
from rest_framework.parsers import JSONParser

from django.contrib.auth.models import User
from .models import *
from .serializers import *

# Create your views here

def home(request):
    return HttpResponse("Home page for rec and ingred")

# Recipe creation with no linking to ingred. THIS IS DEPRECATED
@csrf_exempt
def recNoIngred(request, id = 0, *args, **kwargs):
    if request.method == "GET":
        recipes = Recipe.objects.all()
        # Recipe.objects.all().delete() # DO NOT UNCOMMENT. THIS IS TO CLEAR THE USER DB
        rec_serializer = RecSerializer(recipes, many = True)
        return JsonResponse(rec_serializer.data, safe = False)
    elif request.method == "POST": # Submission of recipes 
        rec_data = JSONParser().parse(request)
        rec_serializer = RecSerializer(data = rec_data)
        if rec_serializer.is_valid():
            rec_data["user_id"] = User.objects.get(id = rec_data["user_id"])
            Recipe.objects.create(**rec_data)
            return JsonResponse("Added Successfully", safe = False)
        print(rec_serializer.errors) # Print errors 
        return JsonResponse("Failed to add", safe = False)
    elif request.method == "PUT":
        rec_data = JSONParser().parse(request)
        rec = Recipe.objects.get(rec_name = rec_data['rec_name'])
        rec_serializer = RecSerializer(rec, data = rec_data)
        if rec_serializer.is_valid():
            rec_serializer.save()
            return JsonResponse("Updated Successfully", safe = False)
        return JsonResponse("Failed to update", safe = False)
    elif request.method == "DELETE":
        rec = Recipe.objects.get(id = id)
        rec.delete()
        return JsonResponse("Deleted successfully", safe = False)

# Ingred Creation
@csrf_exempt
def ingredView(request, id = 0, *args, **kwargs): 
    # No update/delete as this db should be fully created and unedited thereafter

    if request.method == "GET":
        ingredients = Ingredient.objects.all()
        # Ingredient.objects.all().delete() # DO NOT UNCOMMENT. THIS IS TO CLEAR THE USER DB
        ingred_serializer = IngredSerializer(ingredients, many = True)
        return JsonResponse(ingred_serializer.data, safe = False)
    elif request.method == "POST":
        ingred_data = JSONParser().parse(request)
        ingred_serializer = IngredSerializer(data = ingred_data)
        #ingred_data.pop('ingred_id', "required_default")
        if ingred_serializer.is_valid():
            Ingredient.objects.create(**ingred_data)
            return JsonResponse(f"Successfully added {ingred_data['ingred_name']}", safe = False)
        print(ingred_serializer.errors) # Print errors 
        return JsonResponse("Failed to add", safe = False)

# Verification view on whether an ingredient exists in our DB
@csrf_exempt
def verifyIngred(request): 
    if request.method == "GET":
        return JsonResponse("This page is for verifying ingredients", safe = False)
    elif request.method == "POST":
        ingred_data = JSONParser().parse(request) # Parse ingredient info
        keywords = ingred_data['ingred_name'].split()
        keywords_full = ' '.join(keywords)
        res = Ingredient.objects.all()
        for keyword in keywords: # Start filtering 
            res = res.filter(ingred_name__icontains = keyword)
        if len(res) > 1 and len(keywords) > 1: # If more than one result, we take the exact keyword 
            res = res.order_by(Length('ingred_name'))[0:1]
        elif len(keywords) == 1: # Filter for exact
            res = res.filter(ingred_name__iexact = keyword)
        if res.exists():
            res = IngredSerializer(res.get())
            return JsonResponse(res.data, safe = False)
        return JsonResponse("Does not exist", safe = False)

# Actual recipe creation page
@csrf_exempt
def recipeCreation(request): 
    if request.method == "GET":
        recipes = Recipe.objects.all()
        # Recipe.objects.all().delete() # DO NOT UNCOMMENT. THIS IS TO CLEAR THE USER DB
        rec_serializer = RecSerializer(recipes, many = True)
        return JsonResponse(rec_serializer.data, safe = False)
        # return JsonResponse("This page is for creating recipes", safe = False)
    elif request.method == "POST":
        rec_data = JSONParser().parse(request)
        ingredients = rec_data.pop('ingredients') # Take out the ingredients

        # First we create the recipe in Recipe table
        rec_serializer = RecSerializer(data = rec_data)
        if rec_serializer.is_valid(): # Validate
            rec_data["user_id"] = User.objects.get(id = rec_data["user_id"]) # Get the User for the foreign key
            Recipe.objects.create(**rec_data) # Create recipe
            recipe = Recipe.objects.latest('rec_id') # Store for later use
            # Then we iterate through the ingredients and make all the Requires entry
            for ingred_id, quantity in ingredients.items():
                ingredient = Ingredient.objects.get(ingred_id = ingred_id) # Get actual ingredient
                Requires.objects.create(ingred_id = ingredient, rec_id = recipe, quantity = quantity) # Create Requires entry
            return JsonResponse(f"Successfully added {recipe.rec_name}", safe = False)
        else: # For debugging 
            print(rec_serializer.errors)
        return JsonResponse("Failed to add",safe = False)

# Getting all the recipes of the user 
@csrf_exempt
def getUserRec(request):
    if request.method == "GET":
        return JsonResponse("This page is for getting recipes of a user", safe = False)
    elif request.method == 'POST':
        user_id = JSONParser().parse(request)['user_id']
        recipes = Recipe.objects.filter(user_id = user_id)
        rec_serializer = RecNameIdSerializer(recipes, many = True)
        return JsonResponse(rec_serializer.data, safe = False)

# Getting full recipe of the user with ingredients
@csrf_exempt
def getFullRecipe(request):
    if request.method == "GET":
        return JsonResponse("This page is for getting a full recipe with ingredients", safe = False)
    elif request.method == 'POST':
        rec_id = JSONParser().parse(request)['rec_id']
        recipe = Recipe.objects.filter(rec_id = rec_id)
        rec_serializer = RecNameIdSerializer(recipe)
        print(Requires.objects.filter(rec_id = rec_id))
        ingredients = Requires.objects.filter(rec_id = rec_id).values("ingred_id")
        print(ingredients.values())
        ingred_serializer = [] 
        # for value in ingredients.values():
        #     ingred_serializer.append(Ingredient.objects.get(ingred_id = value))
        # print(ingred_serializer)
        return JsonResponse("Incomplete", safe = False)