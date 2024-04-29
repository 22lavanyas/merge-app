from urllib import request
from django.shortcuts import render
from django.utils import timezone
from .models import Post, Category
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.models import AnonymousUser

def post_list(request):
    posts = Post.objects.select_related('category').filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if not isinstance(request.user, AnonymousUser):
                post.author = request.user 
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            if not isinstance(request.user, AnonymousUser):
                post.author = request.user 
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})




def category_list(request):
    print("cat")
    categories = Category.objects.filter(creation_date__lte=timezone.now()).order_by('creation_date')
    return render(request, 'blog/category_list.html', {'categories': categories})


def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.post_set.all()
    return render(request, 'blog/category_details.html', {'category': category, 'posts': posts})