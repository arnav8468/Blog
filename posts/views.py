from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm

def home(request):
    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')
    posts = Post.objects.filter(is_published=True)

    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))
    if category_slug:
        posts = posts.filter(category__slug=category_slug)

    featured = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
    categories = Category.objects.all()
    paginator = Paginator(posts.order_by('-created_at'), 9)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    return render(request, 'posts/home.html', {
        'page_obj': page_obj,
        'featured': featured,
        'categories': categories,
        'query': query,
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('posts:post_detail', slug=slug)
    else:
        form = CommentForm()

    return render(request, 'posts/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.success(request, 'Post created successfully!')
            return redirect('posts:post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form, 'action': 'Create'})

@login_required
def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('posts:post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form, 'action': 'Update'})

@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('posts:home')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})

@login_required
def toggle_like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('posts:post_detail', slug=slug)

@login_required
def toggle_bookmark(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user in post.bookmarks.all():
        post.bookmarks.remove(request.user)
    else:
        post.bookmarks.add(request.user)
    return redirect('posts:post_detail', slug=slug)

@login_required
def bookmarked_posts(request):
    posts = request.user.bookmarked_posts.all()
    return render(request, 'posts/bookmarked.html', {'posts': posts})
