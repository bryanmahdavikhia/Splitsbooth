from django.urls import path
from .views import frame_view

app_name = 'list_frame'
urlpatterns = [
    path('', frame_view, name='frames')
]
