from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.forms import ModelForm
from accounts.models import Education_level, Employment_detail, File_uploaded, Preference, Subscribers, User
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email',)
        
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ('email',)  
class CustomAuthentictaionForm(AuthenticationForm):
    username = forms.CharField(widget= forms.EmailInput(attrs={'class':'field_input','placeholder':'Email e.g(you@example.com)','required':True,'autofocus':True}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class':'field_input','placeholder':'password','required':True}))
   
   
             
class UserCreateForm(CustomUserCreationForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'user name','class':'field_input','required':True,'autofocus':True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email(e.g you@example.com)','class':'field_input','required':True}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'phone','class':'field_input','required':True}))
    password1 = forms.CharField(widget= forms.PasswordInput(attrs={'class':'field_input','placeholder':'password','required':True}))
    password2 = forms.CharField(widget= forms.PasswordInput(attrs={'class':'field_input','placeholder':'confirm password','required':True}))
   
   
    class Meta:
        fields = ('username','email','phone','password1','password2')
        model = get_user_model()
class UserProfileForm(ModelForm):
    
    username = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'user name','class':'form-ctrl','required':True,'autofocus':True}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'first name','class':'form-ctrl','required':True}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'last name','class':'form-ctrl','required':True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email(e.g you@example.com)','class':'form-ctrl','required':True}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'phone','class':'form-ctrl','required':True}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'address','class':'form-ctrl','required':True}))
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'location','class':'form-ctrl','required':True}))
    class Meta(UserCreateForm):
        model = get_user_model()
        fields = ('username','first_name','last_name','email','phone','location')
        # ('username','first_name','last_name','email','phone','location')

        excludes = ['password1','password2']
       
   
               
        
class Education_levelForm(ModelForm):
    class Meta:
        model = Education_level
        fields = ('certification','issuing_org','identification_number','issue_date','expiration_date')
        widgets = {
            'certification':forms.TextInput(attrs={'class':'form-ctrl'}),
            'issuing_org':forms.TextInput(attrs={'class':'form-ctrl'}),
            'identification_number':forms.TextInput(attrs={'class':'form-ctrl'}),
            'issue_date':forms.DateTimeInput(attrs={'class':'form-ctrl'}),
            'expiration_date':forms.DateTimeInput(attrs={'class':'form-ctrl'}),
               
        }

class Employement_DetailForm(ModelForm):
    class Meta:
        model = Employment_detail
        fields = ('employer','job_function','current_job_status','start_date','end_date')
        widgets = {
            'employer':forms.TextInput(attrs={'class':'form-ctrl'}),
            'job_function':forms.TextInput(attrs={'class':'form-ctrl'}),
            'current_job_status':forms.Select(attrs={'class':'form-ctrl'},choices=Employment_detail.JOB_STATUS),
            'start_date':forms.DateTimeInput(attrs={'class':'form-ctrl'}),
            'end_date':forms.DateTimeInput(attrs={'class':'form-ctrl'}),
                  
        }


class Preference_Form(ModelForm):
    class Meta:
        model = Preference
        fields = ('job_field_pref','location_pref')
        widgets = {
            'job_field_pref':forms.TextInput(attrs={'class':'form-ctrl'}),
            'location_pref':forms.TextInput(attrs={'class':'form-ctrl'}),
        }
class File_UploadForm(ModelForm):

    class Meta:
        model = File_uploaded
        fields = ('file_name','file','submitted_date','comments')
        widgets = {
            'file_name':forms.TextInput(attrs={'class':'form-ctrl'}),
            'file':forms.FileInput(attrs={'class':'form-ctrl'}),
            'submitted_date':forms.DateTimeInput(attrs={'class':'form-ctrl'}),
            'comments':forms.Textarea(attrs={'class':'form-ctrl' ,'rows':'2'}),
            
        }
             
        
class EmailSubscriptionForm(ModelForm):
    class Meta:
        model = Subscribers
        fields ='__all__'  
        widgets = {
            'email':forms.EmailInput(attrs={'placeholder':'Email(e.g you@example.com)','class':'grid-8 grid-md-5 input_text bg-primaryVeryLight','required':True,'maxlength':'200','title':'Email address'})
            
        }   