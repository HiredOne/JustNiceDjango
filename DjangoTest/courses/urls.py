from django.contrib import admin
from django.urls import path

from .views import (
    CourseView,
    CourseListView
    # my_fbv
)

app_name = 'courses' # Remember to set the app name

urlpatterns = [ 
    # Here modifying the template_name allows us to show a completely different
	# template while using the same view

    # path('', my_fbv, name = 'courses-list'), #FBV variant
    # path('', CourseView.as_view(template_name = 'contact.html'), name = 'courses-list'),
    path('', CourseListView.as_view(), name = 'courses-list'),
    path('<int:id>/', CourseView.as_view(), name = 'courses-det'),
    # path('create/', ArticleCreateView.as_view(), name = 'article-create'),
    # path('<int:id>/delete/', ArticleDeleteView.as_view(), name = 'article-del'),
    # path('<int:id>/update/', ArticleUpdateView.as_view(), name = 'article-upd'),
]
