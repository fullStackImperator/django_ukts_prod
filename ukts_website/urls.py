"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from blog.sitemaps import PostSitemap

from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)


sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('', views.index, name='index'),
    path('', include('blog.urls', namespace='blog')),

    path('treneri/',  include(('treneri.urls', 'treneri'), namespace='treneri')),

    path('o-nama/', include(('onama.urls', 'onama'), namespace='onama')),

    path('za-trenere/', include(('zatrenere.urls', 'zatrenere'), namespace='zatrenere')),

    path('magazin/', include(('magazin.urls', 'magazin'), namespace='magazin')),

    path('klinike/', include(('klinike.urls', 'klinike'), namespace='klinike')),

    path('edukacija/', include(('edukacija.urls', 'edukacija'), namespace='edukacija')),
    
    # path('blog/', include('blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('ckeditor/',include('ckeditor_uploader.urls')),

    path('account/', include(('account.urls', 'account'), namespace='account')),  

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "ukts_website.exception.handler404"