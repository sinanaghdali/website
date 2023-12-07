from django import template
from blog.models import post,category

register = template.Library()

@register.simple_tag(name='counters')
def hello():
    posts=post.objects.filter(status=1).count()
    return posts


@register.simple_tag(name='posts')
def hello():
    posts=post.objects.filter(status=1)
    return posts
@register.filter
def snippet(value,arg=20):
    return value[:arg]

@register.inclusion_tag('blog/blog-popularpost.html')
def popularpost():
    posts=post.objects.filter(status=1).order_by('publish_date')[:2]
    return {'posts':posts}


@register.inclusion_tag('blog/blog-category.html')
def postcategories():
    posts=post.objects.filter(status=1)
    categories=category.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()