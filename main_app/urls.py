from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/',views.signup, name='signup'),
    # posts paths
    path('posts/',views.posts_index, name='posts_index'),
    path('posts/<int:post_id>/',views.post_details, name='post_details'),
    path('posts/create/', views.PostCreate.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    # recipe paths
    path('recipe/create',views.RecipeCreate.as_view(), name='recipes_create'),
    path('recipe/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
    path('recipe/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
    # comments paths
  
]
