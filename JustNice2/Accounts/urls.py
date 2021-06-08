from django.contrib import admin
from django.urls import path
from .views import userApi, SaveFile, login

from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from JustNice2 import settings


app_name = 'Accounts' # Remember to set the app name

urlpatterns = [
    # path('', home_view, name = 'home'),
    # path('api/lead/', LeadListCreate.as_view()), #CBV 
    path('api/user/', userApi), #CBV 
    path('api/user/login/', login),
    path('api/user/<int:id>/', userApi),
    #path('api/SaveFile/', SaveFile)
    url(r'api/SaveFile$', SaveFile),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
