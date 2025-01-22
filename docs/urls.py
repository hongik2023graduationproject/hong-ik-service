from django.urls import path
from .views import docs_home

app_name = 'docs'
urlpatterns = [
    path('', docs_home, name='home'),
]