from django.views.generic import TemplateView
from django.http.response import JsonResponse
from accounts.models import Subscribers


class HomePage(TemplateView):
    template_name = 'index.html'
    
class TestPage(TemplateView):
    template_name = 'test.html'    
    
class ThanksPage(TemplateView):
    template_name = 'thanks.html'    
        
        
        
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