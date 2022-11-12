from django.urls import path
from . import views


urlpatterns = [
   path('login/', views.loginPage , name = 'login' ),
    path('loggedout/', views.logoutUser , name = 'logout' ),
    path('register/', views.registerUser , name = 'register' ),
]