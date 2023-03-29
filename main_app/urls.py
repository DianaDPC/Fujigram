from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/',views.signup, name='signup'),
    # search path
    path('search/',views.search_index, name='search_index'),
    # posts paths
    path('posts/',views.posts_index, name='posts_index'),
    path('posts/<int:post_id>/',views.post_details, name='post_details'),
    path('posts/create/', views.PostCreate.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    # comment paths
    path('posts/<int:post_id>/comment_add/', views.comment_add, name='comment_add'),
    path('posts/<int:post_id>/comment/<int:pk>/update_comment/', views.CommentUpdate.as_view(), name='comment_update'),
    path('posts/<int:post_id>/comment/<int:pk>/delete_comment/', views.CommentDelete.as_view(), name='comment_delete'),
    # recipe paths
    path('recipes/', views.recipes_index, name='recipes_index'),
    path('recipes/create',views.RecipeCreate.as_view(), name='recipes_create'),
    path('recipe/create',views.RecipeCreate.as_view(), name='recipes_create'),
    path('recipe/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipes_update'),
    path('recipe/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipes_delete'),
]
