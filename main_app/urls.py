from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/',views.signup, name='signup'),
    path('recipe/create',views.RecipeCreate.as_view(), name='recipes_create'),
    
    # path('posts/', views.posts_index, name='posts_index'),
    # path('posts/<int:post_id>/', views.posts_detail, name='posts_detail'),
    # path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
]
