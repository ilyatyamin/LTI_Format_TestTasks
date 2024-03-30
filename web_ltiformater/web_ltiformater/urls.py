"""
URL configuration for web_ltiformater project.

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
from django.urls import path

from entries import views

urlpatterns = [
    path("", views.mainpage, name='home'),
    path("result/", views.send_form_postrequest),
    path("result/download_file/", views.download_file, name="download_file"),

    path("ajax/reload_form", views.reload_page, name = 'reload_page')
]
