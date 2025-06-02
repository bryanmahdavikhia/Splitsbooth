from django.urls import path
from .views import activities_view, select_activity

app_name = 'list_activities'
urlpatterns = [
    path('', activities_view, name='activities'),
    path('select/', select_activity, name='select')
]
