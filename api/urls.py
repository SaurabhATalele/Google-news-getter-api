from pathlib import Path
from django import views
from django.urls import URLPattern, path
from . import views

urlpatterns = {
    path('',views.Home),
    path('get/<str:param>',views.lang),
    path('get/<str:param>/<str:topic>',views.top_Head),
}