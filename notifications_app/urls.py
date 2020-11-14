from django.urls import path,include
from notifications_app import views
from django.http import request


app_name = 'notifications_app'

urlpatterns = [
    path('',views.NotificationView.as_view(),name='notifier'),
    
]