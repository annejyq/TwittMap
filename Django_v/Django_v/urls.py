"""Django_v URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Django_v.views import tweeterAPI,search,geosearch

urlpatterns = [
    url(r'^$', tweeterAPI),                 #Main Page, including Google map and UI
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ajax/search/$',search),     #Search based on keywords
    url(r'^ajax/geosearch/$',geosearch),     #Search based on location
]
