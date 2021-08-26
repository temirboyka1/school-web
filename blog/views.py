from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from taggit.models import Tag
from .models import Post

def post_list(request, tag_slug=None):

    object_list = Post.objects.filter(status='published').all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,'blog/post/blog.html', locals())


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug = post, status = 'published', publish__year = year,
    							publish__month = month, publish__day = day)
    post.views += 1
    post.save()

    last_posts = Post.objects.order_by("-publish")[:3]
    all_tags = Tag.objects.all()
   
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:3]

    return render(request, 'blog/post/blog-details.html', locals() )
