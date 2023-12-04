"""DjangoAdmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include 
import users
from django.conf import settings
from django.conf.urls.static import static

handler500 = 'users.views.view_500'
handler403 = 'users.views.view_403'
handler404 = 'users.views.view_404'

urlpatterns = [
    path('', include('users.urls', namespace='users')),
    path('foods/', include('foods.urls', namespace='foods')),
    path('api/', include('foods.api.urls', namespace='api')),
    path('api/', include('users.api.urls', namespace='api')),
    path('register/', users.views.registration_view, name='registration'),
    path('logout/', users.views.logout_view, name='logout'),
    path('login/', users.views.login_view, name='login'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
