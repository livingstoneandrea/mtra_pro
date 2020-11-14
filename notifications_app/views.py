from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class NotificationView(TemplateView):
    template_name = 'accounts/notifier.html'
