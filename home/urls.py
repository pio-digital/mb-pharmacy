# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path

from home.autocomplete import urls as autocomplete_urls

from . import views

urlpatterns = [
    path("pos-page/", views.POSView.as_view(), name="pos_page"),
    path("sales-report-page/", views.ReportView.as_view(), name="sales_report_page"),
    *autocomplete_urls,
]
