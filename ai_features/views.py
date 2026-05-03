from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .services import generate_blog_content, generate_summary, suggest_tags, improve_grammar
from posts.forms import PostForm
from posts.models import Post, Category

@login_required
def ai_generate(request):
    content = ''
    if request.method == 'POST':
        title = request.POST.get('title', '')
        keywords = request.POST.get('keywords', '')
        content = generate_blog_content(title, keywords)
        
        if content:
            slug = title.lower().replace(' ', '-').replace('.', '').replace(',', '').replace('?', '')
            
            post = Post.objects.create(
                title=title,
                content=content,
                author=request.user,
                is_published=True,
                is_ai_generated=True
            )
            
            if keywords:
                tag_list = [k.strip() for k in keywords.split(',') if k.strip()]
                post.tags.add(*tag_list)
            
            messages.success(request, 'AI-generated post published successfully!')
            return redirect('posts:post_detail', slug=post.slug)
        else:
            messages.error(request, 'Failed to generate content. Please try again.')
    
    return render(request, 'ai_features/generate.html', {'content': content})

@login_required
def ai_summary(request, post_id):
    post = Post.objects.get(id=post_id)
    summary = generate_summary(post.content)
    return render(request, 'ai_features/summary.html', {'post': post, 'summary': summary})

@login_required
def ai_suggest_tags(request, post_id):
    post = Post.objects.get(id=post_id)
    tags = suggest_tags(post.content)
    return render(request, 'ai_features/suggest_tags.html', {'post': post, 'tags': tags})

@login_required
def ai_improve(request, post_id):
    post = Post.objects.get(id=post_id)
    improved = improve_grammar(post.content)
    return render(request, 'ai_features/improve.html', {'post': post, 'improved': improved})
