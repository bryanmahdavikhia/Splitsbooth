from django.urls import path
from . import views

urlpatterns = [
    path('', views.oauth_input, name='oauth_input'),
]