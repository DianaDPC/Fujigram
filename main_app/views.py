from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Recipe, Post, Comment



# Create your views here.

class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  fields = '__all__'

class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  fields = '__all__'

class PostDelete(LoginRequiredMixin, DeleteView):
  model = Post
  success_url = '/posts/'

def home(request):
  return render(request, 'home.html')

def posts_index(request):
  posts = Post.objects.all()
  return render(request, 'posts/index.html', { 'posts': posts })

def posts_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'posts/detail.html', { 'post': post })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - Try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
