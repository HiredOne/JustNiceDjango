from django.contrib import admin
from django.urls import path
from pages.views import home_view
from .views import (
    LeadListCreate,
    UserListCreate
)

app_name = 'leads' # Remember to set the app name

urlpatterns = [
    path('', home_view, name = 'home'),
    path('api/lead/', LeadListCreate.as_view()), #CBV 
    path('api/user/', UserListCreate.as_view()), #CBV 
]
