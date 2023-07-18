from django.shortcuts import render
from django.urls import path
from users.views import SignInView, signOutView, signUpView
app_name = 'users'
urlpatterns =[
    path('sign-in/', SignInView.as_view(), name = 'sign-in'),
    path('sign-out/',signOutView.as_view(), name = 'sign-out' ),
    path('sign-up/', signUpView.as_view(), name = 'sign-up')
]