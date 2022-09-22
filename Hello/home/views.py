from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact,Post
from django.contrib import messages
from django.views.generic import ListView,DetailView,CreateView
from home.models import Post
from home.forms import Postform

# Create your views here.
def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    } 
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')

class HomeView(ListView):
    model= Post 
    template_name ='sci.html'
    ordering=['-date']

class article(DetailView):
    model=Post
    template_name ='article.html'

class AddPost(CreateView):
    model=Post
    form_class=Postform
    template_name='add_post.html'
    # fields ='__all__'


 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 