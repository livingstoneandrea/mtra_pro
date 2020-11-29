from django.shortcuts import get_object_or_404, render
from django.urls import reverse,reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect, JsonResponse
from django.core import serializers
from accounts.models import Education_level, Employment_detail, File_uploaded, Preference, User
from django.views.generic import (TemplateView,CreateView,DetailView,ListView,View,UpdateView,DeleteView)
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts import forms
from accounts.forms import Education_levelForm, Employement_DetailForm, File_UploadForm, Preference_Form, UserProfileForm
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.http import HttpResponseForbidden
from django.contrib import messages
from notifications.signals import notify
User = get_user_model()

# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signUp.html'
    
    # def form_valid(self,form):
    #     user = form.save()
    #     # Trigger message sent to group
    #     channel_layer = get_channel_layer()
    #     data = "notification"+ ".New user "+user.username+" has joined @ -." + str(datetime.now())
    #     async_to_sync(channel_layer.group_send)(
    #         "user_notifier",  # Group Name, Should always be string
    #         {
    #             "type": "new_userNotifier",   # Custom Function written in the consumers.py
    #             "event":"New User",
    #             "text": data,
    #         },
    #     ) 
    #     return super(CreateView,self).form_valid(form)   
        
class Login(LoginView):
    authentication_form = forms.CustomAuthentictaionForm
    form_class = forms.CustomAuthentictaionForm
    template_name = 'accounts/login.html'

    
    def form_valid(self, form):
        login(self.request,form.get_user())
        
        return super(LoginView,self).form_valid(form)
    
class Profile(LoginRequiredMixin,FormMixin , View):
    model = User
    template_name = 'accounts/profile.html'
    form = None
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return User.objects.filter(user=self.request.user)
        else:
            return User.objects.none()
    def get_object(self, queryset=None):
        return get_object_or_404(get_user_model(),id = self.request.user.id) 
       
   
    def get_context_data(self, **kwargs):
        context = {}
        
        try:
            context['emp_info'] = Employment_detail.objects.none()
        except :
            context['emp_info'] = UserProfileForm()
        try:
            context['profile_form'] = UserProfileForm(instance = self.get_object())
        except :
            context['profile_form'] = UserProfileForm()
        try:
            context['edu_detailform'] = Education_levelForm(instance=Education_level.objects.filter(user=self.request.user).first())
        except :
            context['edu_detailform'] = Education_levelForm()
        try:
            context['emp_detailform'] = Employement_DetailForm(instance=Employment_detail.objects.all().filter(user=self.request.user).first())
        except :
            context['emp_detailform'] = Employement_DetailForm()
        try:
            context['pref_form'] = Preference_Form(instance=Preference.objects.filter(user=self.request.user).first())
        except :
            context['pref_form'] = Preference_Form()         
        try:
            context['file_uploadform'] = File_UploadForm(instance=File_uploaded.objects.filter(user=self.request.user).first())
        except :
            context['file_uploadform'] = File_UploadForm()  
        
        return context 
    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name,self.get_context_data())
    def post(self, request, *args, **kwargs):
        if self.request.is_ajax and self.request.method == "POST":
            if 'edu_details' in request.POST:
                #get profile form
                try:
                    form = Education_levelForm(self.request.POST,instance=Education_level.objects.filter(user=self.request.user).first())
                except:
                    form = Education_levelForm(self.request.POST)
                
            elif 'emp_details' in request.POST:
                try:
                    form = Employement_DetailForm(self.request.POST,instance=Employment_detail.objects.filter(user=self.request.user).first())
                except:
                    form = Employement_DetailForm(self.request.POST)
            elif 'pref_info' in request.POST:
                try:
                    form = Preference_Form(self.request.POST,instance=Preference.objects.filter(user=self.request.user).first())
                except:
                    form = Preference_Form(self.request.POST)
            elif 'file_upload' in request.POST:
                try:
                    form = File_UploadForm(self.request.POST,self.request.FILE,instance=File_uploaded.objects.filter(user=self.request.user).first())
                except:
                    form = File_UploadForm(self.request.POST)
            else:
                form = UserProfileForm(self.request.POST,instance=self.get_object())
                              
            if form.is_valid():
                instance = form.save(commit = False)
                instance.user = self.get_object()
                instance.save()
                # invoke websocket- send data to client
                current_user = request.user # Getting current user
                channel_layer = get_channel_layer()
                data = "notification"+ "..added some details.." + str(timezone.now()) # Pass any data based on your requirement
                # Trigger message sent to group
                async_to_sync(channel_layer.group_send)(
                    str(current_user.pk),  # Group Name, Should always be string
                    {
                        "type": "notify",   # Custom Function written in the consumers.py
                        "text": data,
                    },
                )
                notify.send(self.get_object(),recipient=self.get_object(), verb="notification  :"+ "your profile succesful updated @ " +str(datetime.now()) )
                
                
                #send to client side
                return JsonResponse({"message":"Your details submmitted & proccessed succeful","user":serializers.serialize('json',[instance,])},status=200)
            else:
                return JsonResponse({"errors":form.errors},status=400)
        return JsonResponse({"errors":""},status=400)    
        
class UserDeleteView(DeleteView):
    model = get_user_model()
    success_url = '/'
    template_name = None
    def delete(self, request, *args,**kwargs):
        self.object = self.get_object()
        if request.is_ajax():
            print("Ajax request in delete")
        
            if self.object.User == request.user:
                success_url = self.get_success_url()
                self.object.delete();
                HttpResponseRedirect(success_url)
                
                return JsonResponse({"message":"You have deleted your account"},status=200)
            else:
                HttpResponseForbidden("Cannot delete the user")
                
                return JsonResponse({"errors":""},status=400) 
            
def del_user(request,pk):
    if request.is_ajax():
        print("Ajax request in delete")
        try:
            user = User.objects.get(pk = pk)
            success_url = '/'
            user.delete()
            messages.success(request,'The user is deleted')
            HttpResponseRedirect(success_url)        
            return JsonResponse({"message":"You have deleted your account"},status=200)
            
        except User.DoesNotExist:
            return JsonResponse({"errors":"User does not exist"},status=400) 
        except Exception as e:
            return JsonResponse({"errors":str(e.message)},status=400)
        
                