from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.treneri_form, name='treneri_form'), # get and post request for insert operation
    path('<int:id>', views.treneri_form, name='treneri_update'), # get and post req for update operation
    path('list/', views.treneri_list, name='treneri_list'), # get req to retrieve and display recs
    path('delete/<int:id>', views.treneri_delete, name='treneri_delete'), # 
    
    path('bcb-upload/', views.uploadBCBView, name="bcb_upload"),
    path('td-upload/', views.uploadTDView, name="td_upload"),

    path('export_csv', views.export_csv, name='export_csv'),  
    path('export_excel', views.export_excel, name='export_excel'),
    path('export_pdf', views.export_pdf, name='export_pdf'),

    # path('slike-upload', views.slike_form, name='slike_form'),

    path('search-trener/', views.main_search_view, name='search_trener'), 
    path('search-trener/search/', views.search_results, name='search'), 
    path('search-trener/search/<pk>', views.trener_detail_view, name='detail'), 

    
    path('test/', views.TestView.as_view(), name='test'), 

]
