from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def saveFile(request):
    # print(request.FILES)
    try:
        file = request.FILES['pic']
        file_name = default_storage.save(file.name, file)
        return JsonResponse(file_name, safe = False)
    except:
        return JsonResponse("This is a secured page", safe = False)