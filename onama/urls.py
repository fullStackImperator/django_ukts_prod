from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'onama'


urlpatterns = [
    # login

    # path('', views.KlinikaView.as_view(), name="klinike"),
    path('statut/', views.StatutView.as_view(), name="statut"),
    path('pravilnik-o-izdavanju-dozvole-za-rad/', views.PravilnikView.as_view(), name="pravilnik"),
    path('kodeks/', views.KodeksView.as_view(), name="kodeks"),
    path('istorijat/', views.IstorijatView.as_view(), name="istorijat"),
    path('zivotno-delo/', views.ZivotnoDeloView.as_view(), name="zivotno_delo"),
    # path('zivotno-delo/', views.ZivotnoDelo, name="zivotno_delo"),
    path('clanovi-uo/', views.ClanoviUOView.as_view(), name="clanovi_uo"),

    path('kontakt', views.KontaktView.as_view(), name="kontakt"),

    path('faq', views.FaqView.as_view(), name="faq"),

    # path('nagrada-za-zivotno-delo', views.IstorijaBCBView.as_view(), name="istorija_bcb"),
    # path('vesti/', views.IstorijaTDView.as_view(), name="istorija_td"),


]
