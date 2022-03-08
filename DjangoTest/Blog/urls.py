from django.contrib import admin
from django.urls import path

from .views import (
    ArticleDetailView,
    ArticleDeleteView,
    ArticleListView,
    ArticleCreateView,
    ArticleUpdateView
)

app_name = 'Blog' # Remember to set the app name

# Note: pk refers to primary key, but it's also the id assigned to the obj
# Note2: Pass the view in as <viewName>.as_view()

urlpatterns = [ 
    path('', ArticleListView.as_view(), name = 'article-list'),
    path('create/', ArticleCreateView.as_view(), name = 'article-create'),
    path('<int:id>/', ArticleDetailView.as_view(), name = 'article-det'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name = 'article-del'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name = 'article-upd'),
]
