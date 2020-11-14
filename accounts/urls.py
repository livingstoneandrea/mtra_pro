from django.urls import path,include
from accounts import views
from django.contrib.auth import views as auth_views
from .forms import CustomAuthentictaionForm
from django.http import request


app_name = 'accounts'

urlpatterns = [
    path('login/',views.Login.as_view(),name='login'),
    path('signup/',views.SignUp.as_view(),name='register'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('profile/',views.Profile.as_view(),name='profile'),
    path('<pk>/delete/',views.del_user,name='delete')
    
]