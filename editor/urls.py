from django.urls import path
from .views import editor_view, execute_code

app_name = 'editor'
urlpatterns = [
    path('', editor_view, name='home'),
    path('execute_code/', execute_code, name='execute_code'),
]
