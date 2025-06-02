from django.urls import path
from .views import input_view

app_name = 'home'
urlpatterns = [
    path('', input_view, name='input')
]
