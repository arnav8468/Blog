from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from posts.models import Post, Category
from django.db.models import Count
from datetime import datetime, timedelta

User = get_user_model()

@login_required
def overview(request):
    total_posts = Post.objects.count()
    total_users = User.objects.count()
    total_categories = Category.objects.count()

    # Posts per day for last 7 days
    last_week = datetime.now() - timedelta(days=7)
    posts_by_day = (Post.objects
        .filter(created_at__gte=last_week)
        .extra({'date': "date(created_at)"})
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date'))

    return render(request, 'dashboard/overview.html', {
        'total_posts': total_posts,
        'total_users': total_users,
        'total_categories': total_categories,
        'posts_by_day': list(posts_by_day),
        'recent_posts': Post.objects.order_by('-created_at')[:5],
    })

@login_required
def posts_management(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'dashboard/posts.html', {'posts': posts})

@login_required
def users_management(request):
    users = User.objects.all().annotate(post_count=Count('posts'))
    return render(request, 'dashboard/users.html', {'users': users})
