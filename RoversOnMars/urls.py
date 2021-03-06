"""RoversOnMars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from .views import home, sslcert
from curiosity import urls as urls_curiosity
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('curiosity/', include(urls_curiosity)),
    path('', include('pwa.urls')),
    path('\.well-known/', include('letsencrypt.urls')),
    path('.well-known/pki-validation/D4A8A9D509E77FB63021190BDE6DAD71.txt', sslcert),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
