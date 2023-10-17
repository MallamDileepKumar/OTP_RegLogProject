from django.urls import path
from OTP_RegLogApp import views

urlpatterns = [
    path('',views.Home.as_view()),
    path('reg/',views.Regview.as_view()),
    path('reg/otp/',views.OTPView.as_view()),
]