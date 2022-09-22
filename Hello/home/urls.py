from django.contrib import admin
from django.urls import path
from home import views
from  home.views import AddPost, HomeView,article
from members.views import UserRegisterView
urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    
    path('sci',HomeView.as_view(),name='sci'),
    path('article/<int:pk>',article.as_view(),name='article'),
    path('add_post/',AddPost.as_view(),name='add_post'),
    path('register/',UserRegisterView.as_view(),name='register'),
    path('login/',UserRegisterView.as_view(),name='login'),


]