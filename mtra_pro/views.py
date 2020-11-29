from django.views.generic import TemplateView,View
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Subscribers
from posts.models import Blog_post

from django.contrib.auth import get_user_model

User = get_user_model()


class HomePage(TemplateView):
    template_name = 'index.html'
    
class TestPage(TemplateView):
    template_name = 'test.html'    
    
class ThanksPage(TemplateView):
    template_name = 'thanks.html'  
class IndexPage(FormMixin , View):
    model = User
    template_name = 'index.html'
    form_class = None
    
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
            
            context["users"] = User.objects.count
            # context["countries"] = Countries.objects.count
            context["subscribers"]= Subscribers.objects.count
            context["blog_posts"]= Blog_post.objects.all()[:3]
        except Exception as e :
            return JsonResponse({"errors":e.message},status=400)
        
        return context 
    
    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name,self.get_context_data())
    def post(self, request, *args, **kwargs):
        if self.request.is_ajax and self.request.method == "POST":
            if 'subsc_form' in request.POST:
                #get subsc form
                try:
                    form_class = self.get_form_class()
                    form_name = 'subsc_form'
                except Exception as e:
                    print('Exception occurred {}'.format(e))
                    
            #get the form
            form = self.get_form(form_class,self.request.POST)        
            
            if form.is_valid():
                instance = form.save(commit = False)
                
                instance.save() 
                
                #send to client side
                return JsonResponse({"message":"Your details submmitted & proccessed succeful","user":serializers.serialize('json',[instance,])},status=200)
            else:
                return JsonResponse({"errors":form.errors},status=400)
        return JsonResponse({"errors":""},status=400)          
        pass
        
        
def EmailSubscriptions(request):
    
    if request.is_ajax and request.method == "POST":
        
        print("form is valid")
        instance = Subscribers(email=request.POST.get('email'))  
        instance.save()
        print("user subscription added")

        return JsonResponse({"message": "subscription succesful" }, status=200)
    else:
            # some form errors occured.
        return JsonResponse({"error": "Error occured"}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400) 