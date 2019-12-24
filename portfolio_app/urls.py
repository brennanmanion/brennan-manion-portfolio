from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('data-science/',views.data_science),
    path('full-stack/',views.full_stack),
    path('automation/',views.automation),
    path('trading/',views.trading),
    path('reading/',views.reading),
    path('entrepreneurship/',views.entrepreneurship),
    path('tutorials/',views.tutorials),
    path('weightlifting/',views.weightlifting),
    path('snowboarding/',views.snowboarding),
    path('music/',views.music),
    path('longboarding/',views.longboarding)
]
