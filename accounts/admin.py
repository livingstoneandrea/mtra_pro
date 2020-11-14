from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm,CustomUserChangeForm
from accounts.models import (Education_level, Employment_detail, File_uploaded, Preference,User,Subscribers)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    models = User
    
    list_display = ('username','email','phone','is_staff','is_active',)
    list_filter = ('username','email','phone','is_staff','is_active',)
    fieldsets = (
        (None, {
            "fields": (
                'username','email','phone','password'
            ),
        }),
        ("permissions",{'fields':('is_staff','is_active')}),
    )
    
    add_fieldsets = (
        (None,{
            'classes':('wide'),
            'fields':('username','email','phone','password1','password2','is_staff','is_active')
        }),      
    )
    
    search_fields = ('email',)
    ordering = ('email',)
    

# Register your models here.
admin.site.register(User, CustomUserAdmin)
# admin.site.register(Profile)
admin.site.register(Education_level)
admin.site.register(Employment_detail)
admin.site.register(Preference)
admin.site.register(File_uploaded)
admin.site.register(Subscribers)
