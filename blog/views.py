from django.shortcuts import render
from blog.models import Blog
    
    
def blogs_view(request):
    b= Blog.objects.all()
    context ={
        'blogs':b
    }
    return render(request, 'blogs.html', context)

def single_blog(request,pk):
    b = Blog.objects.get(id=pk)
    context = {
        'blog':b
    }
    return render(request,'blog.html',context)


def search(request):
    q = request.GET['q']
    blogs = Blog.objects.filter(title__contains=q)
    context = {
        'blogs':blogs
    }
    return render(request,'search.html',context)