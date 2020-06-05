"""covaid19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="corona"),
    path('corona/home/',views.home,name="corona"),
    path('corona/contact',views.contact,name="corona"),
    path('corona/graph/',views.graph,name="corona"),
    path('corona/news/',views.news,name="corona"),
    path('corona/mythbuster/',views.mythbuster,name="corona"),
    path('corona/helpline/',views.helpline,name="corona"),
    path('corona/safety/',views.safety,name="corona"),
    path('corona/precaution/',views.precaution,name="corona"),
    path('corona/country_graph/',views.country_graph,name="corona"),
    path('corona/state_graph/',views.state_graph,name="corona"),
   
    
    
    
]
        