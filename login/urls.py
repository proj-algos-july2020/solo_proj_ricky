from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('registration', views.registration),
    path('registered', views.registered),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
]