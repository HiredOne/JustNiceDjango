from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    #return HttpResponse("<h1>Hello World</h1>") # String of HTML code
    return render(request, "home.html", {})