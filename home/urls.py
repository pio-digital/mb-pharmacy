# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("pos-page/", views.POSView.as_view(), name="pos_page"),
    path("search/", views.SearchView.as_view(), name="search"),
]
