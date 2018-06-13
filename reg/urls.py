from django.urls import path
from reg import views


app_name = 'index'
urlpatterns = [
    path('', views.main, name='index'),
]