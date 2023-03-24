from django.contrib import admin
from .models import Recipe, Post, Comment

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Post)
admin.site.register(Comment)