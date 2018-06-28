from .models import Post, Tag
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (CreateView, DetailView,
                                  UpdateView, DeleteView)


# Create your views here.

def blog_top_view(request):
    context = {}

    posts = Post.objects.all().filter(published_date__isnull=False).order_by('-published_date')
    tags = Tag.objects.all().order_by('-title')

    query = request.GET.get("q")
    page = request.GET.get('page')

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query)
            ).distinct()
    paginator = Paginator(posts, 10)
    try:

        posts = paginator.page(page)

    except PageNotAnInteger:

        posts = paginator.page(1)

    except EmptyPage:

        posts = paginator.page(paginator.num_pages)

    context["posts"] = posts
    context["tags"] = tags

    return render(request, "blog_top.html", context)

def blog_view_per_tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    posts = Post.objects.all().filter(tag=tag).distinct()

    context = {
        'tag':tag,
        'posts': posts,
    }

    return render(request, "blog/view_per_tag.html", context)

class PostDetailView(DetailView):
    model = Post
    slug_field = "title"

class NovoPost(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    redirect_field_name = "post_detail.html"
    form_class = PostForm
    model = Post

class AtualizarPost(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'post_detail.html'
    form_class = PostForm
    model = Post

@login_required
def rascunhos(request):
    context = {}
    posts = Post.objects.all().filter(published_date__isnull=True).order_by('create_date')

    query = request.GET.get("q")
    page = request.GET.get('page')

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query)
            ).distinct()

    paginator = Paginator(posts, 25)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context["posts"] = posts

    return render(request, 'blog_drafts.html', context)

class Remover_Post(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog_top')

@login_required
def publicar_post(request, slug, pk):
    post = get_object_or_404(Post, slug=slug)
    post.publish()
    return redirect('post_detail', slug=slug, pk=pk)

