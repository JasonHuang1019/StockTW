# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 11:09:29 2021

@author: Huang
"""

from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('stock/', views.stock_list),
]