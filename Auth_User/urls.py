from django.urls import path
from . import views

app_name = 'Login'

urlpatterns = [
    path('login/', views.User_login, name='login'),
    path('registration/', views.User_Registration, name='registration')
]
