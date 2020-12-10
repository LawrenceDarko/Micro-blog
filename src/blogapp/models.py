from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default = None, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50]+'...'
    
    