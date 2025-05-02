from django.urls import path
from .import views

# Urls are here
urlpatterns = [
    path('',views.register,name='register'),
    path('login',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard')
]