from django.contrib import admin
from django.urls import path

from .views import (
    SignUpView
)

app_name = 'accounts' # Remember to set the app name

urlpatterns = [ 
    path('signup/', SignUpView.as_view(), name='signup'),
]
