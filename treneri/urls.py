from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.treneri_form, name='treneri_form'), # get and post request for insert operation
    path('<int:id>', views.treneri_form, name='treneri_update'), # get and post req for update operation
    path('list/', views.treneri_list, name='treneri_list'), # get req to retrieve and display recs
    path('delete/<int:id>', views.treneri_delete, name='treneri_delete'), # 
    path('export_csv', views.export_csv, name='export_csv'),
]
