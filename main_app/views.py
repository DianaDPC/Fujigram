from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# to be implemented later with other routes
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin 

from .models import Recipe, Post, Comment

def home(request):
  return render(request, 'home.html')

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

def posts_index(request):
  posts=Post.objects.all()
  return render(request, 'posts/index.html', {'posts':posts})

def post_details(request, post_id):
  post=Post.objects.get(id=post_id)
  return render(request, 'posts/details.html', {'post':post})

class PostCreate(CreateView):
  model = Post
  fields = ['camera_used', 'photo', 'msg_body']
  success_url = '/posts/'

class PostUpdate(UpdateView):
  model = Post
  fields = ['camera_used', 'msg_body']
  success_url = '/posts/'

class PostDelete(DeleteView):
  model = Post
  success_url = '/posts/'