from django.urls import path
from finsure import views

urlpatterns = [
    path('', views.finsure_login, name='finsure_login'),
    path('', views.finsure_finances, name='finsure_finances'),
    path('', views.finsure_otp, name='finsure_otp'),
    path('', views.xyz_login, name='xyz_login'),
    path('', views.xyz_loan, name='xyz_loan'),
    path('', views.xyz_accepted, name='xyz_accepted'),
    path('', views.xyz_rejected, name='xyz_rejected'),
]