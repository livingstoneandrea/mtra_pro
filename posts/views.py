from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (ListView,DetailView,CreateView,DeleteView)
from . import models
from . import forms

from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

class Blog_PostListView(ListView):
    model = models.Blog_post
    template_name = "posts/post_list.html"
class Blog_PostDetail(DetailView):
    model = models.Blog_post
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.kwargs.get('blog_id'))
    
class CreatePost(LoginRequiredMixin,CreateView):
    fields = ('') 
    model = models.Blog_post
    
    def form_valid(self,form):
        self.object = form.save(commit=False) 
        self.object.user = self.request.user
        self.object.save()  
        return super().form_valid(form)
    
class DeletePost(LoginRequiredMixin, DeleteView):
    model = models.Blog_post
    success_url = reverse_lazy('home')
    def get_queryset(self):
        return super().get_queryset().filter(post_id = self.kwargs.get('post_id'))
    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post Deleted')
        return super.delete(*args,**kwargs)        
    
