from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from .models import Post
from django.shortcuts import render
# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class Blogline(ListView):
    template_name = "articles.html"
    model = Post

class DetailPost(DetailView):
    template_name = "detail.html"
    model = Post

def Home(request):
    return render(request, 'home.html')

def Sources(request):
    return render(request, 'sources.html')

def About(request):
    return render(request, 'about.html')