from django.urls import path
from finsure import views

urlpatterns = [
    path('', views.finsure_login, name='finsure_login'),
]