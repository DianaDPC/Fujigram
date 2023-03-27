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

class RecipeCreate(CreateView):
  model = Recipe
  fields = ['name','sensor','dynamic_range','film_simulation','monochromatic_color_WC','monochromatic_color_MG','highlight_tone','shadow_tone','color','noise_reduction','clarity','grain_effect','grain_size','color_chrome_effect','white_balance','white_balance_shift_red','white_balance_shift_blue','sharpness','long_exposure_nr','lens_modulation_optimizer','color_space','iso','exposure_compensation']

  def form_valid(self, form):
    form.instance.user_id = self.request.user
    return super().form_valid(form)
  
