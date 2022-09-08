import http
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    # return HttpResponse("This is aboutpage")
    return render(request,'about.html')

def services(request):
    # return HttpResponse("This is services")
    return render(request,'services.html')
def contact(request):
    # return HttpResponse("This is contact page")
    return render(request,'contact.html')