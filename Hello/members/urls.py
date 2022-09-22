
from django.urls import path
from members.views import UserRegisterView


urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('login/',UserRegisterView.as_view(),name='login'),
]