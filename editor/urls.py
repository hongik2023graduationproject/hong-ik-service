from django.urls import path
from .views import editor_view

app_name = 'editor'
urlpatterns = [
    path('', editor_view, name='home'),
]
