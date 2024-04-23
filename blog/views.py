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