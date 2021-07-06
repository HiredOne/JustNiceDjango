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
        file = request.FILES['pic'] # Get the file 
        if "png" in file.name:
            filename = request.POST['filename'] + ".png" # Get filename
        elif "jpg" in file.name:
            filename = request.POST['filename'] + ".jpg" # Get filename
        elif "jpeg" in file.name:
            filename = request.POST['filename'] + ".jpeg" # Get filename
        file_name = default_storage.save(filename, file)
        return JsonResponse(file_name, safe = False)
    except:
        return JsonResponse("This is for photo uploading", safe = False)

@csrf_exempt
def updatePhoto(request): # For updating user/rec photo
    try:
        res = {"url" : default_storage.url('default.jpg')} # URL to default photo
        res['status'] = 'default' # Status of photo

        # First we find (if existing) old photo and get the url
        filename = request.POST['filename'] 
        if default_storage.exists(filename + ".png"):
            old_filename = filename + ".png"
            res['url'] = default_storage.url(old_filename)
            res['status'] = 'old' # Update status
        elif default_storage.exists(filename + ".jpg"):
            old_filename = filename + ".jpg"
            res['url'] = default_storage.url(old_filename)
            res['status'] = 'old' # Update status
        elif default_storage.exists(filename + ".jpeg"):
            old_filename = filename + ".jpeg"
            res['url'] = default_storage.url(old_filename)
            res['status'] = 'old' # Update status

        # Next, we parse the new photo
        file = request.FILES['pic'] # Get the photo
        # Make new filename
        if "png" in file.name:
            new_filename = filename + ".png"
        elif "jpg" in file.name:
            new_filename = filename + ".jpg"
        elif "jpeg" in file.name:
            new_filename = filename + ".jpeg"

        # After confirming new photo is ready for upload, delete the old one
        default_storage.delete(old_filename)
        
        # Now we upload the new one 
        new_filename = default_storage.save(new_filename, file)
        res['url'] = default_storage.url(new_filename)
        res['status'] = 'new' # Update status
        return JsonResponse(res, safe = False)
    except:
        return JsonResponse(res, safe = False)

@csrf_exempt
def getPhoto(request): # Photo retrieval
    try:
        res = {"url" : default_storage.url('default.jpg')} # URL to default photo
        filename = JSONParser().parse(request)['filename']
        if default_storage.exists(filename + ".png"):
            res['url'] = default_storage.url(filename + ".png")
        elif default_storage.exists(filename + ".jpg"):
            res['url'] = default_storage.url(filename + ".jpg")
        elif default_storage.exists(filename + ".jpeg"):
            res['url'] = default_storage.url(filename + ".jpeg")
        return JsonResponse(res, safe = False)    
    except:
        return JsonResponse(res, safe = False)