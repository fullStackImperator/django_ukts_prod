from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'magazin'


urlpatterns = [
    # login

    path('', views.FilesView.as_view(), name="magazin_brojevi"),
    path('istorija/', views.IstorijaMagazinView.as_view(), name="magazin_istorija"),
    path('brojevi/', views.FilesView.as_view(), name="magazin_brojevi"),
]
