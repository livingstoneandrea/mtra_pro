from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse,reverse_lazy
from django.conf import settings

import misaka

# Create your models here.

User = get_user_model()

class Blog_post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE  ,related_name='posts')
    blog_image = models.ImageField(upload_to='blog_posts/',blank=True,null=True)
    created_at = models.DateTimeField( auto_now=True)
    post_title = models.CharField(max_length=60)
    post_description = models.TextField()
    post_desc_html = models.TextField(editable = False)
    
    def __str__(self):
        return self.post_title
    def save(self,*args, **kwargs):
        self.post_desc_html = misaka.html(self.post_description)
        super().save(*args,**kwargs)
        
    def get_absolute_url(self):
        return reverse("posts:single", kwargs={"pk": self.pk})
    class Meta:
        ordering = ['-created_at']
        
        
