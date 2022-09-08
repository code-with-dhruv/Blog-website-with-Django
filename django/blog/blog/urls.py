
from django.contrib import admin
from django.urls import path,include

#how to change django admin text
# django admin text change just copy and past this code in you project urls.py
admin.site.site_header = "PROUD NATIONALISTS"
admin.site.site_title = "ADMIN PORTAL"
admin.site.index_title = "Welcome to all"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),

    

]
