from django.urls import path
from finsure import views

urlpatterns = [
    path('', views.finsure_login, name='finsure_login'),
    path('', views.finsure_finances, name='finsure_finances'),
    path('', views.finsure_otp, name='finsure_otp'),
]