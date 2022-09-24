from django.urls import path

from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'


urlpatterns = [
    # login
    # path('register/', views.registerPage, name="register"),
    # path('login/', views.loginPage, name="login"),
    # path('logout/', views.logoutUser, name="logout"),

    # post views
    # path('login/', views.loginPage, name="login"),
    path('', views.home_view, name='post_list'),
    path('vesti', views.vesti_list, name='vesti'),
    path('tag/<slug:tag_slug>/', views.home_view, name='post_list_by_tag'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
    path('comment/reply/', views.reply_page, name="reply"),
]
