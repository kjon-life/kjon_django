"""
URL configuration for kjon_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django_otp.admin import OTPAdminSite


# ↓ New basic view returning "Hello, kjon!" ↓
#def hello(request):
#    return HttpResponse("Hello, kjon!")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('hello.urls')),  # Include hello
]

# Enforce 2FA only in production from DEBUG check
if not settings.DEBUG:
    admin.site.__class__ = OTPAdminSite