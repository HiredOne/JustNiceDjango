from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    #return HttpResponse("<h1>Hello World</h1>") # String of HTML code
    return render(request, "home.html", {}) 

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 456, 789, "abc"]
    }
    return render(request, "about.html", my_context)