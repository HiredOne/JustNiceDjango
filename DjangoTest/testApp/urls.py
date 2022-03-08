from django.contrib import admin
from django.urls import path
from testApp.views import (test_detail_view, test_create_view,
    test_login_view, render_initial_data,
    dynamic_lookup_view, test_delete_view,
    test_list_view, test_update_view)

app_name = 'testApp'

urlpatterns = [ 
    path('', test_list_view, name = 'product-list'),
    path('<int:my_id>/', test_detail_view, name = 'product-det'),
    path('<int:my_id>/delete/', test_delete_view, name = 'product-del'),
    path('<int:my_id>/update/', test_update_view, name = 'product-upd'),
]
