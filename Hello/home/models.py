from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    
class Post(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__ (self):
        return self.title + '|' +str(self.author)
    
    def get_absolute_url(self):
        return reverse("article", kwargs={"pk": self.pk})
    
    
    