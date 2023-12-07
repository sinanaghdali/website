from django.shortcuts import render,get_object_or_404
from blog.models import post
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

# Create your views here.

def blog_view(reguest,cat_name=None,author_username=None):
    posts = post.objects.filter(status=1)
    if cat_name:
        posts=posts.filter(category_name=cat_name)
    if author_username:
        posts=posts.filter(author__username=author_username)
    posts = Paginator(posts, 3)
    try:
         page_number =reguest.GET.get("page")
         posts =posts.get_page(page_number)
       
    except PageNotAnInteger:       
       posts = posts.get.page(1)
    except EmptyPage:      
       posts = posts.get_page(1)
    context={'posts':posts}
    return render(reguest,'blog/blog-home.html',context)

def blog_single(reguest,pid):
    #posts = post.objects.filter(status=1)
    posts=get_object_or_404(post,id=pid,status=1)
    context={'posts':posts}
    return render(reguest,'blog/blog-single.html',context)


def test(reguest):
    #posts = post.objects.filter(status=1)
    #posts = post.objects.all()
    #context={'posts':posts}
    #posts=get_object_or_404(post,id=pid)
    #posts = post.objects.get(id=pid)
    #context={'posts':posts}
    
    return render(reguest, 'test.html')
    

def blog_category(reguest,cat_name):
    posts = post.objects.filter(status=1)
    posts=posts.filter(category_name=cat_name)
    context={'posts':posts}
    return render(reguest,'blog/blog-home.html',context)





def blog_search(reguest,cat_name=None,author_username=None):
    posts = post.objects.filter(status=1)
    if reguest.method == 'GET':
        if s := reguest.GET.get('s'):
            posts=posts.filter(content__contains=s)
        
        
    context={'posts':posts}
    return render(reguest,'blog/blog-home.html',context)