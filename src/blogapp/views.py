from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    #return HttpResponse("I'm in the views page")
    articles = Article.objects.all().order_by('date')
    return render(request, 'blogapp/article_list.html', {'articles':articles})

def article_detail(request, slug):
    #return render(request, 'blogapp/detail.html')
    article = Article.objects.get(slug=slug)
    return render(request, 'blogapp/article_detail.html', {'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user 
            form.save()
            return redirect('blogapp:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'blogapp/article_create.html', {'form':form})