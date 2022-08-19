from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'klinike'


urlpatterns = [
    # login

    path('', views.KlinikaView.as_view(), name="klinike"),
    path('klinika-bcb/', views.KlinikaView.as_view(), name="klinika_bcb"),
    path('trenerski-dani/', views.TrenerskiDaniView.as_view(), name="trenerski_dani"),

    # path('klinika-bcb-galerija/', views.GalerijaBCBView.as_view(), name="galerija_bcb"),
    path('klinika-bcb-galerija/', views.GalerijaBCBView, name="galerija_bcb"),
    path('klinika-td-galerija/', views.GalerijaTDView, name="galerija_td"),

    # path('klinika-bcb-galerija/upload', views.addPhotoBCB, name="galerija_bcb_upload"),
    # path('klinika-td-galerija/upload', views.GalerijaTDView.as_view(), name="galerija_td_upload"),

    # path('klinika-bcb-istorija/', views.IstorijaBCBView.as_view(), name="istorija_bcb"),
    # path('klinika-td-istorija/', views.IstorijaTDView.as_view(), name="istorija_td"),


]
