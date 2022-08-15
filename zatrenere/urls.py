from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'zatrenere'


urlpatterns = [
    # login

    # path('', views.KlinikaView.as_view(), name="klinike"),
    path('planeri/', views.PlaneriView.as_view(), name="planeri"),
    path('lekarski/', views.LekarskiView.as_view(), name="lekarski"),
    path('obrasci-uplatnice/', views.UplatniceView.as_view(), name="uplatnice"),
    path('aplikacija/', views.AplikacijaView, name="aplikacija"),

]
