from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    # username = None
    email = models.EmailField(_('email address'),unique=True)
    phone = models.CharField(max_length=11,blank=True,null=True)
    address = models.CharField(max_length=60,blank=True,null=True)
    location = models.CharField(max_length=60,blank=True,null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    # @property
    # def group_name(self):
    #     """
    #     Returns a group name based on the user's id to be used by Django Channels.
    #     Example usage:
    #     user = User.objects.get(pk=1)
    #     group_name = user.group_name
    #     """
    #     return "user_%s" % self.id
    
    def __str__(self):
        return self.email

class Employment_detail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    employer = models.CharField(max_length=150, blank=True, null=True)
    job_function = models.CharField(max_length=100, blank=True, null=True)
    JOB_STATUS = (
        ('not employed', 'Not Employed'),
        ('employed', ' Employed')

    )

    current_job_status = models.CharField(max_length=20, choices=JOB_STATUS)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.employer


class Education_level(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    certification = models.CharField(max_length=100, null=True)
    issuing_org = models.CharField(max_length=100, null=True)
    identification_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.certification


class Preference(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    job_field_pref = models.CharField(max_length=100, null=True)
    location_pref = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "{}".format(self.job_field_pref)


class File_uploaded(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    file_name = models.CharField(max_length=250,blank=True)
    file = models.FileField(upload_to='user_files/',blank=True)
    submitted_date = models.DateTimeField(default=timezone.now)
    comments = models.TextField()

    def __str__(self):
        return self.file_name
       
class Subscribers(models.Model):
    email = models.EmailField(max_length=100,unique=True)
    def __str__(self):
        return self.email