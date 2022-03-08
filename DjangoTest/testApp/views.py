from django.shortcuts import render, get_object_or_404, redirect
from .forms import TestForm, RawTestForm
from .models import TestApp

# Create your views here.

def test_list_view(request): # For displaying all users 
    queryset = TestApp.objects.all() # List of objects
    context = {
        "objList" : queryset
    }
    return render(request, "products/test_list.html", context)


def test_detail_view(request, my_id): # For displaying 1 user
    #obj = TestApp.objects.get(id = my_id)    
    obj = get_object_or_404(TestApp, id = my_id)
    context = {
        'object' : obj
    }
    return render(request, "products/test_detail.html", context)

def test_create_view(request): # This is for creating users 
    form = TestForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TestForm()
    context = {
        'form' : form
    }
    return render(request, "products/test_create.html", context)

def test_delete_view(request, my_id): # For deleting users 
    obj = get_object_or_404(TestApp, id = my_id)
    if request.method == 'POST':
        # Confirming delete
        obj.delete()
        return redirect('../../')
    context = {
        'object' : obj
    }
    return render(request, "products/test_delete.html", context)

def test_update_view(request, my_id): # For updating user credentials
    obj = get_object_or_404(TestApp, id = my_id)
    # form = TestForm(request.POST or None, initial = initial_data)
    form = TestForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request, "products/test_create.html", context)

def render_initial_data(request): # This view was used to test initial data
    initial_data = {
        'title' : "Some init title"
    }
    obj = TestApp.objects.get(id = 1)
    # form = TestForm(request.POST or None, initial = initial_data)
    form = TestForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request, "products/test_create.html", context)
    
def test_login_view(request): # Some test login view (obsolete)
    userName = request.POST.get("Username")
    userPwd = request.POST.get("Password")
    #TestApp.objects.create(title = userName, description = userPwd, price = 0.0)
    return render(request, "products/test_login.html", {})

def dynamic_lookup_view(request, my_id): # This is the test_detail_view
    #obj = TestApp.objects.get(id = my_id)    
    obj = get_object_or_404(TestApp, id = my_id)
    context = {
        'object' : obj
    }
    return render(request, "products/test_detail.html", context)


# def test_create_view(request):
#     my_form = RawTestForm()
#     if request.method == 'POST':
#         my_form = RawTestForm(request.POST)
#         if my_form.is_valid():
#             # Data is good
#             print(my_form.cleaned_data)
#             #TestApp.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form" : my_form
#     }
#     return render(request, "products/test_create.html", context)

# def test_create_view(request):
#     print(request.GET)
#     print(request.POST)
#     context = {}
#     return render(request, "products/test_create.html", context)