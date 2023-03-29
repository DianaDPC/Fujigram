from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.postgres.search import SearchVector
from .models import Recipe, Post, Comment
from .forms import CommentForm


def home(request):
  return render(request, 'home.html')

@login_required
def posts_index(request):
  posts = Post.objects.all()
  return render(request, 'posts/index.html', { 'posts': posts })

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

@login_required
def post_details(request, post_id):
  post=Post.objects.get(id=post_id)
  comments=post.comment_set.all()
  comment_form = CommentForm()
  return render(request, 'posts/details.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['camera_used', 'photo', 'msg_body', 'recipe']
  success_url = '/posts/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  fields = ['camera_used', 'msg_body']

  def test_func(self):
    obj = self.get_object()
    return obj.user == self.request.user

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Post
  success_url = '/posts/'

  def test_func(self):
    obj = self.get_object()
    return obj.user == self.request.user
  
class RecipeCreate(LoginRequiredMixin, CreateView):
  model = Recipe
  fields = ['name','sensor','dynamic_range','film_simulation','monochromatic_color_WC','monochromatic_color_MG','highlight_tone','shadow_tone','color','noise_reduction','clarity','grain_effect','grain_size','color_chrome_effect','white_balance','white_balance_shift_red','white_balance_shift_blue','sharpness','long_exposure_nr','lens_modulation_optimizer','color_space','iso','exposure_compensation']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

@login_required  
def recipes_index(request):
  recipes = Recipe.objects.all()
  return render(request, 'recipes/index.html',{'recipes':recipes})

@login_required
def comment_add(request, post_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.post_id = post_id
    new_comment.user_id = request.user.id
    new_comment.save()
    return redirect('post_details', post_id=post_id)
  
class CommentUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Comment
  fields = ['msg_body']

  def test_func(self):
    obj = self.get_object()
    return obj.user == self.request.user

class CommentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Comment
  success_url = '/posts/'

  def test_func(self):
    obj = self.get_object()
    return obj.user == self.request.user

class RecipeUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Recipe
  fields = ['name','sensor','dynamic_range','film_simulation','monochromatic_color_WC','monochromatic_color_MG','highlight_tone','shadow_tone','color','noise_reduction','clarity','grain_effect','grain_size','color_chrome_effect','white_balance','white_balance_shift_red','white_balance_shift_blue','sharpness','long_exposure_nr','lens_modulation_optimizer','color_space','iso','exposure_compensation']
  success_url = '/recipes/'

  def test_func(self):
    obj = self.get_object()
    return obj.user == self.request.user

class RecipeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Recipe
  success_url = '/recipes/'

  def test_func(self):
    obj = self.get_object()
    return obj.user == self.request.user

def search_index(request):
  q=request.GET.get('query')
  posts=Post.objects.annotate(
  search=SearchVector('camera_used'),
  ).filter(search=q)
  if (len(posts) < 1):
    posts=Recipe.objects.annotate(
    search=SearchVector('name', 'sensor'),
    ).get(search=q).post_set.all()
  return render(request, 'posts/index.html', {'posts':posts})
