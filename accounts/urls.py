from django.urls import path
from .views import signup , user_activate , profile
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup/',signup , name = 'signup'),
    path('profile/',profile , name = 'profile'),
    path('<str:username>/activate',user_activate , name = 'user_activate'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),

    
    ]