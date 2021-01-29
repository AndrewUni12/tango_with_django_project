# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:10:56 2021

@author: Andrew
"""

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path(r'about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category'),
]