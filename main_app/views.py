from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.forms import ModelForm
from .models import Recipe, Post, Comment


# Create your views here.
def posts_index(request):
  posts = Post.objects.all()
  return render(request, 'posts/index.html', { 'posts': posts })

def posts_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'posts/detail.html', { 'post': post })

class PostCreate(CreateView):
    model = Post
    fields = '__all__'

class RecipeCreate(CreateView):
   model = Post
   fields = '__all__'
