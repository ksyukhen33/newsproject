

# Create your views here.
from django.views.generic import ListView
from news.models import Posts, Comment, Authors, Category, PostCategory


class Posts_list (ListView):
    model = Posts
    ordering = 'name_posts'
    template_name = 'posts.html'
    context_object_name = 'posts'