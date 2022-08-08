from pathlib import Path
from django import views
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.Home),
    path('get/<str:param>',views.lang),
    path('get/<str:param>/<str:topic>',views.top_Head),
    path('autorities/login',views.load_login),
    path('userlogin',views.load_login,name ="home_login"),
    path('signup',views.load_login,name='signup'),
    path('signup',views.load_login,name='forgot_pass'),
    path('addnews',views.addnews,name='addnews'),
    path('create',views.create_news,name= 'create_news'),

]