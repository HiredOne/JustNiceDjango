from django.contrib import admin
from django.urls import path
from .views import * # IMPORT THE VIEWS
from Accounts.views import saveFile

from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings

app_name = 'RecIngred' # Remember to set the app name

urlpatterns = [
    # path('', home_view, name = 'home'),
    # path('api/lead/', LeadListCreate.as_view()), #CBV 
    path('', home), #CBV 
    # path('recipe/', recNoIngredView), # Deprecated 
    # path('recipe/<int:id>/', recNoIngredView), # Deprecated 
    path ('recipe/', recipeCreation),
    path('checkingred/', verifyIngred),
    path('ingred/', ingredView),
    path('uploadphoto/', saveFile)
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
