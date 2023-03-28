from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Recipe, Post, Comment


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
  
class RecipeCreate(CreateView):
  model = Recipe
  fields = ['name','sensor','dynamic_range','film_simulation','monochromatic_color_WC','monochromatic_color_MG','highlight_tone','shadow_tone','color','noise_reduction','clarity','grain_effect','grain_size','color_chrome_effect','white_balance','white_balance_shift_red','white_balance_shift_blue','sharpness','long_exposure_nr','lens_modulation_optimizer','color_space','iso','exposure_compensation']

  def form_valid(self, form):
    form.instance.user_id = self.request.user
    return super().form_valid(form)
  
def recipes_index(request):
  recipes = Recipe.objects.all()
  return render(request, 'recipes/index.html',{'recipes':recipes})